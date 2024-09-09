def jokenpo():
    import random
    error = True
    vitorias, derrotas, op = 0, 0, '1'
    while op == '1':
        jogada_PC = random.choices(["pedra", "papel", "tesoura"])
        while error == True:
            jogada_Usuario = input('Pedra, papel ou tesoura?')
            if jogada_Usuario == 'pedra' or jogada_Usuario == 'papel' or jogada_Usuario == 'tesoura':
                error = False
            else:
                print('Jogada inválida')
            print(f'PC:{jogada_PC[0]} X {jogada_Usuario}:Usuario')
        if jogada_Usuario == jogada_PC[0]:
            print('Empate')
        elif (jogada_Usuario == 'pedra' and jogada_PC[0] == 'tesoura') or (jogada_Usuario == 'papel' and jogada_PC[0] == 'pedra') or (jogada_Usuario == 'tesoura' and jogada_PC[0] == 'papel'):
            print(f'Parabéns, {jogada_Usuario} ganha de {jogada_PC[0]}')
            vitorias += 1
        else:
            print(f'Você perdeu, {jogada_Usuario} perde pra {jogada_PC[0]}')
            derrotas +=1
        op = input('Deseja continuar? 1-Sim 0-Não')
        while op != '1' and op != '0':
            print('Opção inválida')
            op = input('Deseja continuar? 1-Sim 0-Não')

        error = True
    print(f'Você ganhou {vitorias} vezes e perdeu {derrotas} vezes')

    print(f'Até mais')

