print('\033[32m -='*5,'PROGRAMA TABUADA','-='*5,'\033[m')
cont = 'S'
while cont == 'S':
    num = int(input('Informe um número para sua Tabuada:'))
    for c in range(1,11):
        print(f'{c} x {num} = {num*c}')
    cont = str(input('Quer continuar? [S][N]:')).upper()
print('FIM DO PROGRAMA')
