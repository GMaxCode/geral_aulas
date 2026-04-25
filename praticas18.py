# FUNÇÕES

def converter_para_celsius(fahrenheit):
    # O que vem aqui dentro? a conta para converter de fahrenheit para celsius
    resultado = (fahrenheit - 32) / 1.8
    return resultado

# Como você usaria a função para converter 100 graus Fahrenheit?
meu_resultado = converter_para_celsius(100)
print(f"{meu_resultado:.2f}")