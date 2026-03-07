vendas_brutas = [(101,"Monitor",5,1200.0),(102,"Mouse",50,80.0),(103,"Teclado",8,150.0),(104,"Case",3,50.0)]
vendas_brutas2 = [(101,"Monitor",5,1220),(102,"Mouse",50,78),(103,"Teclado",8,99.9),(104,"Case",3,55.0)]

def processamento_dados(lista):
    total_valor = 0
    print("Quantidade baixa em estoque:")
    for c in lista: 
        id = c[0]
        nome = c[1]
        quantidade = c[2]
        preco_unitario = c[3]

        valor_item = quantidade * preco_unitario
        total_valor += valor_item
        
        if quantidade < 10:
            print(f"Produto: {nome} - Quantidade: {quantidade}")

    print(f"\nTotal do inventario: {total_valor:.2f}")


print("Processamento da primeira lista: \nQual lista deseja processar? (1 ou 2)")
print(f"Lista 1: {vendas_brutas} \nLista 2: {vendas_brutas2}")
esco = input("Digite o número da lista: 1 ou 2:")
esc = 0
if esco == "1":
    esc = vendas_brutas
elif esco == "2":
    esc = vendas_brutas2

processamento_dados(esc)
    
        

    