# import pandas as pd

# df = pd.read_excel('base_invest.xlsx', sheet_name= 'Transacoes')
# # df = pd.read_excel(r'C:\Users\conceicao.ryan\Documents\UC1\base_invest.xlsx', sheet_name='Transacoes')
# print(df.head())


# df[df['operacao'] == 'compra']
# df[df['operacao'] == 'venda']

# # Máximo de compra 
# # Mínimo de compra
# # Máximo de venda
# # Mínimo de venda

# # df[df['operacao'] == 'compra']['preco'].max()
# # df[df['operacao'] == 'compra']['preco'].min()
# # df[df['operacao'] == 'venda']['preco'].max()
# # df[df['operacao'] == 'venda']['preco'].min()

# print("Máximo de compra", df[df['operacao'] == 'compra']['preco'].max())
# print("Mínimo de compra", df[df['operacao'] == 'compra']['preco'].min())
# print("Máximo de venda", df[df['operacao'] == 'venda']['preco'].max())
# print("Mínimo de venda", df[df['operacao'] == 'venda']['preco'].min())

import pandas as pd

df_transacoes = pd.read_excel('C:\\Users\\conceicao.ryan\\Documents \\base_invest.xlsx', sheet_name='Transacoes')
df_ativo = pd.read_excel('C:\\Users\\conceicao.ryan\\Documents \\base_invest.xlsx', sheet_name='Ativo')

# Pergunta 1: Quais são as máximas e mínimas de operação de compra e venda das transações? ---
# variável nova    tabela[filtro]
df_compra = df_transacoes[df_transacoes['operacao'] == 'compra']
#
df_venda = df_transacoes[df_transacoes['operacao'] == 'venda']
print(df_compra)
print(df_venda)


max_compra_preco = df_compra['preco'].max()
min_compra_preco = df_compra['preco'].min()
max_venda_preco = df_venda['preco'].max()
min_venda_preco = df_venda['preco'].min()

print("--- Preços máximos e mínimos das operações ---")
print(f"Preço máximo de compra: {max_compra_preco}")
print(f"Preço mínimo de compra: {min_compra_preco}")
print(f"Preço máximo de venda: {max_venda_preco}")
print(f"Preço mínimo de venda: {min_venda_preco}")
print("\n")





