def evaluate_npi(expression: str):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()
            if token == "+":
                stack.append((a + b))
            elif token == "-":
                stack.append((a - b))
            elif token == "*":
                stack.append((a * b))
            elif token == "/":
                stack.append((a / b))
    return stack[0] if stack else None