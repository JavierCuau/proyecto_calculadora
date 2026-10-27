# calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def potencia(a, b):
    return a ** b

if __name__ == "__main__":
    num1 = 10
    num2 = 4
    
    print(f"El resultado de la suma es: {sumar(num1, num2)}")
    print(f"El resultado de la resta es: {restar(num1, num2)}")
    print(f"El resultado de la multiplicación es: {multiplicar(num1, num2)}")
    print(f"El resultado de la división es: {dividir(num1, num2)}")
    print(f"El resultado de la potencia es: {potencia(num1, num2)}")
