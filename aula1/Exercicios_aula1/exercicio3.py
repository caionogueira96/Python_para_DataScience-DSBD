import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "dia": ["D1", "D2", "D3", "D4", "D5",
            "D6", "D7", "D8", "D9", "D10"],
    "preco": [25.50, 26.20, 25.80, 27.00, 28.50,
              27.80, 29.20, 30.50, 29.80, 31.00]
}

df = pd.DataFrame(dados)
df["variacao"] = df["preco"].diff()   # diferença em relação ao dia anterior
print(df)
print()

# a) Maior preço
idx_max = df["preco"].idxmax()
print(f"a) Maior preço: R$ {df.loc[idx_max, 'preco']:.2f} no dia {df.loc[idx_max, 'dia']}")

# b) Menor preço
idx_min = df["preco"].idxmin()
print(f"b) Menor preço: R$ {df.loc[idx_min, 'preco']:.2f} no dia {df.loc[idx_min, 'dia']}")

# c) Dias com queda (variação negativa)
quedas = df[df["variacao"] < 0]
print("c) Dias com queda:")
for i in quedas.index:
    print(f"   {df.loc[i, 'dia']}: R$ {df.loc[i-1, 'preco']:.2f} -> R$ {df.loc[i, 'preco']:.2f} ({df.loc[i, 'variacao']:+.2f})")

# d) Média dos preços
print(f"d) Preço médio de fechamento: R$ {df['preco'].mean():.2f}")

# e) Lucro comprando 100 ações no D1 e vendendo no D10
quantidade = 100
compra = df["preco"].iloc[0]    # primeira linha
venda = df["preco"].iloc[-1]    # última linha
lucro = (venda - compra) * quantidade
print(f"e) Lucro: (R$ {venda:.2f} - R$ {compra:.2f}) x {quantidade} = R$ {lucro:.2f} ({(venda/compra-1)*100:.1f}%)")

# Gráfico de linhas, com as quedas destacadas em vermelho
plt.plot(df["dia"], df["preco"], marker="o", label="Preço de fechamento")
plt.scatter(quedas["dia"], quedas["preco"], color="red", zorder=3, label="Queda")
plt.title("Evolução do preço da ação")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("grafico_ex3.png")
plt.show(block=True)
input("Pressione Enter para encerrar...")
