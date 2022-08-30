from typing import List

from mylang.ExecutionException import ExecutionException
from mylang.stack import Stack


def run_program(instructions: List[str], memory: Stack) -> Stack:
    """
    run given list of instruction
    if any error happen ExecutionException is raised

    :param instructions: program
    :param memory: memory which will be used
    :return: memory after program execution
    """

    for instruction in instructions:
        _execute_instruction(instruction, memory)
    return memory


def _execute_instruction(instruction: str, memory: Stack):
    if instruction == "ADD":
        _op_add(memory)
    elif instruction == "SUB":
        _op_sub(memory)
    elif instruction == "DIV":
        _op_div(memory)
    elif instruction == "MUL":
        _op_mul(memory)
    elif instruction == "PRINT":
        _op_print(memory)
    elif _is_numeric_value(instruction):
        memory.push(instruction)
    else:
        raise ExecutionException(f"invalid operation: '{instruction}'")


def _op_add(memory: Stack):
    result = 0
    while not memory.is_empty():
        result += float(memory.pop())
    memory.push(_format_float_value(result))


def _op_sub(memory: Stack):
    args = _get_operation_args(memory)
    result = None
    for arg in args:
        if result is None:
            result = arg
        else:
            result -= arg
    memory.push(_format_float_value(result))


def _op_div(memory: Stack):
    args = _get_operation_args(memory)
    result = None
    for arg in args:
        if result is None:
            result = arg
        else:
            if arg == 0:
                raise ExecutionException("division by zero")
            else:
                result /= arg
    memory.push(_format_float_value(result))


def _op_mul(memory: Stack):
    result = 1
    while not memory.is_empty():
        result *= float(memory.pop())
    memory.push(_format_float_value(result))


def _op_print(memory: Stack):
    print(memory.top())


def _get_operation_args(memory: Stack) -> List[float]:
    args: List[float] = []
    while not memory.is_empty():
        args.append(float(memory.pop()))
    args.reverse()
    return args


def _format_float_value(value: float) -> str:
    if value % 1 == 0:
        return str(int(value))
    else:
        return str(value)


def _is_numeric_value(instruction):
    return instruction.isnumeric() or instruction.replace(".", "", 1).isdigit() and instruction.count(".") < 2
