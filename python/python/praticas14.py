#Dicionario
dados = {'hi':'oi',
         'bye':'tchau',
         'thanks': 'obrigado',
         'welcome':'bem vindo'
        }
digite =input('digite qual palavra deseja ser traduzida: ').lower()

if digite in dados:
    print(f'A tradução de {digite} é: {dados[digite]}')

else:
    print('digite outra palavra.')
