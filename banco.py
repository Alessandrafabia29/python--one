print('-=-' * 20)
print('\033[1;43m EMPRÉSTIMO BANCÁRIO \033[m')
print('-=-' *20)
nome = str(input('Informe o nome completo do cliente:'))
casa = float(input('Informe o valor da casa a ser financiada:'))
salario = float(input('Informe o salário do cliente:'))
anos = int(input('Em quantos anos será o financiamento:'))
prestacao = casa / (anos * 12)
prestacaoMinima = salario * 30/100
print('Para o(a) {} financiar uma casa no valor de R$ {:.2f}, Em {} anos, A prestação será de {:.2f}.'.format(nome,casa,anos,prestacao))
if prestacao <= prestacaoMinima:
    print('EMPRÉSTIMO \033[1;32m CONCEDIDO. \033[m')
else:
    print('EMPRÉSTIMO \033[1;31m NEGADO. \033[m')
    print('Porque a prestação mínima não atingiu a requisição bancária.')