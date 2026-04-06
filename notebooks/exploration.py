import pandas as pd

df = pd.read_csv("data/patients_dakar.csv")

print("Nombre de patients :", len(df))
print("Colonnes :", df.columns)

print("\n--- Aperçu ---")
print(df.head())

print("\n--- Statistiques ---")
print(df.describe())

print("\n--- Diagnostics ---")
print(df["diagnostic"].value_counts())

print("\n--- Température moyenne ---")
print(df.groupby("diagnostic")["temperature"].mean())
import pandas as pd

df = pd.read_csv("data/patients_dakar.csv")

print("Nombre de patients :", len(df))
print("Colonnes :", df.columns)

print("\n--- Aperçu ---")
print(df.head())

print("\n--- Statistiques ---")
print(df.describe())

print("\n--- Diagnostics ---")
print(df["diagnostic"].value_counts())

print("\n--- Température moyenne ---")
print(df.groupby("diagnostic")["temperature"].mean())

print("\n--- Diagnostic  la plus fréquente ---")
print(df["diagnostic"].value_counts().idxmax())