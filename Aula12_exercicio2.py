perguntas = ['Que animal é maior que 3 e menor que 4?', 
             'Que animal é considerado o rei da floresta? ',
             'Que animal é conhecido por ter listras pretas e brancas?']
respostas = ["piolho", 'leao', 'zebra']
print('''
Bem vindo!
Preparamos uma pergunta para você.
''')

for i, pergunta in enumerate(perguntas):
    resposta = input(f'{pergunta}').lower().replace("ã", "a").replace('é', 'e').replace('ú', 'u').replace('í','i').replace('ç', 'c')
    print("Acertou!") if resposta == respostas[i] else print("Errou!")

