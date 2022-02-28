# Operator Precedence.
import math
import operator
import LookupError

# Operator precedence stored in dictionary
# Operator is the key
# Value is an integer. Higher the number; higher the precedence
OpPrecedence = {
    "+" : 1,
    "-" : 1,
    "*" : 2,
    "/" : 2,
    "%" : 2,
    "^" : 11,
    "(" : 12,
    ")" : 12
}

# Function that runs true if the precedence of op2 is higher or equal to op1
# op2: operator to check for precedence
# op1: operator to check against for precdence
# returns True if op2 has higher or equal precedence compared to op1
# return False if op2 doesn't have higher or equal precedence to op1
def opPrecedenceHigherOrEqual(op2, op1):
    if op2 not in OpPrecedence.keys():
        errStr = str.format(LookupError.CalcLookupError['UnsupportedOperator'], format(op1))
        raise Exception(errStr)

    if op1 not in OpPrecedence.keys():
        errStr = str.format(LookupError.CalcLookupError['UnsupportedOperator'], format(op1))
        raise Exception(errStr)

    if OpPrecedence.get(op2) >= OpPrecedence.get(op1):
        return True
    else:
        return False

# Performs mathematical operation based on the operator passed.
# Params:
#   c1: First operand
#   c2: Second operand. Can be empty if the operation is unary.
#   op: Operator that determines what operation to perform.
# Returns the result of the mathematical operation.
def doOperation (c1, op, c2 = None):
    if op == '!':
        return math.factorial(int(c1))
    if op == '+':
        return operator.add(float(c1), float(c2))
    elif op == '-':
        return operator.sub(float(c1), float(c2))
    elif op == '%':
        return operator.mod(float(c1), float(c2))
    elif op == '*':
        return operator.mul(float(c1), float(c2))
    elif op == '/':
        return operator.truediv(float(c1), float(c2))
    elif op == '^':
        return operator.pow(float(c1), float(c2))
    else:
        errStr = str.format(LookupError.CalcLookupError['UnsupportedOperator'], format(op1))
        raise Exception(errStr)


