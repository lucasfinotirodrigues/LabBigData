import pandas as pd
import random 

idades = [random.randrange(0,101) for idade in range(0,1000)]
print(len(idades))
idade_pd = pd.Series(idades)
mean = round(idade_pd.mean())
median = round(idade_pd.median())
std = round(idade_pd.std())

print("Média ==> ", mean)
print("Mediana ==> ", median)
print("Desvio Padrão ==> ", std)

idades = [mean if idade <= 21 else idade for idade in idades ]

print(idades)