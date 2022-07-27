import unittest

from src.mylang.stack import Stack


class StackTest(unittest.TestCase):
    
    def test_top(self):
        """
        top of empyt stack
        """
        
        stack: Stack = Stack()
        res = stack.top()

        self.assertTrue(stack.is_empty())
        self.assertEqual(res, "")


    def test_push(self):
        """
        push value to empty stack
        """
        
        stack: Stack = Stack()

        stack.push("a")
        res = stack.top()

        self.assertEqual(res, "a")
        self.assertFalse(stack.is_empty())

    def test_pop(self):
        """
        pop value
        """
        
        stack: Stack = Stack()

        stack.push("a")
        poped_value = stack.pop()
        res = stack.top()

        self.assertEqual(poped_value, "a")
        self.assertEqual(res, "")


    def test_pop(self):
        """
        pop from empy stack
        """
        
        stack: Stack = Stack()

        poped_value = stack.pop()
        res = stack.top()

        self.assertEqual(poped_value, "")
        self.assertEqual(res, "")
