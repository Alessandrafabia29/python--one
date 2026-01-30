from random import randint
computador = randint(0,15)
print('\033[35m--==--' * 11)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 15.')
print('Será que você consegue advinhar qual foi?')
print('--==--' * 11 + '\033[33m')
acertou = False
palpite = 0



    
while not acertou:
    jogador = int(input('\033[32m Qual seu palpite?'))
    palpite = palpite + 1 
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[33m ++...Mais...+++Tente mais uma vez!')
        elif jogador > computador:
            print('\033[34m --...Menos...--Tente mais uma vez!')
    
print('\033[036m ACERTOU!!! com {} palpites!'.format(palpite))

       


input('\nPressione Enter para sair...')

