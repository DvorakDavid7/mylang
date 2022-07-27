

from typing import List

from src.mylang.stack import Stack


args: List[str] = []


def run_program(memory: Stack):
    while not memory.is_empty():
        op_code = memory.pop()
        execute_instruction(op_code, memory)
    return memory


def execute_instruction(op_code: str, memory: Stack):
    if op_code == "ADD":
        op_add(memory)

    elif op_code == "SUB":
        op_sub(memory)

    elif op_code == "PRINT":
        op_print(memory)

    else:
        args.append(op_code)


def op_add(memory: Stack):
    s = 0
    for a in args:
        s += int(a)
    memory.push(str(s))


def op_sub(memory: Stack):
    operand1 = int(args[-1])
    operand2 = int(args[-2])
    memory.push(str(operand1 - operand2))


def op_print(memory: Stack):
    print(args[-1])
