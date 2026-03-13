# carro=True
# combustivel=True
# # qual é a condição pra que este carro funcione??
# if carro==True and combustivel==True:
#     print('meu fusquinha ésta rodando.')
# elif carro==False or combustivel==False:
#     print('nao sobrou nada')
# else:
#     print('erro de execução')

# print('-'*25)

# if not carro and not combustivel:
#     print('meu fusquinha ésta rodando.')
# elif carro==False or combustivel==False:
#     print('nao sobrou nada')
# else:
#     print('erro de execução')

# semana = int(input('digite um numero: ')) 
# if semana == 1: 
#     print("Domingo") 
# elif semana == 2: 
#     print("Segunda-feira") 
# elif semana == 3: 
#     print("Terça-feira") 
# elif semana == 4: 
#     print("Quarta-feira") 
# elif semana == 5: 
#     print("Quinta-feira") 
# elif semana == 6: 
#     print("Sexta-feira") 
# elif semana == 7: 
#     print("Sábado") 
# else: # O 'else' funciona como o 'default' 
#     print("Dia inválido")

## sem tratamento de exces

try:
    mes = int(input('digite um numero: '))  
    match mes: 
        case 1: 
            print("Janeiro") 
        case 2: 
            print("Fevereiro") 
        case 3: 
            print("Março") 
        case 4: 
            print("abril") 
        case 5: 
            print("Maio") 
        case 6: 
            print("Junho")
        case 7:
            print("julho")
        case 8: 
            print("agosto") 
        case 9 : 
            print("setembro") 
        case 10: 
            print("outubro") 
        case 11: 
            print("novembro") 
        case 12: 
            print("dezembro")  
        case _: # O underline ( _ ) funciona como o 'default' ou 'else' 
            print("Mês inválido") 
except ValueError: 
    print('error desconhecido.')



try: 
    numero_mes = int(input("Digite um número de 1 a 12: "))
    match numero_mes: 
        case 1: 
            print("O número 1 corresponde a Janeiro.")
        case 2:
            print("O número 2 corresponde a fevereiro.") 
        case 3:
            print("O número 3 corresponde a março.")
        case 4:
            print("O número 4 corresponde a abril.")
        case 5:
            print("O número 5 corresponde a maio.")
        case 6:
            print("O número 6 corresponde a junho.")
        case 7:
            print("O número 7 corresponde a juho.")
        case 8:
            print("O número 8 corresponde a agosto.")
        case 9:
            print("O número 9 corresponde a setembro.")
        case 10:
            print("O número 10 corresponde a outubro.")
        case 11:
            print("O número 11 corresponde a novembro.")
        case 12: 
            print("O número 12 corresponde a Dezembro.") 
        case _: 
            print(f"Número {numero_mes} inválido. Digite entre 1 e 12.") 

except ValueError: 
    print('errouuuuuuuuu.')
except TypeError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
except IndentationError:
    print("")
except ZeroDivisionError:
    print("")
