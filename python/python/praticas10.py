# DICIONARIOS
while True:
    print('Hoje nos temos: >>> Maçã, Pera e Goiaba')
    digite = input('digite o que deseja hoje: ')
    produtos = {
        'maçã': '5.0',
        'pera': '6.8',
        'goiaba': '7.5'
    }
    if digite == "Goiaba":
        print(produtos['goiaba'])
    elif digite == 'Maça':
        print(produtos['maçã'])
    else:
        print(produtos['pera'])



