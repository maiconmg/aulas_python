"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id =  Identidade
"""
condicao = False
passou_no_if = None
if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('Nao faça algo')

if passou_no_if is None:
    print('Nao passou no if')

else:
    print('passou no if')