# import numpy as np 
# # Dados de exemplo 
# dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40]) c
# print(dados)
# # Calcular quartis 
# q1 = np.percentile(dados, 25) # O 1º quartil representa 25% dos dados 
# q2 = np.percentile(dados, 50) # A Mediana é o mesmo que o quartil de 50% 
# q3 = np.percentile(dados, 75) # O 3º quartil representa 75% dos dados 
# # Exibir os resultados 
# print(f"Primeiro quartil (Q1): {q1}") 
# print(f"Segundo quartil (Q2, Mediana): {q2}") 
# print(f"Terceiro quartil (Q3): {q3}")

# import pandas as pd 
# # Carregar a planilha 'Transacoes' para um DataFrame 
# #df_transacoes = pd.read_excel(c:\\Users\\conceicao.ryan\\Downloads\\base_invest.xlsx', sheet_name='Transacoes') 
# # Exibir as primeiras 5 linhas para verificar os dados 
# print(df_transacoes.head())
# df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
# print(df_transacoes.iloc[2])

# import pandas as pd 
# import matplotlib.pyplot as plt 
# df_transacoes = pd.read_excel("C:\\Users\\conceicao.ryan\\Downloads\\base_invest.xlsx", sheet_name = 'Transacoes')
# # Contar a frequência de cada tipo de operação 
# contagem_operacao = df_transacoes['operacao'].value_counts() 
# # Criar um gráfico de barras 
# contagem_operacao.plot(kind='bar', title='Tipos de Operação') 
# # Mostrar o gráfico 
# plt.show()
