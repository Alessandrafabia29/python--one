print('\033[32m---=---' * 3)
print(' CADASTRO NACIONAL')
print('---=---' * 3)
somaidade = 0
media = 0
maioridadehomem = 0
mulheresmenores = 0
nomevelho =0

for dados in range(1,7):
    print('\033[36m ----{} pessoa ----- \033[m'.format(dados))
    nome = str(input('Informe o Nome:')).strip()
    idade = int(input('Informe a Idade:'))
    sexo = int(input('Informeo Sexo: [1]Feminino [2]Masculino --'))
    somaidade += idade
    if dados == 1 and sexo == 2:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo == 2 and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 1 and idade < 20:
        mulheresmenores += 1
        
media = somaidade/4 

print('\033[32m ****BANCO DE DADOS****')
print('\033[33m A média da idade do grupo é {}'.format(media))
print('\033[34m O nome do Homem mais velho do grupo é {}, com {} anos.' .format(nomevelho,maioridadehomem))
print('\033[35m O número de mulheres menores de 20 anos é : {} .'.format(mulheresmenores))

input('\nPressione ENTER para sair.')