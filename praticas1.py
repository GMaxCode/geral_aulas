while True:

    sua_senhA = int(input('crie uma senha com somente números: '))
    senha = int(input('digite sua senha atual: '))
    
    if senha == sua_senhA:
        print('acesso liberado!!!')

    else:
        print('está senha esta errada... Tente novamente!!')