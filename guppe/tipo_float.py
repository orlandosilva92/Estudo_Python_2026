"""
Tipo Float
Tipo real, decimal
Casas decimais
Obs.: Separador é o ponto não a vírgula
"""
valor = 1.44
print(valor)
print(type(valor))
print(dir(valor))

#Dupla atribuição
valor2, valor3 = 1.34, 1.12
print(valor2)
print(valor3)

#Pegando um valor Float e saindo valor inteiro
#Ao converter valores Float para inteiro perdemos precisão
res = int(valor2)
print(res)


