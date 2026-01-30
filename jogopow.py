from random import randint
from time import sleep

itens = ('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)
print('\033[32m--==--' * 5)
print('---VAMOS JOGAR JO KEN POW---')
print('--==--' * 5 + '\033[m' )
print('''Qual sua jogada:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
jogador = int(input('Qual a sua jogada:'))
print('\033[32m JO')
sleep(1)
print('KEN')
sleep(1)
print('POW!!!')
print('\033[41m -='*11 + '\033[m')
print('\033[31m COMPUTADOR jogou {}'.format(itens[computador]))
print('\033[36m JOGADOR jogou {}'.format(itens[jogador]))
print('\033[41m -='*11 + '\033[m')
if computador == 0:
    if jogador == 0:
        print('\033[33m EMPATE')
    elif jogador == 1:
        print('\033[33m JOGADOR VENCE!!!')
    elif jogador ==2:
        print('\033[33m COMPUTADOR VENCE!!')
    else:
        print('\033[33m JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('\033[33m COMPUTADOR VENCE!!!')
    elif jogador == 1:
        print('\033[33m EMPATE')
    elif jogador ==2:
        print('\033[33m JOGADOR VENCE!!')
    else:
        print('\033[33m JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('\033[33m JOGADOR VENCE!!!')
    elif jogador == 1:
        print('\033[33m COMPUTADOR VENCE!!!')
    elif jogador ==2:
        print('\033[33m EMPATE')
    else:
        print('\033[33m JOGADA INVÁLIDA')

input('\nPressione Enter para sair...')
