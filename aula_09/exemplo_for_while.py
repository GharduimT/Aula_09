# # Explicando for while

# lst_valores = [] #  lista vazia

# #estrutura For
# for i in range(5): #RANGE - intervalo numérico
#     num = int (input('Informe o número: '))
#     lst_valores.append(num) #  append
# print (f'Os números são{lst_valores}')

#While

lst_nomes = []
resposta = ''

while resposta != 'n': #enquando resposta for diferente de...
    nome =input('Informe o nome: ')
    lst_nomes.append(nome) #se parasse aqui haveria repetição continuamente
    
