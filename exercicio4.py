from random import randint
op = 1
acertos, erros = 0, 0
while op != 0:
    try:
        chute = int(input("Digite um número entre 0 e 100: "))
        if chute < 0 or chute > 100:
            print("Número inválido")
        else:
            num_da_sorte =  randint(0, 100)
            print(f"Você escolheu {chute}")
            print(f"O número sorteado foi {num_da_sorte}")
            if chute == num_da_sorte:
                print("Você acertou!")
                acertos += 1
            else:
                #exercicio 2: Reescreva seu código para que, em caso de derrota, o jogador seja informado se o número alvo era maior ou menor que o chute
                if chute > num_da_sorte:
                    print("Você errou! O número sorteado é menor")
                else:
                    print("Você errou! O número sorteado é maior")
                erros +=1

            while op != 1 or op != 0:
                try:
                    op = int(input('''Deseja continuar? 
                                    1 - SIM
                                    0 - NAO\n'''))
                    if op == 1 or op == 0:
                        break
                    else:
                        print("Opção incorreta!")
                except:
                    print('''
                            
                            Opção incorreta!
                            1 - Continuar
                            2 - Sair''')
    except ValueError:
        print("Número inválido")

print(f''' 
Até mais!
      Você acertou {acertos} vezes
      Você errou {erros} vezes''')