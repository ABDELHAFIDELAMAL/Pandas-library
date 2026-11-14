import pandas as pd

table = df = pd.read_csv('employees.txt')

# affiche première ligne
print(table.head(1))
# affiche dernière ligne
print(table.tail(1))
# affiche la moyenne d'une ligne
print(table["Salaire"].mean())
# affiche maximum d'une ligne
print(table["Salaire"].max())
# affiche minimum d'une ligne
print(table["Salaire"].min())
# Affiche le nombre de valeurs non nulles
print(table.count())

print(table["Nom"])
print(table.shape)
print(table.isnull().sum())



#➢ df.shape : donne le nombre des lignes et des colonnes du dataframe
#➢ df.info() :donne le type de donnée
#➢ df.describe() :donne une vue statistique d’ensemble
#➢ df.head(n): afficher les n premiers éléments du dataframe
#➢ df.tail() affiche les n derniers éléments du dataframe
#➢ df.mean() : donne la moyenne de chaque colonnes
#➢ df.std() : retourne une division standard de chaque colonnes
#➢ df.min() :valeurs minimale de chaque colonnes
#➢ df.max(): valeurs maximale de chaque colonnes
# df.count() :affiche le nombre de valeurs non nulles
#➢ df[col_name] : affiche une colonne particulière