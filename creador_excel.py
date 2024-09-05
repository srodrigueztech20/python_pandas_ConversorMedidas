import pandas as pd

# Dalaframe informacion básica para armar el Excel

data = {
    "Piezas" : ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centimetros" : [40,120,60,30,180]}

df = pd.DataFrame(data)

# Guardar el Dataframe en un archivo Excel

df.to_excel("muebles_medidas.xlsx", index=False)