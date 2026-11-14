# Exemplo 1 - Tipos de variáveis 
num = 4 
print (type(num))
num2 = float(input("Digite um número: "))
print(f'Você digitou o número: {num2}')
print(f'A variável digitada é do tipo {type(num2)}')

#Tipos de prints com os tipos de dados 

#variável para armazenar o nome do aluno
nome_aluno = 'Rocky'
idade_aluno = 15 
media_aluno = 8.45 

print ('Nome do aluno %s, ele tem %d anos e sua média é %.2f.' %(nome_aluno,idade_aluno,media_aluno))
print ('Nome do aluno {}, ele tem {} anos e sua média é {}.' .format(nome_aluno,idade_aluno,media_aluno))
print (f'Nome do aluno {nome_aluno}, ele tem {idade_aluno} anos e sua média é {media_aluno:.2f}.')