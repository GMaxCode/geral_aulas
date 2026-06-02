# DICIONARIO!!
frase = 'sempre fui de jogar futebol'
i = 0
dicionario = {}

while i < len(frase):
     a = frase[i]

     if a in dicionario:
        dicionario[a]+=1
     else:
        dicionario[a] = 1
     i += 1
print(dicionario)