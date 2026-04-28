# Dados semiestrurados
# Json
import pandas as pd

dados_planilha = {
    "Nome" : ["Ana", "Carlos", "Jessica", "Rodrigo", "Marcelo"],
    "Idade": [23,50,26,35,63],
    "Cidade": ["Sao Paulo","Sao Caetano","Maua","Diadema","Sao Bernado"]
}

dados_json = {
    "Nome" : ["Ana", "Carlos", "Jessica", "Rodrigo", "Marcelo"],
    "Idade": [23,50,26,35,63],
    "Cidade": ["Sao Paulo","Sao Caetano","Maua","Diadema","Sao Bernado"]
}

df_json = pd.DataFrame(dados_json)
df_json.to_json("dadosSemi.json", orient = "records", lines=False)
