import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# PASO 1: CARGAR LOS DATOS
# =====================================================================
# pd.read_csv toma el archivo y lo transforma instantáneamente en un "DataFrame"
# (una tabla inteligente de Pandas altamente optimizada).
print("Cargando el archivo... Por favor espera.")
df = pd.read_csv('owid-covid-data.csv')
print("¡Archivo cargado con éxito!\n")


# =====================================================================
# PASO 2: INSPECCIONAR LA ESTRUCTURA (Exploración inicial)
# =====================================================================
# .shape nos dice cuántas filas y columnas tiene el archivo en total.
print(f"El dataset contiene {df.shape[0]} filas y {df.shape[1]} columnas.")

# .head() nos muestra las primeras 5 filas para entender qué tipo de datos hay.
print("\nVista rápida de las primeras filas:")
print(df[['continent', 'location', 'date', 'total_cases', 'new_cases']].head())


# =====================================================================
# PASO 3: FILTRAR Y LIMPIAR (Aquí reducimos el monstruo a algo manejable)
# =====================================================================
# El archivo tiene datos de todo el mundo. Vamos a aislar únicamente los datos de México.
filtro_pais = df['location'] == 'Mexico'
df_mexico = df[filtro_pais].copy()

# Convertimos la columna de fecha a un formato que Python entienda cronológicamente
df_mexico['date'] = pd.to_datetime(df_mexico['date'])

# Tratamiento de valores nulos (NumPy + Pandas):
# Si en algunos días antiguos no se registraron casos nuevos, aparecerá como "NaN" (Nulo).
# Usamos .fillna() para convertir esos nulos en 0 y no alterar los cálculos matemáticos.
df_mexico['new_cases'] = df_mexico['new_cases'].fillna(0)


# =====================================================================
# PASO 4: ANALIZAR Y EXTRAER VALOR (Pandas avanzado pero simple)
# =====================================================================
# Vamos a ordenar los datos para descubrir cuáles fueron los 3 días con más contagios registrados.
dias_pico = df_mexico.sort_values(by='new_cases', ascending=False).head(3)

print("\n--- Los 3 días con más casos nuevos registrados en México ---")
print(dias_pico[['date', 'new_cases']])


# =====================================================================
# PASO 5: VISUALIZAR EL IMPACTO (Matplotlib)
# =====================================================================
# Tomamos nuestra tabla filtrada de México y graficamos la evolución temporal.
plt.figure(figsize=(10, 6))


# Dibujamos la línea de casos totales
# plt.plot(df_mexico['date'], df_mexico['total_cases'], color='#8B0000', linewidth=2.5, label='Casos Totales')



plt.hist(df_mexico['new_cases'], bins=30 , color='royalblue', edgecolor='black', alpha=0.7)
plt.title("Evolución Acumulada de Casos de COVID-19 en México", fontsize=16, fontweight='bold')
plt.xlabel("Línea de Tiempo (Años)", fontsize=12)
plt.ylabel("Número de Personas (Millones)", fontsize=12)

plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Estilizado profesional del gráfico
# plt.title('Evolución Acumulada de Casos de COVID-19 en México', fontsize=14, fontweight='bold', pad=15)
# plt.xlabel('Línea de Tiempo (Años)', fontsize=12)
# plt.ylabel('Número de Personas (Millones)', fontsize=12)
# plt.grid(True, linestyle='--', alpha=0.5) # Cuadrícula de fondo tenue
# plt.legend(loc='upper left')

# Ajusta los márgenes automáticamente para que no se corte el texto
plt.tight_layout()

# Desplegar gráfico
# plt.show()