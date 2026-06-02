produtos = {
    'macarrão': 4.54,
    'arroz': 16.90,
    'feijão': 3.40,
    'carne': 30.00
}
g = 0
while True:
    num1 = input(f'qual produto deseja comprar {produtos.keys()}: ').lower() #
    num2 = int(input(f'quantos você vai querer de {num1}: '))
    total = produtos.get(num1) * num2 
    g += total
    sair = input('deseja mais alguma coisa [s]im ou [n]ão: ').capitalize()
    if sair == 'Não':
        print(f'muito obrigado!! a compra ficou no valor de R$ {g:.2f}')
        break
    else:
        print('continue...')
        continue
    
        

 

