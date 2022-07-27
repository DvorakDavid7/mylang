import unittest
import src.mylang.tokenizer as tokenizer

class TokenizerTest(unittest.TestCase):

    def test_tokenize_input(self):
        source_code: str = """
            ADD 3 5
            PRINT       
        """

        tokens = tokenizer.get_tokens(source_code)
        self.assertEqual(tokens[0], "ADD")
        self.assertEqual(tokens[1], "3")
        self.assertEqual(tokens[2], "5")
        self.assertEqual(tokens[3], "PRINT")


    def test_tokenize_input_with_more_empty_lines(self):
        source_code: str = """

            ADD  3       5
        
                        PRINT       
                        
        """

        tokens = tokenizer.get_tokens(source_code)
        self.assertEqual(tokens[0], "ADD")
        self.assertEqual(tokens[1], "3")
        self.assertEqual(tokens[2], "5")
        self.assertEqual(tokens[3], "PRINT")
