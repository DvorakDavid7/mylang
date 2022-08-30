import unittest
import mylang as tokenizer
from mylang.tokenizer import get_tokens


class TokenizerTest(unittest.TestCase):

    def test_tokenize_input(self):
        source_code: str = """
            3 5 ADD
            PRINT       
        """

        tokens = get_tokens(source_code)
        self.assertEqual(tokens[0], "3")
        self.assertEqual(tokens[1], "5")
        self.assertEqual(tokens[2], "ADD")
        self.assertEqual(tokens[3], "PRINT")

    def test_tokenize_input_with_more_empty_lines(self):
        source_code: str = """
        
            3       5  ADD
        
                        PRINT       
                        
        """

        tokens = get_tokens(source_code)
        self.assertEqual(tokens[0], "3")
        self.assertEqual(tokens[1], "5")
        self.assertEqual(tokens[2], "ADD")
        self.assertEqual(tokens[3], "PRINT")
