import random

def rolar():
    max = 6
    min = 1
    rolar = random.randint(min, max)
    return rolar

while True: 
    jogadores = input('Digite o número de jogadores (2-4): ')
    if jogadores.isdigit():
        jogadores = int(jogadores)
        if 2 <= jogadores <= 4:
            break
        else:
            print('Tem que ser entre 2-4 jogadores.')
    else: 
        print('Inválido, tente novamente.')

pontos_max = 50
pontos_jogador = [0 for _ in range(jogadores)]

while max(pontos_jogador) < pontos_max:

    for index_jogador in range(jogadores):
        print('\nA vez do jogador ', index_jogador + 1, ' começou!\n')
        print('Sua pontuação total é: ', pontos_jogador[index_jogador], '\n')
        pontos_atual = 0

        while True:
            jogar = input('Gostaria de rolar? (y/n) ')
            if jogar.lower() != 'y':
                break
            resp = rolar()
      
            if resp == 1:
                print('Você rolou um 1. Sua vez acabou.')
                pontos_atual = 0
                break
            else:
                pontos_atual += resp
                print('Você rolou um ', resp)

            print('Sua pontuação é: ', pontos_atual)

        pontos_jogador[index_jogador] += pontos_atual
        print('Sua pontuação total é: ', pontos_jogador[index_jogador])

pontos_max = max(pontos_jogador)
ganhador = pontos_jogador.index(pontos_max)
print('Jogador número ', ganhador + 1, ' é o ganhador com uma pontuação de ', pontos_max)
