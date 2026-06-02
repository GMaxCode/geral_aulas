'''
5. Nota do aluno

Peça uma nota (0 a 10) e classifique:

0 a 4 → Reprovado
5 a 6 → Recuperação
7 a 10 → Aprovado

'''
nota = float(input('digite sua nota: '))

try:

    if nota < 0 or nota > 10:
        print('nota invalida!! Digite números de 1 a 10!!')

    elif nota <= 4:
        print('você foi reprovado!!')

    elif nota <=6:
        print('você ficou de recuperação!!')
        
    else:
        print('você foi aprovado!!!')

except ValueError:
    print('Digite apenas números!!')