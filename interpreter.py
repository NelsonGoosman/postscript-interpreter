from operations import keywords
from datastructures import *
import sys


def process_boolean(value: str):
    # (parse status, bool value)
    if value == "true":
        return (True, True)
    elif value == "false":
        return (True, False)
    else:
        return False


def process_number(value: str):
    # check if value is a float and return it
    try:
        float_value = float(value)
        if float_value.is_integer():
            return (True, int(float_value))
        else:
            return (True, float_value)
    except ValueError:
        return False


def process_code_block(value: str):
    if len(value) >= 2 and value.startswith("{") and value.endswith("}"):
        return (True, value[1:-1].strip().split())


def process_name_constant(value: str):
    # check if value is a name constant (variable) and return it
    if value.startswith("/"):
        return (True, value)


def process_string(value: str):
    # check if value is a string and return it
    if value.startswith("(") and value.endswith(")"):
        return (True, value[1:-1])


def process_constants(input):
    if isinstance(input, Procedure):
        return None
    res = process_boolean(input)
    res = res or process_number(input)
    res = res or process_code_block(input)
    res = res or process_name_constant(input)
    res = res or process_string(input)
    return res


def process_input(input):
    result = process_constants(input)
    if result:
        # push to operand stack if value is a constant, string, name contant, or code block
        operand_stack.push(result[1]) 
    elif input in keywords: 
        # if its a keyword, execute it 
        keywords[input]()
    else:
        # if its a name, look it up in the dictionry and push value to operand stack
        lookup_in_dictionary(input) 


def lookup_in_dictionary(input):

    def execute_value(value):
        if input in keywords:
            keywords[input]()
        elif isinstance(value, Procedure):
            value.execute(process_input)
        else:
            operand_stack.push(value)

    if scope == "Dynamic":
        top_dict = dictionary_stack.peek()
        try:
            value = top_dict.get(input)
            execute_value(value)
        except KeyError:
            print(f"{input} not in dictionary")
    else:
        # static scoping
        for dictionary in reversed(dictionary_stack.stack):
            try:
                value = dictionary.get(input)
                execute_value(value)
                break
            except KeyError:
                continue
        else:
            print(f"Variable {input} not in scope")


def repl():
    code_block = False  # keeps track of whether we are in a code block
    nested_procedure_count = 0  # keeps track of nested procedures
    while True:
        user_input = input(
            "REPL> " if not code_block else (3 * nested_procedure_count * " ") + "... "
        )
        if user_input.lower() == "quit":
            print("Exiting REPL")
            break
        tokens = user_input.strip().split()
        for token in tokens:
            if not code_block and token in keywords:
                keywords[token]()

            elif token == "{":
                # procedure starts in the form { ...
                code_block = True
                nested_procedure_count += 1
                operand_stack.push(Procedure([], scope))

            elif token.startswith("{"):
                if token.endswith("}"):
                    operand_stack.push(Procedure(token[1:-1].strip().split(), scope))
                else:
                    code_block = True
                    nested_procedure_count += 1
                    operand_stack.push(Procedure(token[1:], scope))

            elif token == "}":
                # procedure ends in the form ... }
                if nested_procedure_count == 1:
                    code_block = False
                else:
                    nested_procedure = operand_stack.pop()
                    operand_stack.peek().add(nested_procedure)

                nested_procedure_count -= 1

            elif token.endswith("}"):
                # procedure ends in the form ...}
                token = token[:-1]
                operand_stack.peek().add(token)

                if nested_procedure_count == 1:
                    code_block = False
                else:
                    nested_procedure = operand_stack.pop()
                    print (nested_procedure)
                    operand_stack.peek().add(nested_procedure)

                nested_procedure_count -= 1

            elif code_block:
                operand_stack.peek().add(token)

            else:
                process_input(token)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "static":
            scope = "Static"
            print("Scope set to static")
        elif sys.argv[1].lower() == "dynamic":
            scope = "Dynamic"
            print("Scope set to dynamic")
        else:
            print("Invalid argument. Use 'static' or 'dynamic'.")
            sys.exit(1)
    else:
        print("No scoping argument provided. Defaulting to 'Dynamic'.")
        scope = "Dynamic"
    repl()
