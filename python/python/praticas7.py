#calculadora simples
#digite um número e um operador ( *, +, %)

num = int(input('digite um número: '))
num2 = int(input('digite outro número: '))
operador = str(input('digite um operador entre esses >> +,x,/ : '))

if operador == "+":
    print(f'{num} + {num2} = {num + num2}')

if operador == '*':
    print(f'{num} x {num2} = {num * num2}')

if operador == '%':
    print(f'{num} x {num2} = {num / num2}')




