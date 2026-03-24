# Média Escolar para 5 Estudantes 
# Use um for loop para iterar 5 vezes. Dentro do loop, realize a leitura das notas e a decisão 
# (if/elif/else) da média. Crie uma lista vazia (resultados = []). A cada repetição, adicione uma 
# string (ex: "Aluno 1 - Aprovado") a esta lista usando .append(). 
resultados = []

for i in range(5):
    print(f"\n--- Aluno {i + 1} ---")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    resultados.append(f"Aluno {i + 1} - {situacao} (Média: {media:.1f})")

print("\n RESULTADOS")
for resultado in resultados:
    print(resultado)

#     Cadastro Seletivo de Candidatos 
# Use um for loop para iterar 5 vezes. Dentro do loop, use um if/else para checar se o 
# candidato é menor de 18 anos (rejeição). Crie uma lista principal: candidatos_validos = []. 
# Se o candidato for válido, crie um Dicionário (ex: candidato = {'nome': '...', 'email': '...'}). 
# Adicione este Dicionário à lista: candidatos_validos.append(candidato).
candidatos_validos = []

for i in range(5):
    print(f"\n--- Candidato {i + 1} ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    if idade < 18:
        print(f" {nome} rejeitado — menor de 18 anos.")
    else:
        email = input("E-mail: ")
        candidato = {
            'nome': nome,
            'email': email,
            'idade': idade
        }
        candidatos_validos.append(candidato)
        print(f" {nome} cadastrado com sucesso!")

print("\ CANDIDATOS VÁLIDOS ")
for c in candidatos_validos:
    print(f"Nome: {c['nome']} | Idade: {c['idade']} | E-mail: {c['email']}")

    