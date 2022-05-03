from application.stack import Stack
from application.stack_balanced_sequence import is_balanced_sequence
import unittest


class TestBalancedSequence(unittest.TestCase):
    '''Тест на сбалансированность скобок'''
    def test_stack_balanced_sequence(self):
        self.assertEqual(is_balanced_sequence('(())'), 'Сбалансированная последовательность')
        self.assertEqual(is_balanced_sequence('(()'), 'Несбалансированная последовательность')
        self.assertEqual(is_balanced_sequence('(5(10 + 2)'), 'Несбалансированная последовательность')
        self.assertEqual(is_balanced_sequence('{[]}5([{(10 + 2)}])'), 'Сбалансированная последовательность')