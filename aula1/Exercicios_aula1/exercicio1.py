import pandas as pd
import matplotlib.pyplot as plt
dados = {
    "tempo": ["08:00", "09:00", "10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00"],
    "temperatura": [25, 28, 32,35,38,42,45,41,37,33]
}
df = pd.DataFrame(dados)
df.plot(
    x="tempo",
    y="temperatura",
    kind="line",
    legend=True
)
plt.title("Temperatura por tempo")
plt.ylabel("Temperatura (°C)")
plt.show()

# a) Em qual horário foi registrada a maior temperatura?
idx_max = df["temperatura"].idxmax()
print("a) Maior temperatura:", df.loc[idx_max, "temperatura"], "°C às", df.loc[idx_max, "tempo"])

# b) Qual foi a menor temperatura registrada?
print("b) Menor temperatura:", df["temperatura"].min(), "°C")

# c) Em qual intervalo ocorreu a maior elevação de temperatura?
df["variacao"] = df["temperatura"].diff()
maior = df["variacao"].max()
for i in df[df["variacao"] == maior].index:
    print(f"c) Maior elevação: +{maior:.0f} °C entre {df.loc[i-1, 'tempo']} e {df.loc[i, 'tempo']}")

# d) Temperatura média usando df["temperatura"].mean()
print(f"d) Temperatura média: {df['temperatura'].mean():.1f} °C")
