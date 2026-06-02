# _, nome2,*_ =  ['guilherme', 'joão', 'maria'] #desempacotamento + tuplas 
# print(nome2,_) 

'''
-------------------------------------------------------------------------------------------
'''

# tuplas = ['guilherme', 'joão', 'maria'] #tuplas são imutáveis, ou seja não é possível mudar o valor que tem nela.
# lista = tuple(tuplas)
# print(lista)

'''
-------------------------------------------------------------------------------------------
'''
tuplas = ['guilherme', 'joão', 'maria'] 
lista_enum = enumerate(tuplas)

for item in lista_enum:
    print(item)

