from .chunker import chunk_code, CodeChunk, Chunk, InClassChunk
from crimson.file_loader import filter_source, Search_
from typing import List, TypedDict, Optional


class Code(TypedDict):
    content: str
    path: Optional[str]


def collect_chunks_from_source(
    source: str,
    includes: List[str] = [],
    excludes: List[str] = [],
    search: Search_.annotation = Search_.default,
    flat: bool = True,
) -> List[Chunk]:
    paths = filter_source(
        source=source, includes=includes, excludes=excludes, search=search
    )

    chunks = []

    for path in paths:
        with open(path, "r") as file:
            content = file.read()

        chunks.extend(chunk_code(content, path))

    chunks = flat_chunks(chunks=chunks, turn_on=flat)

    return chunks


def collect_chunks(codes: List[Code], flat: bool = True) -> List[CodeChunk]:
    chunks = []
    for code in codes:
        content = code["content"]
        path = code["path"]
        chunks.extend(chunk_code(content, path))

    if flat is True:
        chunks = flat_chunks(chunks=chunks, turn_on=flat)
    return chunks


def flat_chunks(chunks: List[CodeChunk], turn_on: bool = True) -> List[Chunk]:
    if turn_on is False:
        return chunks

    new_chunks = []

    for chunk in chunks:
        new_chunks.append(chunk)
        if chunk.sub_chunks is not None:
            new_chunks.extend(chunk.sub_chunks)

    return new_chunks


def get_source_info_as_string(chunk: Chunk) -> str:
    source = []
    if chunk.path is not None:
        source.append(f"path: {chunk.path}")

    source.append(f"start line: {chunk.start_line}")

    if isinstance(chunk, CodeChunk):
        source.append(f"{chunk.type}: {chunk.name}")

    if isinstance(chunk, InClassChunk):
        source.append(f"class: {chunk.parent}")
        source.append(f"{chunk.type}: {chunk.name}")

    return source
