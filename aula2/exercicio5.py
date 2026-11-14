combustivel = input ('Qual combustível?')
volume = float(input ('Quantos litros?'))

if combustivel == "etanol" and volume >= 15  : custo = (volume * 1.7 * 0.96)
elif combustivel == "etanol" and volume < 15 : custo = (volume * 1.7 * 0.97)
elif combustivel == "diesel" and volume >= 15 : custo = (volume * 2 * 0.95 )
elif combustivel == "diesel" and volume < 15 : custo = (volume * 2 * 0.97)
elif combustivel == "gasolina" and volume >= 20 : custo = (volume * 4.5 * 0.97)
else : custo = (volume * 4.5)
print (f'O preço total ficou R$ {custo}')





