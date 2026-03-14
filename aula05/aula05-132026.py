# intervalo1 = range(10)
# print(intervalo1)


# for numero in range(1,10,2):# a primeira virgula vai pular o 0 # a ultima vai pular de 2 em 2 
#     print('número:')
#     print (numero)

print("--- Usando FOR (Repetição Contada) ---") 
# O range(5) gera os números 0, 1, 2, 3, 4 (5 repetições) 
for i in range(5):  
    try: 
        # i representa o número atual da repetição (0, 1, 2...) 
        print(f"Número {i + 1} de 5:") 
        num = float(input("Digite um número: ")) 

        dobro = num * 2 
        triplo = num * 3 
        quádruplo = num * 4 

        print(f"  Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n") 

    except ValueError: 
         print("Entrada inválida. Tente novamente.")
         
# >>> WHILE
# #1
# loolap=float(input('qual o valor do ingresso '))

# while loolap >= 300:
#     print("mas nao vou mesmo!!!")

# print('estarei la')

# #2
# loolap=300.0000000001
# while loolap >= 300:
#     print("mas nao vou mesmo!!!")

# print('estarei la')

#3
loolap=301.0000000000000
while loolap > 300:
    print("mas nao vou mesmo!!!")

print('estarei la')

#Desafios: 
#1. Cálculo de Média Escolar para Vários Alunos 
#Use o laço for para repetir a lógica de cálculo de média e status 
#(Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudantes.
