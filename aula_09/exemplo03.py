def cadastra_pessoa(num):
    for i in range(num):
        nome = input('Informe o nome do vendedor:')
        valor = float(input('Informe o valor da venda:'))

        pessoa = {
            'Nome': nome,
            'Valor': valor,
        }
        lst_cadastro.append(pessoa)  

#Média e Total
def calcula_total_media():
    tot = 0
    for pessoa in lst_cadastro:
        tot += pessoa['Valor']

    med = tot /len(lst_cadastro)
    return tot, med

def buscar_maior():
    maior = 0
    vendedor = ''

    for v in lst_cadastro:
        if v['Valor'] > maior: #se o queestá na chave for maior do que o que tem na variável...
            maior = v['Valor']
            vendedor = v['Nome']

    return maior, vendedor


#EXEMPLO 01 - CADASTRA FUNCIONARIO
lst_cadastro = []


qtd = int(input('Quantas pessoas? '))
cadastra_pessoa(qtd)  #captura a função
print(lst_cadastro)

# -------------------------
#exemplo 02 - TOTAL E MEDIA
total, media = calcula_total_media()
print(50*'=')
print(f'Total: {total}')
print(f'Total: {media}')

#EXEMPLO 03 - MAIOR VALOR E VENDEDOR

maior_venda, maior_vendedor = buscar_maior()

print(50*'=')
print(f'Maior Venda: {maior_venda}')
print(f'Nome do Vendedor: {maior_vendedor}')