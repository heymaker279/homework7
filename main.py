from typing import List
from application.stack_balanced_sequence import is_balanced_sequence


'''решение задачи №2'''
if __name__ == "__main__":
    example = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
    for item in example:
        print(is_balanced_sequence(item))


'''Решение к 1 задаче из лекции (LeetCode)'''
nums = [2, 7, 3, 6, 9, 41]
target = 9


def twoSum(nums: List[int], target: int) -> List[int]:
    for index, value in enumerate(nums):
        for index2, value2 in enumerate(nums):
            if value2 + value == target and index != index2:
                return [index, index2]


print(twoSum(nums, target))


# '''Вариант решения перподавателя'''
# def twoSum(nums: List[int], target: int) -> List[int]:
#     data = {}
#     for index, value in enumerate(nums):
#         if value in data:
#             return [data[value], index]
#         data[target - value] = index