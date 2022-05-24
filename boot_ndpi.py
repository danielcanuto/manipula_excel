# Função consolida planilhas

# percorrer as  linhas da planilha

# preencher os itens no formulario
import pandas as pd


my_planilha = "pastas_af.xlsx"

data_frame = pd.read_excel(my_planilha)

print(type(data_frame))


for id,row in data_frame.iterrows():
    print(f'id: {id} Siape {row["SIAPE"]} - Nome {row["Nome servidor"]}')

plan = pd.read_excel(r"pastas_af.xlsx")

# esse print irar imprimr a colun a Nome servidor na linha 2
print(plan['Nome servidor'] [2])

print(plan)