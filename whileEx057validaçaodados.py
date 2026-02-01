print('-='*6,'VALIDAÇÃO DE DADOS','-='*6)
sexo = str(input('Informe seu sexo:')).upper()[0].strip()
while sexo not in 'FM':
    print('\033[31m Dados inválidos:Tente novamente.\033[m')
    sexo = str(input('Informe seu sexo:')).upper()[0].strip()
print('\033[032m Dados registrados com Sucesso.\033[m')


