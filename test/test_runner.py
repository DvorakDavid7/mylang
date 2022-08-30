import unittest

from mylang.ExecutionException import ExecutionException
from mylang.runner import run_program
from mylang.stack import Stack


class InstructionRunnerTest(unittest.TestCase):

    def test_run_program_print(self):
        """
        should print the number on the top of the stack
        """
        instructions = [
            "3",
            "PRINT",
        ]
        init_memory: Stack = Stack()
        result_memory = run_program(instructions, init_memory)

        self.assertEqual(result_memory.top(), "3")

    def test_run_program_add_floats(self):
        """
        adds two or more floats 5.3 + 3.2
        """

        instructions = [
            "5.3",
            "3.2",
            "ADD",
        ]
        init_memory: Stack = Stack()
        result_memory = run_program(instructions, init_memory)

        self.assertEqual(result_memory.top(), "8.5")

    def test_run_program_sub(self):
        """
        subtract two or more numbers 5 - 3 - 4
        """

        instructions = [
            "5",
            "3",
            "4",
            "SUB",
        ]
        init_memory: Stack = Stack()
        result_memory = run_program(instructions, init_memory)

        self.assertEqual(result_memory.top(), "-2")

    def test_run_program_mul(self):
        """
        multiply two or more numbers 5 * 3 * 2
        """

        instructions = [
            "5",
            "3",
            "2",
            "MUL",
        ]
        init_memory: Stack = Stack()
        result_memory = run_program(instructions, init_memory)

        self.assertEqual(result_memory.top(), "30")

    def test_run_program_div(self):
        """
        divide two or more numbers 10 / 5 / 2
        """

        instructions = [
            "12",
            "4",
            "5",
            "DIV",
        ]
        init_memory: Stack = Stack()
        result_memory = run_program(instructions, init_memory)

        self.assertEqual(result_memory.top(), "0.6")

    def test_run_program_div_by_zero(self):
        """
        should raise an exception when dividing by zero
        """

        instructions = [
            "5",
            "0",
            "DIV",
        ]
        init_memory: Stack = Stack()

        with self.assertRaises(ExecutionException):
            _ = run_program(instructions, init_memory)

    def test_run_program_invalid_operation(self):
        """
        should raise an exception when executing invalid operation
        """

        instructions = [
            "1",
            "5",
            "INVALID",
        ]
        init_memory: Stack = Stack()

        with self.assertRaises(ExecutionException):
            _ = run_program(instructions, init_memory)
