def precedence(c):  # set precedence of our operator
    if c in "*/":
        return 2
    elif c in "+-":
        return 1
    else:
        return 0


def isOperator(c):  # determines whether or not input is an operator
    if c in "+-*/()":
        return c != ""
    else:
        return True


def isNumber(c):    # determines whether or not input is a number (or decimal point)
    if c in "1234567890.":
        return c != ""
    else:
        return False


def dothemath(op, a, b):    # does math! yay
    if op == '+':
        return float(a) + float(b)
    elif op == '-':
        return float(a) - float(b)
    elif op == '*':
        return float(a) * float(b)
    elif op == '/':
        return float(a) / float(b)
    else:
        return 0


def eval_infix(s):
    expression = list(s)    # brings expression given into function
    OperatorStack = []      # creates stacks for the operators and operands
    OperandStack = []
    num = ''                # stores multi-digit numbers

    while len(expression) > 0:
        c = expression.pop(0)   # pull first character out of our expression
        while c == ' ':
            c = expression.pop(0)   # if the character is empty, skip it
        if len(expression) > 0:
            d = expression[0]   # stores the next character, for comparison purposes later
        else:
            d = ''

        if isNumber(c):
            num += c
            if not isNumber(d):
                OperandStack.append(num)    # once we get through a number (no matter how many digits),
                num = ''                    # put it on the stack and clear out the num variable.

        elif c == "(":
            OperatorStack.append(c)         # if the operator is a front paren, append it automatically
        elif c == ")":
            while len(OperatorStack) > 0:   # if it's a back paren:
                c = OperatorStack.pop()     # grab the next character
                if c == "(":                # if it's a front paren, STOP :)
                    break
                elif isOperator(c):         # if it's an operator,
                    b = OperandStack.pop()
                    a = OperandStack.pop()
                    OperandStack.append(dothemath(c, a, b)) # do math on the last two numbers on our num stack

        elif isOperator(c):     # if our character is an operator
            while True:         # loop!
                if len(OperatorStack) > 0:  # get top value from operator stack
                    top = OperatorStack[-1]
                else:
                    top = ''

                if isOperator(top):     # if the top value exists, essentially:
                    if not precedence(c) > precedence(top):     # if it's a lower precedence than what's next (on top),
                        lastop = OperatorStack.pop()        # Do the math!
                        b = OperandStack.pop()
                        a = OperandStack.pop()
                        OperandStack.append(dothemath(lastop, a, b))
                    else:
                        OperatorStack.append(c)         # otherwise, just stick that on the stack, for later! wooooo
                        break
                else:
                    OperatorStack.append(c)             # if the top value ain't there, just stick it on that stack baby
                    break

    while len(OperatorStack) > 0:   # once we're done importing the expression, but there's still s**t to do,
        c = OperatorStack.pop()     # grab that operator
        if c == "(":                # if it's a back paren we done baby
            break
        elif isOperator(c):         # otherwise,
            b = OperandStack.pop()
            a = OperandStack.pop()
            OperandStack.append(dothemath(c, a, b))     # DO THE LAST MATH! :D :D :D

    return OperandStack.pop()       # Return our final number. And we're done!


def main():
    expr = input("Enter expression: ")
    pythons = eval(expr)
    mine = eval_infix(expr)
    print(mine, pythons)


if __name__ == '__main__':
    main()
