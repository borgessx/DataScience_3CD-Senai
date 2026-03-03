total = cont = 0

while True:
    preco = float(input('Preço: R$ '))
    total = total + preco
    if preco == 0:
        print(f'Valor final: R$ {total:.2f} \nQuantidade de itens: {cont} \nMédia: R$ {total/cont:.2f}')
        break
    elif preco < 0:
        print('Valor inválido. Tente novamente.')
        continue
    cont += 1
