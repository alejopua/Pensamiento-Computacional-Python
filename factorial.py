def fact(n):
    """Función que calcula el factorial de n número positivo, n > 2"""
    return 1 if n == 1 else n * fact(n - 1)

n = int(input("Digite un numero positivo para calcular su factorial: "))
print(fact(n))