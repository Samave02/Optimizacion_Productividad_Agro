 Análisis de Datos Ambientales y Agrícolas con CRISP-DM

Este proyecto aplica la metodología CRISP-DM para el análisis de datos relacionados con **precipitación**, **productos agroquímicos** y otras variables relevantes para el monitoreo y mejora de las prácticas agrícolas en Colombia.

## Estructura del Proyecto

- `data/`: Conjuntos de datos utilizados (originales y limpios)
- `notebooks/`: Jupyter Notebooks con análisis exploratorio, preparación y modelado
- `src/`: Scripts en Python para limpieza, transformación y visualización
- `outputs/`: Gráficos, resultados, modelos entrenados

## Objetivo General

Evaluar la efectividad de las técnicas de machine learning (ML) en la mejora de la productividad agrícola en Boyacá.

## Herramientas Utilizadas

- Python (Pandas, Matplotlib, Scikit-learn, Seaborn)
- Jupyter Notebooks
- Git y GitHub
- Metodología CRISP-DM

## Fases CRISP-DM Implementadas

1. **Comprensión del Negocio**  
   El objetivo general del proyecto es evaluar la efectividad de los modelos de ML en la predicción y en la optimización de la productividad agrícola. Para esto, se definió los siguientes objetivos:

    - Implementar modelos de machine learning para predecir la productividad agrícola y detectar factores limitantes, como problemas de suelo o riesgos climáticos, considerando condiciones agroclimáticas de Boyacá.
    - Interpretar los resultados del sistema de optimización y ajustar las recomendaciones basadas en las condiciones específicas de cada zona agrícola de Boyacá.
    - Analizar el impacto de las recomendaciones generadas por los modelos en la toma de decisiones de los agricultores y su efectividad en la mejora de la productividad agrícola.


2. **Comprensión de los Datos**  
   En el proceso de recopilación de datos, luego de revisar fuentes bibliográficas, se optó por trabajar con información relacionada con **Agricultura y Desarrollo Rural**, y datos provenientes de **redes meteorológicas**, tales como:

- Temperatura mínima del aire  
- Velocidad del viento  
- Precipitaciones

Las fuentes utilizadas fueron:

- [IDEAM](http://dhime.ideam.gov.co/webgis/home/) (*Instituto de Hidrología, Meteorología y Estudios Ambientales*), mediante la plataforma de **Datos Abiertos Colombia**.  
- [Agronet](https://www.agronet.gov.co/Paginas/inicio.aspx), portal del **Ministerio de Agricultura y Desarrollo Rural**.

3. **Preparación de los Datos**
  - `Limpieza de datos/`: Conjuntos de datos utilizados en cada uno de los procesos.
5. **Modelado**  
   - `Modelado/` :selección y aplicación de varias técnicas de modelado.
6. **Evaluación**  
   - En desarrollo

## Fuentes de Datos

- [Datos IDEAM - Precipitación](http://www.ideam.gov.co)
- [Datos VECOL - Agroquímicos](https://www.datos.gov.co/d/y2zk-c694)
