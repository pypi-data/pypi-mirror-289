# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Decode files from a raw binary format to a PyArrow Table.
"""

import io
from enum import Enum
from typing import BinaryIO
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

import numpy
import pyarrow
from orso.tools import random_string
from pyarrow import parquet

from opteryx.connectors.capabilities import PredicatePushable
from opteryx.exceptions import UnsupportedFileTypeError
from opteryx.managers.expression import NodeType
from opteryx.managers.expression import get_all_nodes_of_type
from opteryx.utils.arrow import post_read_projector
from opteryx.utils.memory_view_stream import MemoryViewStream


class ExtentionType(str, Enum):
    """labels for the file extentions"""

    DATA = "DATA"
    CONTROL = "CONTROL"


def convert_arrow_schema_to_orso_schema(arrow_schema):
    from orso.schema import FlatColumn
    from orso.schema import RelationSchema

    return RelationSchema(
        name="arrow",
        columns=[FlatColumn.from_arrow(field) for field in arrow_schema],
    )


def get_decoder(dataset: str) -> Callable:
    """helper routine to get the decoder for a given file"""
    ext = dataset.split(".")[-1].lower()
    if ext not in KNOWN_EXTENSIONS:  # pragma: no cover
        raise UnsupportedFileTypeError(f"Unsupported file type - {ext}")
    file_decoder, file_type = KNOWN_EXTENSIONS[ext]
    if file_type != ExtentionType.DATA:  # pragma: no cover
        raise UnsupportedFileTypeError(f"File is not a data file - {ext}")
    return file_decoder


def do_nothing(buffer: Union[memoryview, bytes], **kwargs):  # pragma: no cover
    """for when you need to look like you're doing something"""
    return False


def filter_records(filter: Optional[Union[List, Tuple]], table: pyarrow.Table):
    """
    When we can't push predicates to the actual read, use this to filter records
    just after the read.
    """
    # notes:
    #   at this point we've not renamed any columns, this may affect some filters
    from opteryx.managers.expression import NodeType
    from opteryx.managers.expression import evaluate
    from opteryx.models import Node

    if isinstance(filter, list) and filter:
        filter_copy = list(filter)
        root = filter_copy.pop()

        if root.left.node_type == NodeType.IDENTIFIER:
            root.left.schema_column.identity = root.left.source_column
        if root.right.node_type == NodeType.IDENTIFIER:
            root.right.schema_column.identity = root.right.source_column

        while filter_copy:
            right = filter_copy.pop()
            if right.left.node_type == NodeType.IDENTIFIER:
                right.left.schema_column.identity = right.left.source_column
            if right.right.node_type == NodeType.IDENTIFIER:
                right.right.schema_column.identity = right.right.source_column
            root = Node(
                NodeType.AND,
                left=root,
                right=right,
                schema_column=Node("schema_column", identity=random_string()),
            )
    else:
        root = filter

    mask = evaluate(root, table)
    return table.filter(mask)


def zstd_decoder(
    buffer: Union[memoryview, bytes],
    *,
    projection: Optional[list] = None,
    selection: Optional[list] = None,
    just_schema: bool = False,
    **kwargs,
) -> Tuple[int, int, pyarrow.Table]:
    """
    Read zstandard compressed JSONL files
    """
    import zstandard

    stream: BinaryIO = None
    stream = MemoryViewStream(buffer) if isinstance(buffer, memoryview) else io.BytesIO(buffer)

    with zstandard.open(stream, "rb") as file:
        return jsonl_decoder(
            file, projection=projection, selection=selection, just_schema=just_schema
        )


def lzma_decoder(
    buffer: Union[memoryview, bytes],
    *,
    projection: Optional[list] = None,
    selection: Optional[list] = None,
    just_schema: bool = False,
    **kwargs,
) -> Tuple[int, int, pyarrow.Table]:
    """
    Read lzma compressed JSONL files
    """
    import lzma

    stream: BinaryIO = None
    stream = MemoryViewStream(buffer) if isinstance(buffer, memoryview) else io.BytesIO(buffer)

    with lzma.open(stream, "rb") as file:
        return jsonl_decoder(
            file, projection=projection, selection=selection, just_schema=just_schema
        )


def parquet_decoder(
    buffer: Union[memoryview, bytes],
    *,
    projection: Optional[list] = None,
    selection: Optional[list] = None,
    just_schema: bool = False,
    force_read: bool = False,
) -> Tuple[int, int, pyarrow.Table]:
    """
    Read parquet formatted files.

    Parameters:
        buffer: Union[memoryview, bytes]
            The input buffer containing the parquet file data.
        projection: List, optional
            List of columns to project.
        selection: optional
            The selection filter.
        just_schema: bool, optional
            Flag to indicate if only schema is needed.
        force_read: bool, optional
            Flag to skip some optimizations.
    Returns:
        Tuple containing number of rows, number of columns, and the table or schema.
    """
    selected_columns = None

    # we need to work out if we have a selection which may force us
    # fetching columns just for filtering
    dnf_filter, selection = PredicatePushable.to_dnf(selection) if selection else (None, None)

    # try to avoid turning a memoryview buffer into bytes, it's quite slow
    stream: BinaryIO = (
        MemoryViewStream(buffer) if isinstance(buffer, memoryview) else io.BytesIO(buffer)
    )

    # Open the parquet file only once
    parquet_file = parquet.ParquetFile(stream)

    if projection or just_schema or selection:
        # Return just the schema if that's all that's needed
        if just_schema:
            return convert_arrow_schema_to_orso_schema(parquet_file.schema_arrow)

        # Projection processing
        columns_in_filters = {
            c.value for c in get_all_nodes_of_type(selection, (NodeType.IDENTIFIER,))
        }
        arrow_schema_columns_set = set(parquet_file.schema_arrow.names)
        projection_names = {
            name for proj_col in projection for name in proj_col.schema_column.all_names
        }.union(columns_in_filters)
        selected_columns = list(arrow_schema_columns_set.intersection(projection_names))

        # If no columns are selected, set to None
        if not selected_columns:
            selected_columns = None

        if not columns_in_filters.issubset(arrow_schema_columns_set):
            if selected_columns is None:
                selected_columns = list(arrow_schema_columns_set)
            fields = [pyarrow.field(name, pyarrow.string()) for name in selected_columns]
            schema = pyarrow.schema(fields)

            # Create an empty table with the schema
            empty_table = pyarrow.Table.from_arrays(
                [pyarrow.array([], type=schema.field(i).type) for i in range(len(fields))],
                schema=schema,
            )

            return (
                parquet_file.metadata.num_rows,
                parquet_file.metadata.num_columns,
                empty_table,
            )

    if selected_columns is None and not force_read:
        selected_columns = []

    # Read the parquet table with the optimized column list and selection filters
    table = parquet.read_table(
        stream,
        columns=selected_columns,
        pre_buffer=False,
        filters=dnf_filter,
        use_threads=False,
    )
    # Any filters we couldn't push to PyArrow to read we run here
    if selection:
        table = filter_records(selection, table)

    return (parquet_file.metadata.num_rows, parquet_file.metadata.num_columns, table)


def orc_decoder(
    buffer: Union[memoryview, bytes],
    *,
    projection: Optional[list] = None,
    selection: Optional[list] = None,
    just_schema: bool = False,
    **kwargs,
) -> Tuple[int, int, pyarrow.Table]:
    """
    Read orc formatted files
    """
    import pyarrow.orc as orc

    stream: BinaryIO = None
    stream = MemoryViewStream(buffer) if isinstance(buffer, memoryview) else io.BytesIO(buffer)
    orc_file = orc.ORCFile(stream)

    if just_schema:
        orc_schema = orc_file.schema
        return convert_arrow_schema_to_orso_schema(orc_schema)

    table = orc_file.read()
    full_shape = table.shape
    if selection:
        table = filter_records(selection, table)
    if projection:
        table = post_read_projector(table, projection)
    return *full_shape, table


def jsonl_decoder(
    buffer: Union[memoryview, bytes],
    *,
    projection: Optional[list] = None,
    selection: Optional[list] = None,
    just_schema: bool = False,
    **kwargs,
) -> Tuple[int, int, pyarrow.Table]:
    import pyarrow.json

    stream: BinaryIO = None
    if isinstance(buffer, memoryview):
        stream = MemoryViewStream(buffer)
    elif isinstance(buffer, bytes):
        stream = io.BytesIO(buffer)
    else:
        stream = buffer

    table = pyarrow.json.read_json(stream)
    schema = table.schema
    if just_schema:
        return convert_arrow_schema_to_orso_schema(schema)

    full_shape = table.shape
    if selection:
        table = filter_records(selection, table)
    if projection:
        table = post_read_projector(table, projection)

    return *full_shape, table


def csv_decoder(
    buffer: Union[memoryview, bytes],
    *,
    projection: Optional[list] = None,
    selection: Optional[list] = None,
    just_schema: bool = False,
    delimiter: str = ",",
    **kwargs,
) -> Tuple[int, int, pyarrow.Table]:
    import pyarrow.csv
    from pyarrow.csv import ParseOptions

    stream: BinaryIO = None
    stream = MemoryViewStream(buffer) if isinstance(buffer, memoryview) else io.BytesIO(buffer)
    parse_options = ParseOptions(delimiter=delimiter, newlines_in_values=True)
    table = pyarrow.csv.read_csv(stream, parse_options=parse_options)
    schema = table.schema
    if just_schema:
        return convert_arrow_schema_to_orso_schema(schema)

    full_shape = table.shape
    if selection:
        table = filter_records(selection, table)
    if projection:
        table = post_read_projector(table, projection)

    return *full_shape, table


def tsv_decoder(
    buffer: Union[memoryview, bytes],
    *,
    projection: Optional[list] = None,
    selection: Optional[list] = None,
    just_schema: bool = False,
    **kwargs,
) -> Tuple[int, int, pyarrow.Table]:
    return csv_decoder(
        buffer=buffer,
        projection=projection,
        selection=selection,
        delimiter="\t",
        just_schema=just_schema,
    )


def arrow_decoder(
    buffer: Union[memoryview, bytes],
    *,
    projection: Optional[list] = None,
    selection: Optional[list] = None,
    just_schema: bool = False,
    **kwargs,
) -> Tuple[int, int, pyarrow.Table]:
    import pyarrow.feather as pf

    stream: BinaryIO = None
    stream = MemoryViewStream(buffer) if isinstance(buffer, memoryview) else io.BytesIO(buffer)
    table = pf.read_table(stream)
    schema = table.schema
    if just_schema:
        return convert_arrow_schema_to_orso_schema(schema)

    full_shape = table.shape
    if selection:
        table = filter_records(selection, table)
    if projection:
        table = post_read_projector(table, projection)

    return *full_shape, table


def avro_decoder(
    buffer: Union[memoryview, bytes],
    *,
    projection: Optional[list] = None,
    selection: Optional[list] = None,
    just_schema: bool = False,
    **kwargs,
) -> Tuple[int, int, pyarrow.Table]:
    """
    AVRO isn't well supported, it is converted between table types which is
    really slow
    """
    try:
        from avro.datafile import DataFileReader
        from avro.io import DatumReader
    except ImportError:  # pragma: no cover
        raise Exception("`avro` is missing, please install or include in your `requirements.txt`.")

    stream: BinaryIO = None
    stream = MemoryViewStream(buffer) if isinstance(buffer, memoryview) else io.BytesIO(buffer)
    reader = DataFileReader(stream, DatumReader())

    table = pyarrow.Table.from_pylist(list(reader))
    schema = table.schema
    if just_schema:
        return convert_arrow_schema_to_orso_schema(schema)

    full_shape = table.shape
    if selection:
        table = filter_records(selection, table)
    if projection:
        table = post_read_projector(table, projection)

    return *full_shape, table


def ipc_decoder(
    buffer: Union[memoryview, bytes],
    *,
    projection: Optional[list] = None,
    selection: Optional[list] = None,
    just_schema: bool = False,
    **kwargs,
) -> Tuple[int, int, pyarrow.Table]:
    from itertools import chain

    from pyarrow import ipc

    stream: BinaryIO = None
    stream = MemoryViewStream(buffer) if isinstance(buffer, memoryview) else io.BytesIO(buffer)
    reader = ipc.open_stream(stream)

    batch_one = next(reader, None)
    if batch_one is None:
        return None

    schema = batch_one.schema

    if just_schema:
        return convert_arrow_schema_to_orso_schema(schema)

    table = pyarrow.Table.from_batches([batch for batch in chain([batch_one], reader)])
    full_shape = table.shape
    if selection:
        table = filter_records(selection, table)
    if projection:
        table = post_read_projector(table, projection)

    return *full_shape, table


# for types we know about, set up how we handle them
KNOWN_EXTENSIONS: Dict[str, Tuple[Callable, str]] = {
    "avro": (avro_decoder, ExtentionType.DATA),
    "complete": (do_nothing, ExtentionType.CONTROL),
    "manifest": (do_nothing, ExtentionType.CONTROL),
    "ignore": (do_nothing, ExtentionType.CONTROL),
    "arrow": (arrow_decoder, ExtentionType.DATA),  # feather
    "csv": (csv_decoder, ExtentionType.DATA),
    "ipc": (ipc_decoder, ExtentionType.DATA),
    "jsonl": (jsonl_decoder, ExtentionType.DATA),
    "orc": (orc_decoder, ExtentionType.DATA),
    "parquet": (parquet_decoder, ExtentionType.DATA),
    "tsv": (tsv_decoder, ExtentionType.DATA),
    "zstd": (zstd_decoder, ExtentionType.DATA),  # jsonl/zstd
    "lzma": (lzma_decoder, ExtentionType.DATA),  # jsonl/lzma
}

VALID_EXTENSIONS = set(f".{ext}" for ext in KNOWN_EXTENSIONS)
TUPLE_OF_VALID_EXTENSIONS = tuple(VALID_EXTENSIONS)
DATA_EXTENSIONS = set(
    f".{ext}" for ext, conf in KNOWN_EXTENSIONS.items() if conf[1] == ExtentionType.DATA
)
