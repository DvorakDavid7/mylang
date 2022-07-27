import unittest
import src.mylang.runner as code_runner
from src.mylang.stack import Stack

class InstructionRunnerTest(unittest.TestCase):

    @unittest.SkipTest
    def test_run_instruction(self):
        instructions = [
            "ADD"
            "3"
            "5"
        ]
        
        stack: Stack = code_runner.execute_instructions(instructions)

        self.assertSetEqual(stack.top(), "8")
