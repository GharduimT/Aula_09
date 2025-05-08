lst_nomes = []
resposta = ''

while resposta != 'n': #enquando resposta for diferente de...
    nome =input('Informe o nome: ')
    lst_nomes.append(nome) #se parasse aqui haveria repetição continuamente
    
    resposta = input('Quer continuar? [s/n]: ')

print(f'Os nomes foram {lst_nomes}')