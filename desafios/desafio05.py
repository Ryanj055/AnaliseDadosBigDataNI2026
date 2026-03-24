# #Desafios: 
# #1. Cálculo de Média Escolar para Vários Alunos 
# #Use o laço for para repetir a lógica de cálculo de média e status 
# #(Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudantes.

media = print(input("qual é a sua nota?"))
if media >= 6:
    print('voce foi aprovado')
elif media <= 4:
    print('voce esta de recuperação')
else: media <= 3    
print('voce esta reprovado')


try:
nota = int(input('qual foi a sua nota?: '))

if nota <= 3:
    print("reprovado")
elif nota <= 5:
    print("recuperação")
elif nota <= 10:
    print("aprovado")
else:
    print("nota inválida")


# # 2. Cadastro de Candidatos 
# # Desenvolva um programa que colete dados de 12 pessoas, usando a decisão para filtrar 
# # candidatos menores de 18 anos. 
# # ● O programa deve pedir o Ano de Nascimento do candidato. 
# # ● Se for menor de 18, o programa deve informar que ele não pode participar e pular 
# # a coleta dos demais dados (telefone, email etc) para esse candidato. 
# # ● Se for maior de 18, o programa prossegue com o input() para os demais dados. 
 data_nasc = int(input('em qual ano voce nasceu: ?'))
idade = data_nasc - 2026
print(idade)
if idade > 18:
  
# # 3. Tentativa de Login e Senha 
# # Simule um sistema de login simples onde o usuário tem um número limitado de tentativas 
# # para digitar a senha correta. 
# # ● Defina um nome de usuário e uma senha corretos (ex: admin e 123456). 
# # ● Dê ao usuário 3 tentativas para acertar a combinação. 
# # ● Se a senha estiver correta, imprima uma mensagem de sucesso e use o comando 
# # break para sair do loop. 
# # ● Se a senha estiver errada, informe o erro e diminua o número de tentativas 
# # restantes. 
# # ● Se as tentativas acabarem, imprima uma mensagem de bloqueio.

print(" Sistema de Login ")
usuario_correto = "admin"
senha_correta = "123456"
tentativas = 3

while tentativas > 0:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso!")
        break

    tentativas -= 1
    print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas}")

if tentativas == 0:
    print("Bloqueado! Número máximo de tentativas atingido.")
    