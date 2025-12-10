import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("books.csv")

os.makedirs("images", exist_ok=True)

# Clean Price column
df["Price"] = df["Price"].astype(str).str.replace(r"[^\d\.]", "", regex=True)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# 1. Price Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Price"].dropna(), bins=10)
plt.title("Price Distribution of Books")
plt.xlabel("Price (£)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("images/price_distribution.png")
plt.close()

# 2. Top 10 Expensive Books
top10 = df.sort_values("Price", ascending=False).head(10)
plt.figure(figsize=(10,6))
plt.barh(top10["Title"], top10["Price"])
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.tight_layout()
plt.savefig("images/top10_price.png")
plt.close()

print("Visualizations created in images/ folder!")
