#Número positivo, negativo ou zero
i = 0
while i < 5:
    num = int(input('digite um número: '))
    i += 1  
    if num < 0:
        print('esse número é negativo>')

    elif num == 0:
        print('esse número é zero.')

    else:
        print('esse número é positivo.')