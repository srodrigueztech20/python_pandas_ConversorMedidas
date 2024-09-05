import pandas as pd

def centimetros_pulgadas(cm):
    return cm/2.54

# Leer el archivo Excel

df = pd.read_excel("muebles_medidas.xlsx")

# Añadir una copumna al Dataframe de Pulgadas

df["Pulgadas"] = df["Centimetros"].apply(centimetros_pulgadas)

df.to_excel("muebles_medidas_convertidas.xlsx", index=False)

print("Conversión completada y guardada en un archivo Excel")