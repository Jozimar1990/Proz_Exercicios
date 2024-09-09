from advinhacao import advinhacao
from jokenpo import jokenpo
from quiz import quiz

opcao = input(
    '''
    Bem vindos ao console de jogos em Python!
    
    Escolha uma das opções abaixo:
    1 - Jokepon
    2 - Advinhação
    3 - Quiz
    0 - Sair
    '''
)

match opcao:
    case "1":
        jokenpo()
    case "2":
        advinhacao()
    case "3":
        quiz()
    case _:
        print("opção incorreta!")
