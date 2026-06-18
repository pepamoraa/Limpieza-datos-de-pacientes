# Ejercicio Práctico: Limpieza y Manipulación de Datos Clínicos con Pandas

Este repositorio contiene la resolución de un caso práctico de análisis de datos enfocado en la gestión de información de pacientes en una clínica médica utilizando **Python**.

El objetivo principal es resolver una serie de requerimientos de negocio relacionados con la limpieza de texto, transformación de formatos y consolidación de bases de datos utilizando la librería **Pandas**.

## Contenido del Ejercicio
A lo largo del código se abordan y resuelven los siguientes puntos:
1. **Conversión de Divisas**: Cálculo de deudas de pesos chilenos a dólares mediante ciclos "for" con el uso del comando "iterrows".
2. **Manipulación de Textos**: Extracción de caracteres específicos, estandarización de nombres completos a letras mayúsculas y detección de caracteres específicos (como la letra Ñ).
3. **Limpieza de Datos Corruptos**: Eliminación de filas con información corrupta (registros marcados con "XXXX") aplicando dobles condiciones y filtros inversos (~).
4. **Reemplazo de Patrones**: Corrección de inconsistencias en nombres y fechas de nacimiento utilizando el comando "str.replace".
5. **Consolidación e Integración de Datos**: Combinación de múltiples DataFrames usando funciones esenciales de Pandas como "append", la separación de columnas de texto con "str.split", y uniones avanzadas de tablas mediante "join" y "merge" relacionando los datos a través del RUT.

## Requisitos para ejecutar
* Tener instalado Python 3.x
* Tener instalada la librería Pandas (pip install pandas)
* Contar con los archivos CSV en la misma carpeta raíz del script: "datos_pacientes.csv", "datos_pacientes2.csv" y "nacionalidad.csv".
