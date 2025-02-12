import pandas as pd
import random 

idades = [random.randrange(0,101) for idade in range(0,1000)]
print(len(idades))
idade_pd = pd.Series(idades)
mean = round(idade_pd.mean())
median = round(idade_pd.median())
mode = idade_pd.mode()

print("Média ==> ", mean)
print("Mediana ==> ", median)
print("Moda ==> ", mode)

idades = [mean if idade <= 21 else idade for idade in idades ]

# print(idades)