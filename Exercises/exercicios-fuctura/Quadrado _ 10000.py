import math
grupo = []
for raiz in range(0, 10000):
    grupo.append(math.isqrt(raiz))
    resultado = max(grupo) ** 2
print(f'O maior número quadrado menor que 10000 é o {resultado}')






