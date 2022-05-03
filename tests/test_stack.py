from application.stack import Stack
import unittest


class TestStack(unittest.TestCase, Stack):
    list = []
    '''Проверка списка на пустоту'''
    def test_isEmpty(self):
        test_list = Stack
        self.assertEqual(test_list.isEmpty(self), True)  # список пустой

    def test_isEmpty_not(self):
        test_list = Stack
        test_list.push(self, 'a')  # добавляем элемент в пустой список
        self.assertEqual(test_list.isEmpty(self), False)  # список не пустой

    '''Проверка на добавление элемента в список'''
    def test_push(self):
        self.list = []
        test_list = Stack
        self.assertEqual(test_list.push(self, 'a'), None) # добавляем элемент в пустой список, ничего не возвращает.
        self.assertNotEqual(test_list.push(self, 'a'), 'a')

    '''Проверка на удаление элемента с конца'''
    def test_pop_method(self):
        self.list = []
        test_list = Stack
        test_list.push(self, 'a')
        test_list.push(self, 'b')
        self.assertEqual(test_list.pop(self), 'b') # удаляет и возвращает последний добавленный элемент


    @unittest.expectedFailure
    def test_pop_method_fail(self):
        self.list = []
        test_list = Stack
        test_list.push(self, 'a')
        test_list.push(self, 'b')
        self.assertNotEqual(test_list.pop(self), 'a')
        self.assertEqual(test_list.pop(self), 'b')  # удаляет и возвращает последний добавленный элемент

    '''Проверка на возвращение последнего элемента без удаления'''
    def test_peek(self):
        self.list = []
        test_list = Stack
        test_list.push(self, 'a')
        test_list.push(self, 'b')
        self.assertEqual(test_list.peek(self), 'b') # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        self.assertEqual(test_list.peek(self), 'b') # == b
        self.assertNotEqual(test_list.peek(self), 'a') # != a

    '''Проверка на количество элементов стека'''
    def test_size(self):
        self.list = []
        test_list = Stack
        test_list.push(self, 'a')
        self.assertEqual(test_list.size(self), 1)
        test_list.push(self, 'b')
        self.assertEqual(test_list.size(self), 2)

