import pandas as pd

notas = pd.read_csv('ratings.csv')

notas.columns = ["usuarioId", "filmeId", "nota", "momento"]

notas['nota']

notas['nota'].value_counts()

notas['nota'].mean()