#O programa mostra um vetor com 10 números na ordem inversa
vetor = []

for _ in range(10):
    numero = int(input('Digite um número: '))
    vetor.append(numero)

print('Seus numeros foram: ', vetor[::-1])