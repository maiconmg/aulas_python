# Exercicios - sistema de perguntas e repostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25', 
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

i = 0
acertos = 0
seila = 'Pergunta'
while True:
    for indice, a in perguntas[i].items():
        print(indice, a)

    i += 1
