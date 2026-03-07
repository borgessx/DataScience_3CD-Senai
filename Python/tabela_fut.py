tab_fut = {}
m = 0

while True:
    print("\033[1;33mTABELA DE FUTEBOL\033[0m\n")
    time = str(input('Digite o nome do time: ')).upper()
    if time == 'SAIR':
        break
    pontos = int(input('Digite a quantidade de pontos: '))

    tab_fut[time] = pontos


items = list(tab_fut.items())

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[j][1] > items[i][1]:
            items[i], items[j] = items[j], items[i]

for t, p in items:
    print(f'Time: {t} - Pontos: {p}')