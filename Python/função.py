

def limp_vend(lista):
    listan = []
    for i in lista:
        if 0 < i < 10000:
            listan.append(i)
    return listan


vendas = []

while True: 
    n_filial = int(input("valores: "))
    if n_filial == 0:
        break
    vendas.append(n_filial)

vendan = limp_vend(vendas)

def tot_med(lista):
    t = 0
    for i in lista:
        t += i
    m = t / len(lista)

    return t, m

   
total, media = tot_med(vendan)

print(f"nova lista: {vendan}\ntotal: {total}\nmedia: {media}")

def def_stt(m):
    if m > 5000:
        return "Alta performance"
    elif media < 2000:
        return "Performance estável"
    else:
        return "Performance crítica"





    
