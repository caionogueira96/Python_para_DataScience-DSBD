preço1 = float (input (f'Preço médio do Nissan Kicks em 2024:').replace(",","."))
preço2 = float (input (f'Preço médio do Nissan Kicks em 2025:').replace(",","."))
preço3 = float (input (f'Preço médio do Nissan Kicks em 2026:').replace(",","."))

if preço1 > preço2 and preço1 > preço3 : print (f'O preço mais alto do Nissan Kicks foi em 2024, custando R${preço1}')
elif preço2 > preço1 and preço2 > preço3 : print (f'O preço mais alto do Nissan Kicks foi em 2025, custando R${preço2}')
else : print (f'O preço mais alto do Nissan Kicks foi em 2026, custando R${preço3}')

if preço1 < preço2 and preço1 < preço3 : print (f'O preço mais baixo do Nissan Kicks foi em 2024, custando R${preço1}')
elif preço2 < preço1 and preço2 < preço3 : print (f'O preço mais baixo do Nissan Kicks foi em 2025, custando R${preço2}')
else : print (f'O preço mais baixo do Nissan Kicks foi em 2026, custando R${preço3}')

