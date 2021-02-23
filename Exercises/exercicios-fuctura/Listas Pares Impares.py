#Lê 20 numeros inteiros e armazena em vetores impar e par.
vetor = []
pares = []
impares = []
for numeros in range(20):
    vetor.append(numeros)
for value in vetor:
    if value % 2 == 0:
        pares.append(value)
    else:
        impares.append(value)
print(str(vetor)[1:-1])
print(str(pares)[1:-1])
print(str(impares)[1:-1])
