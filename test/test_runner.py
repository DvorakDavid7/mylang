import unittest
import src.mylang.runner as code_runner
from src.mylang.stack import Stack


class InstructionRunnerTest(unittest.TestCase):
    def test_run_program(self):
        instructions = [
            "PRINT",
            "SUB",
            "8",
            "3",

            "PRINT",
            "ADD",
            "8",
            "3",
        ]
        mem = Stack()

        for i in instructions:
            mem.push(i)

        stack: Stack = code_runner.run_program(mem)
