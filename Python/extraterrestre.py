# inicio


# condicao de exploracao - passo 2
def cond_expl():
    print("APHARA-7")
    pontos = 0
    obs = "" 
    resposta = input("Encontrou algum obstaculo fisico? (s/n) ").upper().strip()[:1]
    if resposta == "S":
        print("Obstaculo detectado")
        pontos += 10
        obs = input("Qual o tipo do obstaculo? (rocha, crateras, etc) ").lower().strip()
    else:
        print("Nenhum obstaculo detectado")
        pontos += 5
        cond_cie()
    return obs, pontos

# forma de superar o obstáculo
def escalar(obs):
    print(f"Iniciando processo de escalada do {obs}")
    print("Processo de escalada deu errado")


def contornar(obs):
    print(f"Iniciando processo de contorno do {obs}")
    print("Processo de contorno deu certo")

 # superar o obstáculo - passo 3
def sup_obs(obs):
    while True:
        print(f"Processo de desvio da {obs}")
        opc = input("Como deseja superar o obstáculo:\n- Escalar\n- Contornar\nQual? ").upper().strip()
        if opc == "ESCALAR":
            escalar(obs)
        elif opc == "CONTORNAR":
            contornar(obs)
            break
        elif opc == "SAIR":
            break
        else:
            print("\n\033[0;31mOpção inválida\033[0m")

# condicao cientifica - passo 6
def cond_cie():
    resposta = input("Encontrou alguma área rica em minerais ou sinais de vida ? (s/n) ").upper().strip()[:1]
    if resposta == "S":
        print("Área rica em minerais ou sinais de vida detectada")
    else:
        print("Nenhuma área rica em minerais ou sinais de vida detectada")

# fim - contagem de pontos
def fim(pontos):
    print(f"Fim da missão, pontos acumulados: {pontos}")

# coleta de dados - passo 7
def coleta(pontos):
    print("Iniciando coleta de dados")
    dec = input("Deseja prosseguir ou retornar ? ").upper().strip()
    if dec == "PROSSEGUIR":
        obs_novo, pontos_novo = cond_expl()
        pontos += pontos_novo
        # se encontrar novo obstáculo, tenta superá‑lo
        if obs_novo:
            sup_obs(obs_novo)
        return pontos
    else:
        fim(pontos)
        return pontos

# fluxo principal

obs, pontos = cond_expl()
# somente tenta superar se algum obstáculo foi informado
if obs:
    sup_obs(obs)

cond_cie()

# coleta pode alterar o total de pontos
pontos = coleta(pontos)

fim(pontos)

print("fim da missão extraterrestre")