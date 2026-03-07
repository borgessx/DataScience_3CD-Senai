from datetime import date

salario = float(input("Digite o salário inicial do funcionário: "))
ano_contratacao = int(input("Digite o ano de contratação: "))

ano_atual = date.today().year


percentual = 0.015

for ano in range(ano_contratacao +1, ano_atual + 1):
    salario += salario * percentual
    percentual *= 2  # dobra o percentual a cada ano

print(f"O salário atual em {ano_atual} é: R${salario:.2f}")
