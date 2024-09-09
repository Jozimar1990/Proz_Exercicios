def quiz():
    perguntas = ['Que animal é maior que 3 e menor que 4?', 
                'Que animal é considerado o rei da floresta? ',
                'Que animal é conhecido por ter listras pretas e brancas?',
                'Que animal é conhecido por ser amigo do home?']
    respostas = ["piolho", 'leao', 'zebra', 'cachorro']
    print('''
    Bem vindo!
    Preparamos uma pergunta para você.
    ''')

    for i, pergunta in enumerate(perguntas):
        resposta = input(f'{pergunta}').lower().replace("ã", "a").replace('é', 'e').replace('ú', 'u').replace('í','i').replace('ç', 'c').replace('à', 'a').replace('â', 'a')
        print("Acertou!") if resposta == respostas[i] else print("Errou!")
