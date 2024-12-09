import re
import Node
from Token import Token
from Datatypes import Stack

general_token_pattern = r"\d+\.\d+|\d+|[()+\-*\/~^]|[a-zA-Z_][a-zA-Z0-9_]*"
operators = set("+-*/^~")
precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "~": 3}

def is_operator(token: Token) -> bool:
    return token.value in operators

def is_operand(token: Token) -> bool:
    return not is_operator(token) and token.value not in ("(", ")")

def build_ast(tokens: list[Token]) -> Node:
    operator_stack = Stack[Token]()
    node_stack = Stack[Node]()
    for token in tokens:
        if is_operand(token):
            node_stack.push(Node(value=token.value))

def tokenize(full_input: str) -> list[Token]:
    tokens = re.findall(general_token_pattern, full_input)
    return_tokens = []
    for tokenizing_token in tokens:
        tokenizing_token = Token(None, tokenizing_token)
        match tokenizing_token.check_value_type():
            case "int":
                tokenizing_token.value_to_int()
            case "float":
                tokenizing_token.value_to_float()
            case "str":
                pass
        return_tokens.append(tokenizing_token)
    return return_tokens


if __name__ == "__main__":
    while True:
        user_input: str = input(">>> ")
        tokenized_input: list[Token] = tokenize(user_input)

        if not tokenized_input:
            print("You need to give a valid input.")
            continue
        elif not tokenized_input[0].value.isnumeric() and tokenized_input[0].value.strip().lower() == "exit":
            print("Goodbye")
            break

        else:
            pass