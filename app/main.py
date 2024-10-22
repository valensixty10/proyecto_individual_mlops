import pandas as pd

# Ruta a los datasets
dataset_1 = pd.read_csv(r'data\raw\credits.csv')
dataset_2 = pd.read_csv(r'data\raw\movies_dataset.csv')

# Si los archivos son muy grandes y CSV, puedes leer por chunks
chunk_size = 10000
for chunk in pd.read_csv(r'data\raw\credits.csv', chunksize=chunk_size):
    # Procesa el chunk
    print(chunk.head())