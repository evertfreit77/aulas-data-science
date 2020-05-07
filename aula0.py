import pandas as pd

notas = pd.read_csv('ratings.csv')

notas.columns = ["usuarioId", "filmeId", "nota", "momento"]

notas['nota']

notas['nota'].value_counts()

notas['nota'].mean()

notas.nota.plot()

notas.nota.plot(kind='hist')

print("Média",notas['nota'].mean())
print("Mediana",notas['nota'].median())

notas.nota.describe()

import seaborn as sns

sns.boxplot(notas.nota)