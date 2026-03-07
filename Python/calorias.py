dic_cal = {}

dic_cal['Data'] = str(input('Digite a data: '))
dic_cal['Tempo caminhada'] = float(input('Digite o tempo de caminhada: '))
dic_cal['refeição'] = str(input('Digite a refeição: '))
dic_cal['calorias'] = float(input('Digite a quantidade de calorias perdidas: '))

with open("arquivo.txt", "w") as f:
    f.write(str(dic_cal))