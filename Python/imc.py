peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

"""
Menor que 18,5	Magreza	0
Entre 18,5 e 24,9	Normal	0
Entre 25,0 e 29,9	Sobrepeso	I
Entre 30,0 e 39,9	Obesidade	II
Maior que 40,0	Obesidade Grave	III

"""

if imc < 18.5:
    print(f"\033[32mSeu IMC é {imc:.2f} você está com Magreza.\033[0m")
elif imc >18.5 and imc <25:
    print(f"\033[32mSeu IMC é {imc:.2f} você está com Peso Normal.\033[0m")
elif imc >25 and imc <30:
    print(f"\033[32mSeu IMC é {imc:.2f} você está com Sobrepeso.\033[0m")
elif imc >30 and imc <40:
    print(f"\033[32mSeu IMC é {imc:.2f} você está com Obesidade.\033[0m")
else:
    print(f"\033[32mSeu IMC é {imc:.2f} você está com Obesidade Grave.\033[0m")