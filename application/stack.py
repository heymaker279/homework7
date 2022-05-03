'''Решение задачи №1'''


class Stack:
    def __init__(self) -> None:
        self.list = list()

    def isEmpty(self) -> bool:  # проверка стека на пустоту. Метод возвращает True или False.
        return len(self.list) == 0

    def push(self, item) -> None:  # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        self.list.append(item)

    def pop(self):  # удаляет верхний элемент из стека. Стек изменяется. Метод возвращает верхний элемент стека.
        popped_item = self.list.pop()
        return popped_item

    def peek(self):  # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        if len(self.list) == 0:
            pass
        else:
            return self.list[-1]

    def size(self):  # возвращает количество элементов в стеке.
        return len(self.list)
