''' 
iterável >> str, range , etc
iterador >> quem sabe entregar um valor por vez, usando: next() > me entrega o próximo valor
iter >> me entrega seu iterador

'''
# text = iter('python')

# print(next(text))
# print(next(text))

text = 'python'
for letra in text:
    print(letra)