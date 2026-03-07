def media(a,b):
    return a/b

num = int(input("Quantos numeros deseja calcular a média? "))

total = 0.0
for i in range(num):
    valor = float(input(f"Digite o {i+1}* número: "))
    total += valor

resultado = media(total, num)
print(f"A media é: {resultado}")

