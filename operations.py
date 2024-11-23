from math import ceil, sqrt
from datastructures import *


####  Stack operations wrappers  ####
def peek_op():
    operand_stack.push(operand_stack.peek())


def pop_op():
    operand_stack.pop()


def exch_op():
    operand_stack.exch()


def copy_op():
    operand_stack.copy(operand_stack.pop())


def dup_op():
    operand_stack.dup()


def clear_op():
    operand_stack.clear()


def count_op():
    operand_stack.count()


####  Arithmetic operations  ####


def add_op():
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        operand_stack.push(num1 + num2)
    else:
        None


def sub_op():
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        operand_stack.push(num1 - num2)
    else:
        None


def mul_op():
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        operand_stack.push(num1 * num2)
    else:
        None


def div_op():
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        operand_stack.push(num1 / num2)
    else:
        None


def idiv_op():  # integer division
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        operand_stack.push(num1 // num2)
    else:
        None


def mod_op():
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        operand_stack.push(num1 % num2)
    else:
        None


def abs_op():
    if len(operand_stack.stack) >= 1:
        num = operand_stack.pop()
        operand_stack.push(abs(num))
    else:
        None


def neg_op():
    if len(operand_stack.stack) >= 1:
        num = operand_stack.pop()
        operand_stack.push(-num)
    else:
        None


def ceiling_op():
    if len(operand_stack.stack) >= 1:
        num = operand_stack.pop()
        operand_stack.push(ceil(num))
    else:
        None


def floor_op():
    if len(operand_stack.stack) >= 1:
        num = operand_stack.pop()
        operand_stack.push(int(num))
    else:
        None


def round_op():
    if len(operand_stack.stack) >= 1:
        num = operand_stack.pop()
        operand_stack.push(round(num))
    else:
        None


def sqrt_op():
    if len(operand_stack.stack) >= 1:
        num = operand_stack.pop()
        operand_stack.push(sqrt(num))
    else:
        None


####  Dictionary operations  ####


def dict_op():
    # int dict: creates a new dictionary with the given capacity
    size = operand_stack.pop()
    new_dict = Dictionary(size)
    operand_stack.push(new_dict)


def dictlength_op():
    # dict length: returns the number of key-value pairs in the dictionary
    if len(dictionary_stack.stack) >= 1:
        dictionary = dictionary_stack.peek()
        operand_stack.push(dictionary.size)
    else:
        None


def maxlength_op():
    # dict maxlength: returns the maximum number of key-value pairs that the dictionary can hold
    if len(dictionary_stack.stack) >= 1:
        dictionary = dictionary_stack.peek()
        operand_stack.push(dictionary.max_size)
    else:
        None


def begin_op():
    # dict begin: starts a new dictionary
    dictionary = operand_stack.pop()
    dictionary_stack.push(dictionary)


def end_op():
    # dict end: ends the current dictionary
    dictionary_stack.pop()


def def_op():
    # key value dict def: adds a key-value pair to the dictionary
    value = operand_stack.pop()
    key = operand_stack.pop()[1:]  # Remove the leading '/'
    dictionary = dictionary_stack.peek()
    dictionary.add(key, value)


####  Bit and boolean operations  ####
def eq_op():
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        operand_stack.push(num1 == num2)
    else:
        None


def ne_op():
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()

        operand_stack.push(num1 != num2)
    else:
        None


def ge_op():
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        operand_stack.push(num1 >= num2)
    else:
        None


def gt_op():
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        operand_stack.push(num1 > num2)
    else:
        None


def le_op():
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        operand_stack.push(num1 <= num2)
    else:
        None  # TODO: what do i do here? Throw error?


def lt_op():
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        operand_stack.push(num1 < num2)
    else:
        None


def and_op():
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        if isinstance(num1, bool) and isinstance(num2, bool):
            operand_stack.push(num1 and num2)
        elif isinstance(num1, int) and isinstance(num2, int):
            operand_stack.push(num1 & num2)
        else:
            raise TypeError("Operands must be both booleans or both integers")
    else:
        None


def not_op():
    if len(operand_stack.stack) >= 1:
        num = operand_stack.pop()
        if isinstance(num, bool):
            operand_stack.push(not num)
        elif isinstance(num, int):
            operand_stack.push(~num)
        else:
            raise TypeError("Operand must be a boolean or an integer")
    else:
        None


def or_op():
    if len(operand_stack.stack) >= 2:
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        if isinstance(num1, bool) and isinstance(num2, bool):
            operand_stack.push(num1 or num2)
        elif isinstance(num1, int) and isinstance(num2, int):
            operand_stack.push(num1 | num2)
        else:
            raise TypeError("Operands must be both booleans or both integers")
    else:
        None


def true_op():
    operand_stack.push(True)


def false_op():
    operand_stack.push(False)


## flow control operations ##
def if_op():
    # bool { operation } if
    operation = operand_stack.pop()
    bool_value = operand_stack.pop()
    if bool_value:
        operation.execute(_process_input)


def ifelse_op():
    # bool { operation } { operation } ifelse
    else_op = operand_stack.pop()
    if_op = operand_stack.pop()
    bool_value = operand_stack.pop()
    if bool_value:
        if_op.execute(_process_input)
    else:
        else_op.execute(_process_input)


def for_op():
    # start step end { operation } for
    operation = operand_stack.pop()
    end = operand_stack.pop()
    step = operand_stack.pop()
    start = operand_stack.pop()
    for i in range(start, end, step):
        operation.execute(_process_input)


def repeat_op():
    # n { operation } repeat
    operation = operand_stack.pop()
    n = operand_stack.pop()
    for i in range(n):
        operation.execute(_process_input)


### String operations ###
def strlen_op():
    # str length
    operand_stack.push(len(operand_stack.peek()))


def getidx_op():
    # str idx get
    if len(operand_stack.stack) >= 2:
        index = operand_stack.pop()
        string = operand_stack.pop()
        operand_stack.push(string)
        operand_stack.push(index)
        operand_stack.push(string[index])
    else:
        None


def getinterval_op():
    # str start end getinterval
    if len(operand_stack.stack) >= 3:
        end = operand_stack.pop()
        start = operand_stack.pop()
        string = operand_stack.pop()
        operand_stack.push(string[start:end])
    else:
        None


def putinterval_op():
    # string1 index string2 putinterval
    # replaces string1[index] ... by string2
    if len(operand_stack.stack) >= 3:
        string2 = operand_stack.pop()
        index = operand_stack.pop()
        string1 = operand_stack.pop()
        new_string = string1[:index] + string2 + string1[index:]
        operand_stack.push(new_string)
    else:
        None


## procedure operations ##
def exec_op():
    # proc exec
    proc = operand_stack.pop()
    proc.execute(_process_input)


## io operations ##
def print_op():
    print(operand_stack.peek())


def pstack():
    stack = operand_stack.getstack()
    for item in stack[::-1]:
        print(item)


## misc operations ##
def quit_op():
    pass


keywords = {
    "peek": peek_op,
    "pop": pop_op,
    "exch": exch_op,
    "copy": copy_op,
    "dup": dup_op,
    "clear": clear_op,
    "count": count_op,
    "add": add_op,
    "div": div_op,
    "sub": sub_op,
    "idiv": idiv_op,
    "mul": mul_op,
    "mod": mod_op,
    "abs": abs_op,
    "neg": neg_op,
    "ceiling": ceiling_op,
    "floor": floor_op,
    "round": round_op,
    "sqrt": sqrt_op,
    "dict": dict_op,
    "length": dictlength_op,
    "maxlength": maxlength_op,
    "begin": begin_op,
    "end": end_op,
    "def": def_op,
    "strlen": strlen_op,
    "get": getidx_op,
    "getinterval": getinterval_op,
    "putinterval": putinterval_op,
    "eq": eq_op,
    "ne": ne_op,
    "ge": ge_op,
    "gt": gt_op,
    "le": le_op,
    "lt": lt_op,
    "and": and_op,
    "not": not_op,
    "or": or_op,
    "true": true_op,
    "false": false_op,
    "if": if_op,
    "ifelse": ifelse_op,
    "for": for_op,
    "repeat": repeat_op,
    "quit": quit_op,
    "print": pstack,
    "exec": exec_op,
}


# FIXME: hacky workarounds for circular imports
def _process_boolean(value: str):
    # (parse status, bool value)
    if value == "true":
        return (True, True)
    elif value == "false":
        return (True, False)
    else:
        return False


def _process_number(value: str):
    # check if value is a float and return it
    try:
        float_value = float(value)
        if float_value.is_integer():
            return (True, int(float_value))
        else:
            return (True, float_value)
    except ValueError:
        return False


def _process_code_block(value: str):
    # check if value is a code block and return it
    if len(value) >= 2 and value.startswith("{") and value.endswith("}"):
        return (True, value[1:-1].strip().split())


def _process_name_constant(value: str):
    # check if value is a name constant (variable) and return it
    if value.startswith("/"):
        return (True, value)


def _process_string(value: str):
    # check if value is a string and return it
    if value.startswith("(") and value.endswith(")"):
        return (True, value[1:-1])


def _process_constants(input):
    # determines if the input is a constant or not
    res = _process_boolean(input)
    res = res or _process_number(input)
    res = res or _process_code_block(input)
    res = res or _process_name_constant(input)
    res = res or _process_string(input)
    return res


def _process_input(input):
    result = _process_constants(input)
    if result:
        # push to operand stack if value is a constant, string, name contant, or code block
        operand_stack.push(result[1]) 
    elif input in keywords: 
        # if its a keyword, execute it 
        keywords[input]()
    else:
        # if its a name, look it up in the dictionry and push value to operand stack
        _lookup_in_dictionary(input) 



def _lookup_in_dictionary(input):

    def execute_value(value):
        if value in keywords:
            keywords[value]()
        elif isinstance(value, Procedure):
            value.execute(_process_input)
        else:
            operand_stack.push(value)

    if scope == "Dynamic":
        top_dict = dictionary_stack.peek()
        try:
            value = top_dict.get(input)
            execute_value(value)
        except KeyError:
            print(f"Variable {input} not in scope")
    else:
        # static scoping
        found = False
        for dictionary in reversed(dictionary_stack.stack):
            try:
                value = dictionary.get(input)
                execute_value(value)
                found = True
                break
            except KeyError:
                continue
        if not found:
            print(f"Variable {input} not in scope")
