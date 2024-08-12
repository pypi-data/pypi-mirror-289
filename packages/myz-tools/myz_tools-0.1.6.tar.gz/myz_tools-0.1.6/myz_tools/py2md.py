import ast
import os


def extract_function_docs_from_file(file_path):
    """
    从 Python 文件中提取函数的 docstring（注释部分）。

    参数:
        file_path: 字符串，Python 文件的路径。

    返回:
        字典，键为函数名，值为函数的 docstring。
    """
    with open(file_path, "r", encoding="utf-8") as file:
        source = file.read()

    # 解析 Python 源代码
    tree = ast.parse(source)

    function_docs = {}

    # 遍历 AST 节点，提取函数定义和 docstring
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            docstring = ast.get_docstring(node)
            function_docs[func_name] = docstring

    return function_docs


def save_docs_to_markdown(docs, output_path):
    """
    将函数的 docstring 保存到 Markdown 文件中。

    参数:
        docs: 字典，包含函数名和 docstring 的映射。
        output_path: 字符串，Markdown 文件的保存路径。
    """
    with open(output_path, "w", encoding="utf-8") as file:
        for func_name, docstring in docs.items():
            file.write(f"### {func_name}\n\n")
            if docstring:
                file.write(f"```\n{docstring}\n```\n")
            else:
                file.write("无 docstring\n")
            file.write("\n")


def main(source_file, output_md):
    """
    主函数，用于从 Python 文件中提取 docstring 并保存为 Markdown 文件。

    参数:
        source_file: 字符串，源 Python 文件的路径。
        output_md: 字符串，输出 Markdown 文件的路径。
    """
    docs = extract_function_docs_from_file(source_file)
    save_docs_to_markdown(docs, output_md)


if __name__ == "__main__":
    # source_file_path = "common_maths.py"  # 替换为 Python 文件路径
    # output_md_path = "test_docs.md"  # 替换为输出 Markdown 文件路径
    # main(source_file_path, output_md_path)
    pass
