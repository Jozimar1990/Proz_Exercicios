#Aula 12 - Exercício de revisão 3
#Reescreva seu código para que cada pergunta tenha uma pontuação específica. Ao final, o programa deve informar a pontuação total do jogador
#Desafio
#Reescreva seu código para que seja possível voltar a uma pergunta anterior e alterar sua resposta

perguntas = {"piolho":'Que animal é maior que 3 e menor que 4?', 
             'leao':'Que animal é considerado o rei da floresta? ',
             'zebra':'Que animal é conhecido por ter listras pretas e brancas?',
             'cachorro':'Que animal é conhecido por ser amigo do home?'}
print('''
Bem vindo!
Preparamos uma pergunta para você.
''')
ponto = 0 
print(len(perguntas))
for i, pergunta in enumerate(perguntas):
    resposta = input(f'{perguntas[pergunta]}').lower().replace("ã", "a").replace('é', 'e').replace('ú', 'u').replace('í','i').replace('ç', 'c').replace('à', 'a').replace('â', 'a')
    if resposta == pergunta:
        print('Acertou!')
        ponto += 3
        i += 1
    else:
        print("Errou!")
        ponto -= 1
        outra_tentativa = input("Deseja tentar novamente? 1 - SIM | 0 - NAO")
        if outra_tentativa == '1':
            
        else:
            i += 1

print(f"Você obteve {ponto} pontos, mais sorte da próxima")