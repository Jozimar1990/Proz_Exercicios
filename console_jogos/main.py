from advinhacao import advinhacao
from jokenpo import jokenpo
from quiz import quiz
from verifica import verificaMenu

opcao = 1

while opcao != "0":
    opcao = verificaMenu()

    match opcao:
        case "1":
            jokenpo()
        case "2":
            advinhacao()
        case "3":
            quiz()
        case "0":
            print("Até a próxima!")
