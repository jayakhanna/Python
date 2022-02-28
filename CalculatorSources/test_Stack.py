import unittest
import LookupError
from Stack import Stack


# Unit tests Class to test the Stack class
# all the tests are idempotent.
class TestStack(unittest.TestCase):
    testStack = Stack()

    def test_push(self):
        try:
            self.testStack.push('a')
            self.testStack.push('b')
            print('Length of stack is:' + str(self.testStack.getlength()))
        except Exception as e:
            print(e)

    def test_pop(self):
        try:
            self.testStack.push('b')
            self.assertEqual('b', self.testStack.pop())
        except Exception as e:
            print(e)

    def test_peek(self):
        try:
            self.testStack.push('b')
            self.testStack.push('a')
            self.assertEqual(self.testStack.peek(), 'a')
            self.testStack.pop()
            self.assertEqual(self.testStack.peek(), 'b')
        except Exception as e:
            print(e)

    def test_emptypop(self):
        try:
            self.testStack.stack.clear()
            fetchItem = self.testStack.pop()
            self.assertEqual(fetchItem, LookupError.CalcLookupError['EmptyStack'],
                         "Expected:" + LookupError.CalcLookupError['EmptyStack'] + " Got:" + fetchItem)
        except Exception as e:
            print(e)

