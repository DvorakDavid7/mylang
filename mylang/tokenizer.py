from typing import List


def get_tokens(source_code: str) -> List[str]:
    """
    parse given source code to tokens
    :param source_code:
    :return: list of tokens
    """
    tokens: List[str] = []

    striped_lines = _strip_source(source_code)

    for command in striped_lines:
        operation = command.split()
        for token in operation:
            tokens.append(token)

    return tokens


def _strip_source(source_code: str) -> List[str]:
    striped_lines: List[str] = []
    lines = source_code.split("\n")

    for line in lines:
        word: str = line.strip()
        if word != "":
            striped_lines.append(line.strip())

    return striped_lines
