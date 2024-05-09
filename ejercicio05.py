import pandas as pd
import requests

df = pd.read_csv('frases.csv', header=None)

for index, row in df.iterrows():
    frase = row[0]
    url = f"http://127.0.0.1:8080/prediccion/{frase}"
    response = requests.get(url)

    prediction = response.json()['prediction']

    print(f"Frase: {frase} - Predicción: {prediction}")