"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
condicao = True

while condicao:
    nome = input('Qual é o seu nome: ')
    print(f'seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')
