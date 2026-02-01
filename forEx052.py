print('-='*7,'\033[35m PROGRAMA NÚMEROS PRIMOS\033[m','-='*7)
tot = 0
num = int(input('Informe um número:'))
for c in range(1,num + 1):
    if num % c == 0:   #quantos do contador c ele-num é divisivel
        print('\033[33m',end='')
        tot = tot +1
    else:
        print('\033[31m',end='')
    print(f'->{c}->',end='')

print(f'\nO número {num} foi dividido {tot} vezes.')
if tot == 2:
    print(f'O número {num} é Primo.É divisível por um e por ele mesmo.')
else:
    print(f'O número {num} não é Primo.')



