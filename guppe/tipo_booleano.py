"""
Tipo Booleano
Algebra Booleana, criada por George Boole
2 constrantes: True, False

Obs.: Sempre com a inicial maiuscula

True, False
"""

user_Ativo = True
print(user_Ativo)

print(type(user_Ativo))

"""
Operações básicas
"""
#Negação - Not
"""
Fazendo a negação se o valor booleano for verdadeiro o resultado será falso
se for falso o resultado será verdadeiro, ou seja, sempre o inverso
"""
#Invertendo o valor do user_Ativo
print(not user_Ativo)

# ou - Or
"""
É uma operação binária, ou seja, depende de dois valores, ou um ou outro deve ser verdadeiro

True or True = True
True or False = True
False or False = False
False or True = True
"""
user_Inativo = False
print(user_Ativo or user_Inativo)
print(not user_Ativo or user_Inativo)

# E - And
"""
Também é uma operação binária, ou seja, depende de dois valores, ambos os valores de vem ser verdadeiros

True and True = True
True and False = False
False and False = False
False and True = False
"""

print(user_Inativo and user_Ativo)
print(not user_Inativo and user_Ativo)