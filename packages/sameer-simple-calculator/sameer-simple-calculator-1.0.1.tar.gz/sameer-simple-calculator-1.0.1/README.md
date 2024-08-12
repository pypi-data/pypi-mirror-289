# How to Use This Package

### Import Dependencies

```

from libname.calculator import (
    addNumbers,
    subtractNumbers,
    multipleNumbers,
    divideNumbers,
    getRemainderValue,
    getExponentialValue
)
```

# Example usage
```
result_add = addNumbers(5, 3, 2)
result_subtract = subtractNumbers(10, 5, 1)
result_multiply = multipleNumbers(2, 3, 4)
result_divide = divideNumbers(20, 4, 2)
result_remainder = getRemainderValue(20, 6, 3)
result_exponential = getExponentialValue(2, 3, 2)
```


```
print(f"Addition Result: {result_add}")
print(f"Subtraction Result: {result_subtract}")
print(f"Multiplication Result: {result_multiply}")
print(f"Division Result: {result_divide}")
print(f"Remainder Result: {result_remainder}")
print(f"Exponential Result: {result_exponential}")

```