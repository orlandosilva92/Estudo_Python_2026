#1. Faça um programa que leia um número inteiro e imprima-o.
#Formato para solicitar ao usuário que digite algo na tela
#obs.: Nesse formato é que o "Input" retorna uma string, então é necessário transformar a string em int com o cast
numero: int = int(input("Informe um número: "))
print(numero)

#2. Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.
numero1: int = int(input("Informe o primeiro número: "))#cast
numero2: int = int(input("Informe o segundo número: "))#cast
numero3: int = int(input("Informe o terceiro número: "))#cast
soma: int = numero1 + numero2 + numero3
#para concatenar dentro do print usa-se a chave {} e para mostrar que vai haver concatenação entre int e string
#é usado a letra "f" antes das aspas simples dentro do print
print(f'A soma dos números {numero1} e {numero2} e {numero3} é igual a {soma}')

#3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.
numero1: int = int(input("Informe o primeiro número: "))#cast
numero2: int = int(input("Informe o segundo número: "))#cast
numero3: int = int(input("Informe o terceiro número: "))#cast
numero1 = numero1 * numero1
numero2 = numero2 * numero2
numero3 = numero3 * numero3
soma: int = numero1 + numero2 + numero3
print(f'A soma dos números {numero1} e {numero2} e {numero3} elevado ao quadrado é igual a {soma}')