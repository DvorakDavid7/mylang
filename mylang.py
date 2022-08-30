#!/usr/bin/env python3

import sys
from typing import List

from mylang.ExecutionException import ExecutionException
from mylang.runner import run_program
from mylang.stack import Stack
from mylang.tokenizer import get_tokens


def main():
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if ".dd" in arg:
            program = _load_program_from_file(arg)
        elif arg == "-r" or arg == "--repl":
            _run_repl_mode()
            return
        else:
            program = _load_program_from_arg(arg)
    else:
        _help()
        return

    try:
        memory: Stack = Stack()
        run_program(program, memory)
    except ExecutionException as e:
        print(e)


def _help():
    h = """usage:
Execute instructions
    python3 mylang.py [filename].dd
or
    python3 mylang.py "[program]"

run REPL mode
    python3 mylang.py -r
    """
    print(h)


def _load_program_from_file(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        source_code = f.read()
        return get_tokens(source_code)


def _load_program_from_arg(arg) -> List[str]:
    return get_tokens(arg)


def _run_repl_mode():
    memory: Stack = Stack()

    while True:
        instruction = input(">>> ")

        if instruction == "mem":
            print(memory)
            continue

        if instruction == "clr":
            while not memory.is_empty():
                memory.pop()
            continue

        if instruction == "exit":
            break

        try:
            run_program(get_tokens(instruction), memory)
        except ExecutionException as e:
            print(e)


if __name__ == "__main__":
    main()
