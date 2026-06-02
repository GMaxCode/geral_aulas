import pandas as pd

# Leitura direta com detecção automática de tipos
df = pd.read_csv('dados_csv/vendas.csv')

# Vetorização: criando coluna com cálculo automático
df['subtotal'] = df['preco'] * df['quantidade']

print("--- RELATÓRIO COM PANDAS ---")
print(df)

# Agregação simplificada
total_geral = df['subtotal'].sum()
print(f"\nTOTAL EM ESTOQUE: R$ {total_geral:.2f}")