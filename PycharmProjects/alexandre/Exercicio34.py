n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
oper = input("Digite Soma para somar, Sub para subtrair, Mult para Div para Dividir os Números:  ")
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1/ n2
rest = n1%n2

if oper == 'Soma':
        elif soma > 0 and soma/2 == 0 and rest == 0:
            print(f'O resultado é {soma} e o número é positivo, par e inteiro ')
        elif soma > 0 and soma/2 != 0 and rest == 0:
            print(f'O resultado é {soma} e o número é positivo, ímpar e inteiro ')
        elif soma > 0 and soma/2 == 0 and rest != 0:
            print(f'O resultado é {soma} e o número é positivo, par e decimal ')
        elif soma > 0 and soma/2 != 0 and rest != 0:
            print(f'O resultado é {soma} e o número é positivo, ímpar e decimal ')

        elif soma < 0 and soma/2 == 0 and rest == 0:
            print(f'O resultado é {soma} e o número é negativo, par e inteiro ')
        elif soma < 0 and soma/2 != 0 and rest == 0:
            print(f'O resultado é {soma} e o número é negativo, ímpar e inteiro ')
        elif soma < 0 and soma/2 == 0 and rest != 0:
            print(f'O resultado é {soma} e o número é negativo, par e decimal ')
        elif soma < 0 and soma/2 != 0 and rest != 0:
            print(f'O resultado é {soma} e o número é negativo, ímpar e decimal ')
        else:
            print("O resultado da soma é Zero.")



