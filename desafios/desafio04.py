# # #1. Cálculo de Lâmpadas:
# # #Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
# # #iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
# # #lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
# # #cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
# # #3m² existe um bocal para uma lâmpada.
# #
largura = float(input("Digite a largura do cômodo: "))
comprimento = float(input("Digite o comprimento do cômodo: "))
potencia_lampada = 3
area = largura * comprimento
total_lampadas = area / potencia_lampada
print(f'sao necessarias {total_lampadas} lampadas para iluminar um comodo de {area}' )
# #
# # # #2. Quantidade de Caixas de Azulejos:
# # # #Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
# # # #largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
# # # #todas as suas paredes (considere que não será descontada a área ocupada por portas e
# # # #janelas). Cada caixa de azulejos possui 1,5 m²
# # #
largura = float(input("Digite a largura da cozinha: "))
comprimento = float(input("Digite o comprimento da cozinha: "))
altura = float(input("Digite a altura da cozinha: "))
area_total = 2 * (comprimento * altura) + 2 * (largura * altura)
caixas = area_total / 1.5
print("voce precisa comprar", caixas, "caixas de azulejo")

# # #3. Rendimento do Taxista:
# # #Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
# # #preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
# # #odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
# # #combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
# # #média do consumo em km/L e o lucro (líquido) do dia.
# #
km_inicial= float(input("Digite quantos km seu veiculo tem no início do dia: "))
km_final = float(input("Digite quantos km o seu veiculo tem no final do dia: "))
combustivel = float(input("quantos litros de combustivel voce colocou no veiculo: "))
dinheiro = float(input("Digite o valor do dinheiro recebido pelos passageiros: "))
km_rodados = km_final - km_inicial
consumo_medio = km_rodados / combustivel
gasto_com_combustivel = combustivel * 6.15
lucro = dinheiro - gasto_com_combustivel
print('seu consumo_medio foi de:' ,consumo_medio)
print('seu lucro total foi:' ,lucro)

# # 4. Código de Origem do Produto:
# # Escreva um programa que leia o código de origem de um produto e imprima na tela a região
# # de sua procedência, conforme a tabela abaixo:
# # Observação: caso o código não seja nenhum dos especificados, o produto deve ser
# # encarado como “Importado”.
try:
    n = int(input("Digite um numero?: "))
    match n:
        case 1:
            print("sul")
        case 2:
            print("norte")
        case 3:
            print("leste")
        case 4:
            print("oeste")
        case 5 | 6:
            print("nordeste")
        case 7 | 8 | 9:
            print("sudeste")
        case 10:
            print("centro-oeste")
        case _:
            print("importado")
except ValueError:
    print('erro desconhecido')


# 5. Média do Aluno com Optativa:
# Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
# optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
# ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
# substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
# mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
# recuperação, de acordo com as informações abaixo:

nota1 = float(input('primeira nota:'))
nota2 = float(input('segunda nota:'))
nota_opt = float(input('tem nota optativa??'))
 

if nota_opt == -1:
    media = (nota1 + nota2 )/2
else:
    if nota_opt > nota1:
         media = (nota_opt + nota2)/2
    else:
        media = (nota_opt + nota1 )/2
if media >= 6.0:
    resultado = 'aprovado'
elif media >= 3.0:
    resultado = 'recuperação'
else:
    resultado = 'reprovado'

print(f'media final:', {media}, 'resultado:',{resultado})



# 6. Positivo ou Negativo:
# Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o
# valor zero como positivo.

n = int(input("Digite um numero?: "))
if n < 0:
    print("negativo")
else: n > 0
print("positivo")
