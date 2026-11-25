import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('dados_vendas.csv')

# Exibir primeiras linhas
print("📄 Primeiros dados:")
print(df.head())

# Estatísticas básicas
print("\n📈 Estatísticas descritivas:")
print(df.describe())

# Gráfico de vendas
plt.figure(figsize=(8,5))
plt.plot(df['Mes'], df['Vendas'], marker='o', color='b')
plt.title("Vendas Mensais - 2024")
plt.xlabel("Mês")
plt.ylabel("Quantidade Vendida")
plt.grid(True)
plt.show()

# Insight simples
media = df['Vendas'].mean()
print(f"\n💡 Média de vendas: {media:.2f}")
if df['Vendas'].iloc[-1] > media:
    print("As vendas de Dezembro estão acima da média — ótimo desempenho!")
else:
    print("As vendas de Dezembro ficaram abaixo da média.")
