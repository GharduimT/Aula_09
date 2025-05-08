# # Explicando for while

# lst_valores = [] #  lista vazia

# #estrutura For
# for i in range(5): #RANGE - intervalo numérico
#     num = int (input('Informe o número: '))
#     lst_valores.append(num) #  append
# print (f'Os números são{lst_valores}')

#While

# lst_nomes = []
# resposta = ''

# while resposta != 'n': #enquando resposta for diferente de...
#     nome =input('Informe o nome: ')
#     lst_nomes.append(nome) #se parasse aqui haveria repetição continuamente
    
#     resposta = input('Quer continuar? [s/n]: ') #como resposta não foi diferente de 'n' ele escreveu na tela o que guardou na lista

# print(f'Os nomes foram {lst_nomes}')

#contador
lst_nomes = []
contador = 0
while contador < 5:
     nome = input('informe o nome')
    lst_nomes.append(nome)
    contador += 1


#loopinfinito
lst_nomes2 = []
while True:
    nome = input('informe o nome')
    lst_nomes2.append(nome)

    resposta = input('Quer continuar? [s/n] ').lower()
    if resposta == 'n':
        break