def soma(a, b):
    return a + b + 1

def mult(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida")
    return a / b
