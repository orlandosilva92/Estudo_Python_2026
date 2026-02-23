'''
Estruturas lógicas: and(e), or(ou), not(não), is(é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Para o 'and' ser verdadeiro(True), ambos os valores precisam ser verdadeiros(True)
Para o 'or' ser verdadeiro(True), um dos valores precisam ser verdadeiros(True)
O 'not' inverte o valor ou nega o valor original. Se algo (x = True | not X = False)
'''
ativo = True
logado = True

#Utilizando o 'and'
if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa verificar sua conta. Entre em contato com o suporte.')

#Utilizando o 'or'
if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Entre em contato com o suporte.')

#Utilizando o 'not'
status = False
if not status:
    print('Você precisa verificar sua conta. Entre em contato com o suporte.')

'''
Utilizando o 'is'
O Operador == (Igualdade)
O '==' verifica se os valores contidos nas variáveis são iguais. Ele não se importa onde o objeto está na memória,
apenas se o conteúdo é o mesmo.
O 'is' verifica se duas variáveis apontam para o exato mesmo objeto na memória (o mesmo endereço). É como perguntar:
"Estes dois nomes referem-se à mesma pessoa?"
'''
if ativo:
    print('Você esta logado no sistema.')

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True (valores iguais)
print(x is y)  # False (objetos diferentes na memória)

'''
Observação:
Use sempre == para comparar valores (números, strings, listas).
Reserve o is apenas para comparar com None, True ou False.
'''
