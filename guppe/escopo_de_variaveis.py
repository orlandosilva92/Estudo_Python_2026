"""
Escopo de variáveis

Dois casos de escopo:

1- Variáveis globais
    -São reconhecidas, ou seja, seu escopo compreende todo o programa.

2- Variáveis locais
    -São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo esta limitado ao bloco onde foi
    declarada.

Para declara variáveis em python, fazermos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos
o tipo de dado dela, esse tipo é inferido ao atribuírmos o valor a mesma.

Exemplo em C:
int numero = 33;

Exemplo em Java:
int numero = 33;
"""
numero = 33
print(numero)
print(type(numero))#"<class 'int'>"

numero = "geek"
print(numero)
print(type(numero))#<class 'str'>

numero = 42
#novo = 0

if(numero > 10):
    novo = numero + 10 # A variável 'novo' está declarada localmente ddentro do bloco if. Portanto, é local
    print(novo)
print(novo)