import math


def addNumbers(num1: int, num2: int, *args: int):
    try:
        return num1+num2+sum(args)
    except TypeError as te:
        return f"Error: {te}"


def subtractNumbers(num1: int, num2: int, *args: int):
    try:
        return (num1-num2)-(sum(args))
    except TypeError as te:
        return f"Error: {te}"


def multipleNumbers(num1: int, num2: int, *args: int):
    try:
        return num1*num2*math.prod(args)
    except TypeError as te:
        return f"Error: {te}"


def divideNumbers(num1: int, num2: int, *args: int):
    if num2 == 0:
        return f"Error: Division by zero is not allowed"
    try:
        result = num1 / num2
    except TypeError as te:
        return f"Error: {te}\nHere is the problem --> result={num1}/{num2}" 
    if args:
        for arg in args:
            if arg == 0:
                return "Error: Division by zero is not allowed"
            else:
                try:
                    result /= arg
                except TypeError as te:
                    return f"Error: {te}\nHere is the problem --> result/={arg}" 
    return result


def getRemainderValue(num1: int, num2: int, *args: int):
    result = num1 % num2
    for arg in args:
        try:
            result %= arg
        except TypeError as te:
            return f"Error: {te}"
    return result


def getExponentialValue(num1:int,num2:int,*args:int):
    result = num1 ** num2
    if args:
        for arg in args:
            try:
                result**=arg
            except TypeError as te:
                return f"Error: {te}\nHere is the problem result**{arg}"
            
    return result