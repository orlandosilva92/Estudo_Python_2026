"""
Estruturas condicionais
if (se), else, elif

Exemplo em C:
if(idade < 18){
    printf("Menor de idade");
}else if(idade == 18){
    printf("Tem 18 anos");
}else{
    printf("Maior de idade");
}

Exemplo em Java:
if(idade < 18){
    System.out.println("Menor de idade");
}else if(idade == 18){
    System.out.println("Tem 18 anos");
}else{
    System.out.println("Maior de idade");
}
"""
idade: int = int(input("Qual a sua idade? "))

if idade < 18:
    print(f'Você tem: {idade} anos. Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print(f'Você tem: {idade} anos. Maior de idade')


