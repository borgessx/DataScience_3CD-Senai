from datetime import date

def calcular_salario(salario_inicial, ano_contratacao,percentual=0.015):
    ano_atual = date.today().year
    salario = salario_inicial 

    for ano in range(ano_contratacao + 1, ano_atual + 1):
        if ano < 1997:
            salario += salario * percentual

        else:
            percentual *= 0.5
            salario += salario * percentual

    return salario


salario = float(input("Digite o salário inicial: "))
ano = int(input("Digite o ano de contratação: "))

salario_atual = calcular_salario(salario, ano)

print(f"Salário atual em {date.today().year}: R${salario_atual:.2f}")
