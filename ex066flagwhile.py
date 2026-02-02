print('-='*6,'Programa Contador e Soma','-='*5)
cont = 0
soma = 0
while True:
    num = int(input('Informe um número(999 para parar):'))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Usuário informou \033[32m {cont} números\033[m e a soma entre eles foi \033[36m {soma}. \033[m')

