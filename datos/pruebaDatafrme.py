 
import pandas as pd

# Crear un DataFrama

data = {"Nombre":['Ana','Luis', 'Carlos'], "Edad":[23, 34, 20], "telefono":[312341, 43212, 34567]}

nombre = ['Ana','Luis', 'Carlos']
edad = [23, 34, 20]
telefono =[312341, 43212, 34567]

df = pd.DataFrame(data)

data2 = pd.DataFrame([nombre, edad, telefono])
print(df["Nombre"])
print (data2)

df.to_csv("salida.csv", index=False)