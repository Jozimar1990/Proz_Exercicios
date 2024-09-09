from random import randint
tent = False
while tent == False:
  try:
    chute = int(input("Digite um número entre 0 e 100: "))
    if chute <0 or chute >100:
      print("Número inválido")
    else:
      tent = True
      num_da_sorte =  randint(0, 100)
      print(f"Você escolheu {chute}")
      print(f"O número sorteado foi {num_da_sorte}")
      if chute == num_da_sorte:
        print("Você acertou!")
      else:
        #exercicio 2: Reescreva seu código para que, em caso de derrota, o jogador seja informado se o número alvo era maior ou menor que o chute
        if chute > num_da_sorte:
          print("Você errou! O número sorteado é menor")
        else:
          print("Você errou! O número sorteado é maior")
  except ValueError:
    print("Número inválido")
