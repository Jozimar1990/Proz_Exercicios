respostas = ["piolho", "teste"]
print('''
Bem vindo!
Preparamos uma pergunta para você.
Que animal é maior que 3 e menor que 4?
''')
resposta = input().lower()
print("Acertou!") if resposta == respostas[0] else print("Errou!")
