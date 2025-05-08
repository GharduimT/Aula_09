def cadastra_pessoa(num):
    for i in range(num):
        nome = input('Informe o nome do vendedor:')
        valor = float(input('Informe o valor da venda:'))

        pessoa = {
            'Nome': nome,
            'Valor': valor,
        }
        lst_cadastro.append(pessoa)  


def calcula_total_media():
    tot = 0
    for pessoa in lst_cadastro:
        tot += pessoa['Valor']

    med = tot /len(lst_cadastro)
    return tot, med

#EXEMPLO 01 - CADASTRA FUNCIONARIO
lst_cadastro = []


qtd = int(input('Quantas pessoas? '))
cadastra_pessoa(qtd)  #captura a função
print(lst_cadastro)

# -------------------------
#exemplo 02 - TOTAL E MEDIA
total, media = calcula_total_media()
print(30*'=')
print(f'Total: {total}')
print(f'Total: {total}')

#EXEMPLO 03 - MAIOR VALOR E VENDEDOR

