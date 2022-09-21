symbols = { "(": ")", "[": "]", "{": "}"}

def check_expression(expression):
    symbols_values = list(symbols.values())
    stack = []
    balanced = True
    i = 0
    while i < len(expression) and balanced:
        if expression[i] in symbols:
            stack.append(expression[i] )
        elif expression[i] in symbols_values and symbols[stack.pop()] != expression[i]:
            balanced = False
        i += 1
    return balanced

exp1 = "( 8 [ 15 + 19 {a/c^2} -x] +256)"
exp2 = "3 * ( 5 + 2) - 6"
exp3 = "2 + [ x / y ( a * c ] - 4 {-2) }"
print(check_expression(exp1))
print(check_expression(exp2))
print(check_expression(exp3))
