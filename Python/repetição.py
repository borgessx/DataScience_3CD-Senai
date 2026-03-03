while True:
    print("\033[34m]")

rep = int(input('Quantos números vai receber: '))
numeros = []
max= min = 0
for c in range(1, rep + 1):
    num = int(input(f'Número {c}: '))
    numeros.append(num)
print(f'Você digitou os números: {numeros}')

for i,c in enumerate(numeros):
    if i == 0:
        max = min = c
    if c > max:
        max = c
    if c < min:
        min = c

print(f'O maior número é: {max}')
print(f'O menor número é: {min}')
    
