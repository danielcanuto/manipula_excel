# Função consolida planilhas

# percorrer as  linhas da planilha

# preencher os itens no formulario
import pandas as pd


my_planilha = "pastas_af.xlsx"

data_frame = pd.read_excel(my_planilha)


for id,row in data_frame.iterrows():
    print(f'id: {id} Siape {row["SIAPE"]} - Nome {row["Nome servidor"]}')
