preço1 = float (input (f'Qual o preço do sorvete?:').replace(",","."))
preço2 = float (input (f'Qual o preço do chocolate?:').replace(",","."))
preço3 = float (input (f'Qual o preço da torta?:').replace(",","."))

if preço1 < preço2 and preço1 < preço3 : print (f'O sorvete é o mais barato, custando R${preço1}')
elif preço2 < preço1 and preço2 < preço3 : print (f'O chocolate é o mais barato, custando R${preço2}')
else : print (f'A torata é a mais barata, custando R${preço3}')