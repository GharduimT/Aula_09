

#criando um dicionário  que vai receber os valores que o usuário vai digitar
# nome = input('Informe o nome do vendedor:')
# valor = input('Informe o valor da venda:')

# pessoa = {
#     'Nome': nome,
#     'Valor': valor,
# }

# #sem função
# lst_cadastro = []

# nome = input('Informe o nome do vendedor:')
# valor = input('Informe o valor da venda:')

# pessoa = {
#     'Nome': nome,
#     'Valor': valor,
# }
# lst_cadastro.append(pessoa) #quando executar vai colocar o que está entre parenteses na lista

#com função
#o que essa função faz? vai repetir x vezes a quantidade x que p usuário informar
#for - numero de vezes previsível
#while - numero de vezes imprevisível
#para numero inteiro RANGE
def cadastra_pessoa(num):
    for i in range(num):
        nome = input('Informe o nome do vendedor:')
        valor = input('Informe o valor da venda:')

        pessoa = {
            'Nome': nome,
            'Valor': valor,
        }
        lst_cadastro.append(pessoa)  # quando executar vai colocar o que está entre parenteses na lista


lst_cadastro = []


qtd = int(input('Quantas pessoas? '))
cadastra_pessoa(qtd)  #captura a função
print(lst_cadastro)
'''SAÍDA
Quantas pessoas? 3
Informe o nome do vendedor:ANA
Informe o valor da venda:200
Informe o nome do vendedor:BOB
Informe o valor da venda:100
Informe o nome do vendedor:PEDRO
Informe o valor da venda:33
[{'Nome': 'ANA', 'Valor': '200'}, {'Nome': 'BOB', 'Valor': '100'}, {'Nome': 'PEDRO', 'Valor': '33'}]
'''