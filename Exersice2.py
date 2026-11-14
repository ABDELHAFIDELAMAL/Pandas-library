import pandas as pd

df = pd.read_csv("etudiants_50.csv")

print(df[["Nom", "Prenom" , "Age" ,"Gender"]][df["Nom"].str.startswith("Ben")])
print(df.head(1))
print(df.isnull())
df.dropna()
print(df)



print("#" * 50)
print(df[["Nom", "Prenom" , "Age" ,"Gender"]].sort_values(by="Age"))