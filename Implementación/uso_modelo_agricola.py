# uso_modelo_agricola.py
"""
Script de ejemplo para cargar el modelo de productividad agrícola y realizar una predicción con datos de usuario.

Requisitos:
- modelo_random_forest.joblib
- scaler.joblib
- pca.joblib

Coloca este script en la misma carpeta donde están los archivos del modelo o ajusta las rutas.
"""
import joblib
import pandas as pd

# Cargar los archivos generados
rf_model = joblib.load('modelo_random_forest.joblib')
scaler = joblib.load('scaler.joblib')
pca = joblib.load('pca.joblib')

# Definir los datos de entrada EXACTAMENTE con los nombres y orden de las columnas de X
# Puedes modificar los valores según el caso real
entrada_usuario = {
    'Anio': [2025],
    'areaSembradaHa': [2.5],
    'areaCosechadaHa': [2.5],
    'produccionTon': [7.0],
    'CicloPermanente': [0],
    'CicloTransitorio': [1],
    'GpCereales': [0],
    'grupoCultivo_Cultivos para condimentos, bebidas medicinales y aromáticas': [0],
    'grupoCultivo_Cultivos tropicales tradicionales': [0],
    'GpFrutales': [1],
    'GpHortalizas': [0],
    'GpLeguminosas': [0],
    'GpOleaginosas': [0],
    'grupoCultivo_Raíces y tubérculos': [0],
    'Boyaca': [1],
    'EdoCañaVerde': [0],
    'Edofresco': [0],
    'EdoFibraCabuya': [0],
    'EdoGrano': [0],
    'EdoGranoSeco': [0],
    'EdoPaddyCascaraVerde': [0],
    'EdoSecoTrilla': [0],
    'Periodo_A': [0],
    'Periodo_B': [1],
    'Periodo_C': [0]
}

X_usuario = pd.DataFrame(entrada_usuario)

# Estandarizar y aplicar PCA
datos_scaled = scaler.transform(X_usuario)
datos_pca = pca.transform(datos_scaled)

# Realizar la predicción
prediccion = rf_model.predict(datos_pca)
print(f'Predicción de rendimiento (ton/ha): {prediccion[0]:.2f}')