#primero que todo se llama al archivo y se agregan todos los comandos necesarios para su lectura
import pandas as pd

df_pacientes=pd.read_csv("datos_pacientes.csv", encoding="utf-8", sep=";")
df_pacientes2=pd.read_csv("datos_pacientes2.csv", encoding="utf-8", sep=";")
df_nacionalidad=pd.read_csv("nacionalidad.csv", encoding="utf-8", sep=";")
print(df_pacientes)

df_pacientes["Nombre"]= df_pacientes["Nombre"].str.upper()
print(df_pacientes.head())


print(df_pacientes.loc[df_pacientes["Nombre"].str.contains("Ñ")])

print(df_pacientes2)

df_pacientes2= df_pacientes2.loc[~(df_pacientes2["RUT"].str.contains("XXXX")) & ~(df_pacientes2["Nombre"].str.contains("XXXX"))]
print(df_pacientes)

df_pacientes2["Nombre"]= df_pacientes2["Nombre"].str.replace("-"," ")
print(df_pacientes2)

print(df_pacientes2["Fecha_Nacimiento"])
df_pacientes2["Fecha_Nacimiento"]= df_pacientes["Fecha_Nacimiento"].str.replace("_/","/")
print(df_pacientes2["Fecha_Nacimiento"])


df_pacientes= df_pacientes.append(df_pacientes2)
print(df_pacientes)

df_pacientes= df_pacientes.set_index("RUT")
print(df_pacientes)

df_separado= df_pacientes["Nombre"].str.split(" ",expand=True)
df_separado.columns=["Primer_Nombre","Segundo_Nombre","Primer_Apellido","Segundo_Apellido"]
print(df_separado)


df_pacientes= df_pacientes.join(df_separado)
print(df_pacientes)

print(df_nacionalidad)

df_pacientes= df_pacientes.merge(df_nacionalidad, left_on="RUT", right_on="RUT", how="left")
print(df_pacientes.dtypes)
print(df_pacientes)

