#Comparar dois números
#Peça dois números e diga:
#Qual é o maior
#Ou se são iguais

while True:
    try:
        num1 = float(input('digite um número de 1 a 10: '))
        num2 = float(input('digite outro numero de 1 a 10: '))


        if not (1 <= num1 <= 10) or not (1 <= num2 <= 10):
            print('Os números devem estar entre 1 e 10.')
            continue

        elif num1 == num2:
            print('esses números são iguais.')

        elif num1 > num2:
            print(f'({num1}) é maior que o número ({num2}).')

        else:
            print(f'({num2}) é maior que o número ({num1}).')
    except ValueError:
        print('digite apenas números.')
        continue 
    sair = input('deseja sair ? responda [s]im ou não.').lower().startswith('s')
    if sair:
     break

  


