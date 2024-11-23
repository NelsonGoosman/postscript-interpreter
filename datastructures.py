import math
scope = "Dynamic"



class StackUnderflowError(Exception):
    def __init__(self, message="Pop operation attempted on an empty stack"):
        self.message = message
        super().__init__(self.message)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            raise StackUnderflowError()

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            raise StackUnderflowError()

    def __str__(self):
        return " ".join(str(x) for x in self.stack)

    def exch(self):
        if len(self.stack) >= 2:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        else:
            None

    def copy(self, n):
        if n <= len(self.stack):
            self.stack.extend(self.stack[-n:])
        else:
            None

    def dup(self):
        if len(self.stack) > 0:
            self.stack.append(self.stack[-1])

    def clear(self):
        self.stack = []

    def count(self):
        self.stack.append(len(self.stack))

    def getstack(self):
        return self.stack


class Dictionary:
    def __init__(self, max_size=math.inf):
        self.max_size = max_size
        self.dict = {}
        self.size = 0

    def add(self, key, value):
        if self.size < self.max_size:
            self.dict[key] = value
            self.size += 1
        else:
            print("Dictionary is full")

    def get(self, key):
        return self.dict[key]

    def __iter__(self):
        return iter(self.dict)

    def __str__(self):
        return str(self.dict)


class Procedure:
    def __init__(self, code_block=[], scope="Dynamic"):
        self.code_block = code_block
        self.scope = scope

    def execute(self, process_fn):
        if self.scope == "Static":  # Use scope through dictionary_stack
            dictionary_stack.push(Dictionary())
        for token in self.code_block:
            if isinstance(token, Procedure):  # TODO: fix unintened behavior. Nested procedures are executed right away even if they are not defined by a constant
                operand_stack.push(token)
            else:
                process_fn(token)
        if self.scope == "Static":  # Use scope through dictionary_stack
            dictionary_stack.pop()

    def __str__(self):
        return "(" + " ".join(self.code_block) + ")"

    def add(self, token):
        self.code_block.append(token)


operand_stack = Stack()
dictionary_stack = Stack()
dictionary_stack.push(Dictionary())