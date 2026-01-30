print('-='*5,'PROGRESSÃO ARITMÉTICA','-='*5)
primeiroTermo = int(input('Informe o primeiro termo da PA:'))
razao = int(input('Informe a razão para a PA:'))
dezTermos = primeiroTermo + (10-1) * razao
for contador in range(primeiroTermo,dezTermos+razao,razao):
    print(f'-> {contador}',end='')
