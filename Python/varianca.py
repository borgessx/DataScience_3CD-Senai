def variancia(numero):
    soma =0

    n = len(numero)
    media = sum(numero) / n

    for i in numero:
        difer = i - media
        quad = difer ** 2
        soma += quad

    variancia = soma / n
    return variancia
