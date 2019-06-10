from stack import Stack

class StringProcessor:
    def reverse(self, string):
        stack = Stack()
        for s in string:
            stack.push(s)
        res = ""
        while stack.is_empty() == False:
            res += stack.pop()
        return res
    def binary_string(self, number):
        stack = Stack()
        binary = ""
        while number != 0:
            stack.push(str(number % 2))
            number = number // 2
        while len(stack.items) != 0:
            binary += str(stack.pop())
        return binary
    def is_balanced(self, string):
        stack = Stack()
        lenstring = len(string) // 2
        if len(string) % 2 == 0:
            for i in string[:lenstring]:
                if i == "(":
                    i = ")"
                if i == "[":
                    i = "]"
                if i == "{":
                    i = "}"
                stack.push(i)
            res = ""
            while stack.is_empty() == False:
                res += stack.pop()
            print(res)
            if res == string[lenstring:]:
                return True
            return False
        return False