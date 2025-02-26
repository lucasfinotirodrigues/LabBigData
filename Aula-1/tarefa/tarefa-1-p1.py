import pandas as pd
import random 

idades = [random.randrange(0,101) for idade in range(0,1000)]
idades_maiores_21 = pd.Series([idade for idade in idades if idade >= 21])
media_idades_maiores_21 = round(idades_maiores_21.mean())
idade_pd = pd.Series(idades)
mean = round(idade_pd.mean())
median = round(idade_pd.median())
mode = idade_pd.mode().values[0] 

print("Média ==> ", mean)
print("Mediana ==> ", median)
print("Moda ==> ", mode)
    
idades = [media_idades_maiores_21 if idade < 21 else idade for idade in idades]

print(idades)