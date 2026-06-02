# FUNÇÕES
valor = float(input('digite o valor da divida: '))
def cal_impost(valor): 
    imposto = valor < 100 * 0.01 
    if imposto < 500 * 0.05:

     if imposto < 1000 * 0.10:

      return imposto

resultado = cal_impost(valor)
     
print(f'o valor do imposto é {resultado} ')


    
    

