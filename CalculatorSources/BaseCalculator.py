import Operator
import re
from Stack import Stack


# Class for the calculator functionality.
class BaseCalculator:
    # Function that strips spaces from the string passed as parameter.
    # param: str is the input string.
    # returns string:str with stripped spaces
    def stripSpaces(self, str):
        pattern = re.compile(r'\s+')
        inputStr = re.sub(pattern, '', str)
        return inputStr

    # Function that tokenizes the expression into operators and operands
    # param: str is the input string
    # returns a list that contains the numbers and operators in the string:str
    def exprTokenize(self, str):
        tokenStr = []
        inputStr = self.stripSpaces(str)
        # Regular expression to find the match of numbers and operators
        tempStr = re.finditer(r'\-+[0-9]+|([*+\/\-)(])|([0-9.]+|.)', inputStr)
        for str in tempStr:
            start = str.start()
            end = str.end()
            tokenStr.append(inputStr[start:end])
        return tokenStr

    # Function to find out whether the given string parameter represents float
    # param: number as string.
    # returns True if the number represents float else False
    def isfloat(self, number):
        try:
            float(number)
        except ValueError:
            return False
        return True

    # Function that takes the expression and evaluates the return the result.
    # Param: string parameter str that has the mathematical expression.
    # Return: string value that has the evaulated result of the mathematical expression.
    def evaluate(self, str):
        calcStack = Stack()
        operand = []
        #input = list(self.stripSpaces(str)) #single digit works fine
        #input = str.split()
        input = list(self.exprTokenize(str))
        for c in input:
            if c.isdigit():
                operand.append(c)
            elif self.isfloat(c):
                operand.append(c)
            elif c == '(':
                calcStack.push(c)
            elif c == '!': #factorial operator
                c3 = Operator.doOperation(operand.pop(), c)
                operand.append(c3)
                operand.append(c3)
            elif c == ')':
                if calcStack.peek() == '(': # that means (-number)
                    calcStack.pop()
                    continue
                while (calcStack.isEmpty() is False) and calcStack.peek() != '(':
                    c2 = operand.pop()
                    c1 = operand.pop()
                    op = calcStack.pop()
                    c3 = Operator.doOperation(c1, op, c2)
                    operand.append(c3)
                    calcStack.pop()
            else:
                while ((calcStack.isEmpty() is False) and ((op2 := calcStack.peek()) != '(')
                       and (Operator.opPrecedenceHigherOrEqual(op2, c) is True) and (c != '^')):
                    op2 = calcStack.peek()
                    c2 = operand.pop()
                    c1 = operand.pop()
                    op2 = calcStack.pop()
                    c3 = Operator.doOperation(c1, op2, c2)
                    operand.append(c3)
                else:
                    calcStack.push(c)

        while (calcStack.isEmpty() is False):
            c2 = operand.pop()
            c1 = operand.pop()
            op = calcStack.pop()
            c3 = Operator.doOperation(c1, op, c2)
            operand.append(c3)

        return operand[0]
