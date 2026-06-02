frase = "java até que é bom mas prefiro python"

i = 0
numero_apareceu = 0
letrada_vez = ''
while i < len(frase):
    letra = frase[i]
    
    i += 1
    if letra == ' ':
        continue
    
    num = frase.count(letra)
    
    if numero_apareceu < num:
        numero_apareceu= num
        letrada_vez = letra
print(f'a letra que mais aperceu foi {letrada_vez} que apareceu {numero_apareceu}')  