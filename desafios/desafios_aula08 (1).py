# atividades da aula 8 - funcoes

#
# desafio 1 - controle de pesca


def calcular_multa(peso_total):
    # se passar de 100kg paga 4 reais por kilo a mais
    limite = 100
    if peso_total > limite:
        quanto_passou = peso_total - limite
        multa = quanto_passou * 4.0
        return multa
    return 0.0  # se nao passou do limite nao tem multa

total_multas = 0.0

while True:
    peso = float(input("quanto pescou hoje? (0 pra sair): "))
    if peso == 0:
        break

    multa = calcular_multa(peso)

    if multa > 0:
        print(f"ops! multa de R$ {multa:.2f}")
    else:
        print("tudo certo, dentro do limite!")

    total_multas += multa

print(f"\ntotal de multas da semana: R$ {total_multas:.2f}")



# desafio 2 - calculadora de imc


def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def obter_classificacao(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif imc < 25.0:
        return "peso normal"
    elif imc < 30.0:
        return "sobrepeso"
    else:
        return "obesidade"

n = int(input("quantas pessoas voce quer calcular? "))

for i in range(n):
    print(f"\npessoa {i + 1}:")
    peso = float(input("  peso em kg: "))
    altura = float(input("  altura em metros: "))

    imc = calcular_imc(peso, altura)
    resultado = obter_classificacao(imc)

    print(f"  imc: {imc:.2f} -> {resultado}")



# desafio 3 - conversor de temperatura


def celsius_para_fahrenheit(temp_c):
    return (temp_c * 9 / 5) + 32

def fahrenheit_para_celsius(temp_f):
    return (temp_f - 32) * 5 / 9

print("qual conversao voce quer?")
print("1 - celsius pra fahrenheit")
print("2 - fahrenheit pra celsius")

opcao = input("escolha: ")

if opcao == "1":
    temp = float(input("temperatura em celsius: "))
    resultado = celsius_para_fahrenheit(temp)
    print(f"{temp}C = {resultado:.1f}F")
elif opcao == "2":
    temp = float(input("temperatura em fahrenheit: "))
    resultado = fahrenheit_para_celsius(temp)
    print(f"{temp}F = {resultado:.1f}C")
else:
    print("opcao invalida...")

# desafio extra - uma funcao so que faz os dois
# achei mais dificil mas consegui!
def converter_temperatura(valor, direcao):
    if direcao == "cf":
        return (valor * 9 / 5) + 32
    elif direcao == "fc":
        return (valor - 32) * 5 / 9
    else:
        print("direcao invalida, use 'cf' ou 'fc'")
        return None



# desafio 4 - ano bissexto


def eh_bissexto(ano):
    # tive que pesquisar as regras disso aqui...
    # divisivel por 400 = bissexto
    # divisivel por 100 mas nao por 400 = nao eh
    # divisivel por 4 = bissexto
    # resto = nao eh

    if ano % 400 == 0:
        return True
    if ano % 100 == 0:
        return False
    if ano % 4 == 0:
        return True
    return False

ano = int(input("digita um ano ai: "))

if eh_bissexto(ano):
    print(f"{ano} eh bissexto!")
else:
    print(f"{ano} nao eh bissexto")



# desafio 5 - contar caractere


def contar_caractere(texto, caractere_procurado):
    contagem = 0
    # converto tudo pra minuscula pra nao diferenciar A de a
    texto = texto.lower()
    caractere_procurado = caractere_procurado.lower()

    for letra in texto:
        if letra == caractere_procurado:
            contagem += 1

    return contagem

frase = input("digita uma frase: ")
letra = input("qual letra quer contar? ")

vezes = contar_caractere(frase, letra)
print(f"a letra '{letra}' apareceu {vezes} vez(es)")



# desafio 6 - simulador de dado


import random

def rolar_dado(lados):
    return random.randint(1, lados)

# simulador de batalha
print("\n=== simulador de batalha ===")

input("aperta enter pra rolar o ataque (d20)...")
ataque = rolar_dado(20)
print(f"ataque: {ataque}")

input("aperta enter pra rolar o dano (d8)...")
dano = rolar_dado(8)
print(f"dano: {dano}")
print(f"\nvoce atacou com {ataque} e causou {dano} de dano!")
