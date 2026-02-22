"""
Tipo String

Em Python, um dado é considerado do tipo string, sempre que:

* Estiver entre àspas simples > 'uma string', '2312312', 'a', 'True', '42.3'
* Estiver entre àspas duplas > ""uma string", "2312312", "a", "True', "42.3"
* Estiver entre àspas simples triplas > '''uma string''','''234''', '''a''',....
"""
# * Estiver entre àspas duplas triplas > """uma string""", """234""",...

nome = 'jose orlando'
print(nome)
print(type(nome))

#Deixar tudo maiusculo
print(nome.upper())

#Deixar tudo minusculo
print(nome.lower())

#Pegas as palavras e colocar em uma lista(array de string)
#['jose', 'orlando']
print(nome.split())

#Mostra na tela as 4 primeiras posições da String contida em nome - Slice de string
print(nome[0:4])
print(nome[5:12])

#Aqui foi pego pelo split as 2 listas e chamadas conforme posição
#['jose', 'orlando']
print(nome.split()[0])
print(nome.split()[1])

#formato de inverter a string
#[::-1] >>> pega o primeiro elemento ":", agora o ultimo elemento ":", e inverte "-1"
print(nome[::-1])

#Comando para substituir caracteres dentro da string
print(nome.replace('o','u'))

print(type(nome))