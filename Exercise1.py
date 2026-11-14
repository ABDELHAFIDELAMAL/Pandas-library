import pandas as pd

df = pd.read_csv("employees.txt")

print("\nAfficher le nombre de lignes et de colonnes :")
print(df.shape)

print("\nAfficher les 3 premières lignes.")
print(df.head(3))

print("\nAfficher les 4 dernières lignes.")
print(df.tail(4))

print("\nAfficher uniquement la colonne Nom.")
print(df["Nom"])

print("\nCalculer le salaire moyen.")
print("moyenne = " , df["Salaire"].mean())

print("\nAfficher le salaire minimum et maximum.")
print("Salaire minimum = " , df["Salaire"].min())
print("Salaire maximum = " , df["Salaire"].max())

print("\nAfficher le nombre de valeurs non nulles dans chaque colonne.")
print(df.count())

print("\nAfficher le nombre de valeurs nulles dans chaque colonne.")
print(df.isnull().sum())

print("\nAfficher les statistiques générales du DataFrame.")
print(df.describe())

print("\nAfficher uniquement les employés dont l'âge est supérieur à 25 ans.")
print(df[df["Age"] > 25])

print("\nAfficher uniquement les employés qui habitent à Marrakech.")
print(df[df["Ville"] == "Marrakech"])

print("\nAfficher les employés dont le salaire est supérieur à 5 000 DH et l'âge supérieur à 25 ans.")
print(df[(df["Salaire"] > 5000) & (df["Age"] > 25)])

print("\nAfficher les employés qui habitent à Marrakech ou Casablanca")
print(df[(df["Ville"] == "Marrakech") | (df["Ville"] == "Casablanca")])

print("\nAfficher les employés dont le salaire est compris entre 5 000 et 10 000 DH inclus.")
print(df[(df["Salaire"] > 5000) & (df["Salaire"] < 10000)])

print("\nAfficher les employés dont le nom commence par la lettre A.")
print(df[df["Nom"].str.startswith("A")])

print("\nAfficher les employés dont le téléphone est manquant (NaN).")
print(df[df["Téléphone"].isnull()])

print("\nCalculer le salaire moyen des employés de Marrakech.")
print("Moyenne =", df[df["Ville"] == "Marrakech"]["Salaire"].mean())

print("\nCalculer le salaire moyen des employés âgés de plus de 25 ans.")
print("Salaire moyen = " , df[df["Age"] > 25]["Salaire"].mean())

print("\nCalculer la somme totale des salaires.")
print("Somme total = " , df["Salaire"].sum())

print("\nTrouver l'employé qui possède le salaire le plus élevé.")
print(df[ df["Salaire"] == df["Salaire"].max() ])

print("\nCalculer le nombre d'employés dans chaque ville.")
print(df["Ville"].value_counts())
