def verificaMenu():
    opcao = input('''
    Bem vindos ao console de jogos em Python!
    
    Escolha uma das opções abaixo:
    1 - Jokepon
    2 - Advinhação
    3 - Quiz
    0 - Sair
    ''')
    if opcao not in ['1', '2', '3', '0']:
        print('Opção incorreta! Tente novamente.')
        return verificaMenu()
    else:
        return opcao