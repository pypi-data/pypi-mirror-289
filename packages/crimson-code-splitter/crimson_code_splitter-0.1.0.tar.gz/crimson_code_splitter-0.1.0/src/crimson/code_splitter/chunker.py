from typing import List, Optional, Literal
import ast


class Chunk:
    def __init__(
        self,
        type: Literal["class", "function", "extra"],
        name: str,
        start_line: int,
        end_line: int,
        code: str,
        path: Optional[str] = None,
    ):
        self.type = type
        self.name = name
        self.start_line = start_line
        self.end_line = end_line
        self.code = code
        self.path = path

    def __repr__(self):
        return f"{self.type.capitalize()} '{self.name}': lines {self.start_line}-{self.end_line} \ncode: \n{self.code}"


class InClassChunk(Chunk):
    def __init__(
        self,
        type: Literal["class", "function", "extra"],
        name: str,
        start_line: int,
        end_line: int,
        code: str,
        parent: str,
        path: Optional[str] = None,
    ):
        super().__init__(type, name, start_line, end_line, code, path)
        self.parent = parent


class CodeChunk(Chunk):
    def __init__(
        self,
        type: Literal["class", "function", "extra"],
        name: str,
        start_line: int,
        end_line: int,
        code: str,
        path: Optional[str] = None,
        sub_chunks: Optional[List[InClassChunk]] = None,
    ):
        super().__init__(type, name, start_line, end_line, code, path)
        self.sub_chunks: List[InClassChunk] = sub_chunks or []


def chunk_code(source_code: str, path: str = None) -> List[CodeChunk]:
    tree = ast.parse(source_code)
    lines = source_code.splitlines()
    chunks: List[CodeChunk] = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            code = get_code_segment(lines, node.lineno, node.end_lineno)
            class_chunk = CodeChunk(
                type="class",
                name=node.name,
                start_line=node.lineno,
                end_line=node.end_lineno,
                code=code,
                path=path,
                sub_chunks=secondary_chunking(node, lines, path),
            )
            chunks.append(class_chunk)
        elif isinstance(node, ast.FunctionDef):
            code = get_code_segment(lines, node.lineno, node.end_lineno)
            chunks.append(
                CodeChunk(
                    type="function",
                    name=node.name,
                    start_line=node.lineno,
                    end_line=node.end_lineno,
                    code=code,
                    path=path,
                )
            )
        else:
            code = get_code_segment(lines, node.lineno, node.end_lineno)
            chunks.append(
                CodeChunk(
                    type="extra",
                    name="extra",
                    start_line=node.lineno,
                    end_line=node.end_lineno,
                    code=code,
                    path=path,
                )
            )

    return chunks


def secondary_chunking(
    class_node: ast.ClassDef, lines: List[str], path: Optional[str] = None
) -> List[InClassChunk]:
    sub_chunks: List[InClassChunk] = []

    # 클래스 선언부와 docstring을 첫 번째 청크로 만듭니다
    class_start = class_node.lineno
    class_end = class_node.body[0].lineno - 1 if class_node.body else class_node.lineno
    class_code = get_code_segment(lines, class_start, class_end)

    # docstring이 있는지 확인합니다
    docstring = ast.get_docstring(class_node)
    if docstring:
        first_stmt = class_node.body[0]
        if isinstance(first_stmt, ast.Expr) and isinstance(first_stmt.value, ast.Str):
            class_end = first_stmt.end_lineno

    class_code = get_code_segment(lines, class_start, class_end)
    sub_chunks.append(
        InClassChunk(
            type="class",
            name=class_node.name,
            start_line=class_start,
            end_line=class_end,
            code=class_code,
            path=path,
            parent=class_node.name,
        )
    )

    # 클래스 내의 다른 요소들을 청크로 만듭니다
    for node in class_node.body:
        if isinstance(node, ast.FunctionDef):
            code = get_code_segment(lines, node.lineno, node.end_lineno)
            sub_chunks.append(
                InClassChunk(
                    type="function",
                    name=node.name,
                    start_line=node.lineno,
                    end_line=node.end_lineno,
                    code=code,
                    path=path,
                    parent=class_node.name,
                )
            )
        elif not (
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Str)
            and node.lineno == class_node.body[0].lineno
        ):
            # docstring이 아닌 경우에만 추가합니다
            code = get_code_segment(lines, node.lineno, node.end_lineno)
            sub_chunks.append(
                InClassChunk(
                    type="extra",
                    name="extra",
                    start_line=node.lineno,
                    end_line=node.end_lineno,
                    code=code,
                    path=path,
                    parent=class_node.name,
                )
            )

    return sub_chunks


def get_code_segment(lines: List[str], start: int, end: int) -> str:
    return "\n".join(lines[start - 1 : end])
