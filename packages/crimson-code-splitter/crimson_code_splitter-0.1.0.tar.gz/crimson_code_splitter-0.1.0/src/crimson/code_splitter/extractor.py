from .chunker import chunk_code, CodeChunk, Chunk, InClassChunk
from crimson.file_loader import filter_source, Search_
from typing import List


def collect_chunks(
    source: str,
    includes: List[str] = [],
    excludes: List[str] = [],
    search: Search_.annotation = Search_.default,
) -> List[Chunk]:
    paths = filter_source(
        source=source, includes=includes, excludes=excludes, search=search
    )

    chunks = []

    for path in paths:
        with open(path, "r") as file:
            content = file.read()

        chunks.extend(chunk_code(content, path))

    return chunks


def flat_chunks(chunks: List[CodeChunk]) -> List[Chunk]:
    new_chunks = []

    for chunk in chunks:
        new_chunks.append(chunk)
        if chunk.sub_chunks is not None:
            new_chunks.extend(chunk.sub_chunks)

    return new_chunks


def extract_source_info(chunk: Chunk) -> str:
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


def generate_chunks_with_source_info(chunks: List[CodeChunk]) -> List[str]:
    processed_chunks = []

    flatten_chunks = flat_chunks(chunks)

    for chunk in flatten_chunks:
        source_info = ["**source info**"]
        source_info.extend(extract_source_info(chunk))
        source_info.append("**code**")
        source_info.append(chunk.code)
        processed_chunks.append("\n".join(source_info))

    return processed_chunks


def extract_chunks(
    source: str,
    includes: List[str] = [],
    excludes: List[str] = [],
    search: Search_.annotation = Search_.default,
) -> List[Chunk]:
    chunks = collect_chunks(
        source=source, includes=includes, excludes=excludes, search=search
    )

    chunks = generate_chunks_with_source_info(chunks)

    return chunks
