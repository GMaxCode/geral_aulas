# for x in produtos → chaves 
# produtos[x] → pega o valor 
# .values() → só valores
# .items() → chave + valor 

total= 0
produtos = {
        'maçã': 5.0,
        'pera': 6.8,
        'goiaba': 7.5
    }
for  valor in produtos.values():
    total += valor

print(total)
