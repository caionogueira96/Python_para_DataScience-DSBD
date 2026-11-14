import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "cliente": ["C1", "C2", "C3", "C4", "C5",
                "C6", "C7", "C8", "C9", "C10"],
    "setor": ["Tecnologia", "Indústria", "Comércio",
              "Tecnologia", "Indústria", "Comércio",
              "Tecnologia", "Indústria", "Comércio",
              "Tecnologia"],
    "vendas": [1500, 2500, 1200, 3000, 4500,
               2000, 3500, 5000, 2800, 4000]
}
df = pd.DataFrame(dados)
print(df)
print()

# Faturamento total por setor (equivalente a uma tabela dinâmica)
fat_setor = df.groupby("setor")["vendas"].sum().sort_values(ascending=False)
print("Faturamento total por setor:")
print(fat_setor)
print()

# a) Setor com maior faturamento (considerando empates)
maior = fat_setor.max()
print("a) Maior faturamento:", ", ".join(fat_setor[fat_setor == maior].index), f"(R$ {maior})")

# b) Setor com menor faturamento
menor = fat_setor.min()
print("b) Menor faturamento:", ", ".join(fat_setor[fat_setor == menor].index), f"(R$ {menor})")

# c) Cliente com a compra de maior valor
idx = df["vendas"].idxmax()
print("c) Maior compra:", df.loc[idx, "cliente"], f"(R$ {df.loc[idx, 'vendas']}, setor {df.loc[idx, 'setor']})")

# d) Faturamento total da empresa
print("d) Faturamento total da empresa: R$", df["vendas"].sum())
print()

# e) Média das vendas por setor
print("e) Média das vendas por setor:")
print(df.groupby("setor")["vendas"].mean())

# Gráfico de barras: faturamento total por setor
fat_setor.plot(kind="bar", color="steelblue")
plt.title("Faturamento total por setor")
plt.xlabel("Setor")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()