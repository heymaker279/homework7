from application.stack import Stack

def is_balanced_sequence(item):
        stack = Stack()
        is_good = True
        for element in item:
            if element in '({[':
                stack.push(element)
            elif element in ')}]':
                if stack.isEmpty() is True:
                    is_good = False
                    break
                open_bracket = stack.pop()
                if open_bracket == '(' and element == ')':
                    continue
                if open_bracket == '[' and element == ']':
                    continue
                if open_bracket == '{' and element == '}':
                    continue
                is_good = False
                break
        if is_good and stack.isEmpty():
            return "Сбалансированная последовательность"
        else:
            return "Несбалансированная последовательность"

