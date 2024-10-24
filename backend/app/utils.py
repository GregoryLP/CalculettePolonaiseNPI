def evaluate_npi(expression: str):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
        elif token in ('+', '-', '*', '/'):
            if len(stack) < 2:
                raise ValueError("Not enough values in stack for operation")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
        else:
            raise ValueError(f"Invalid token: {token}")

    if len(stack) != 1:
        raise ValueError("The user input has too many values or not enough values to produce a single result.")

    return stack[0]
