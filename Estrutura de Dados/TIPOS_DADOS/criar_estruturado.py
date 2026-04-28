# Dados estruturados
# Criacao de arquivos estruturados 

import pandas as pd

# Estrutura de Dicionario 
dados_planilha = {
    "Nome" : ["Ana", "Carlos", "Jessica", "Rodrigo", "Marcelo"],
    "Idade": [23,50,26,35,63],
    "Cidade": ["Sao Paulo","Sao Caetano","Maua","Diadema","Sao Bernado"]
}

df_planilha = pd.DataFrame(dados_planilha)
print(df_planilha)

with pd.ExcelWriter("dadosEstruturados.xlsx") as writer:
    df_planilha.to_excel(writer, sheet_name="Planilha Estruturada", index=False)
