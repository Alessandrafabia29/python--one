soma = 0
cont = 0
for c in range(1,501,2):
    if c %3 == 0:
        soma = soma + c #acumulador
        cont = cont+1   #contador
print(f'A soma dos múltiplos de 3 é {soma}.')
print(f'E a quantidade de multiplos de 3 : {cont}')
