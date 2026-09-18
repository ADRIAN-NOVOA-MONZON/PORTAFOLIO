# CallMeMaybe Detección de Operadores Ineficaces

## Descripción del proyecto

CallMeMaybe, un servicio de telefonía virtual, busca desarrollar una metodología para identificar operadores con desempeño inferior al esperado dentro de su sistema de atención telefónica. El análisis utiliza registros históricos de llamadas para evaluar indicadores relacionados con llamadas perdidas, tiempos de espera y actividad de llamadas salientes.

## Objetivo

Identificar operadores potencialmente ineficaces mediante el análisis de su desempeño operativo y establecer criterios objetivos que permitan diferenciar comportamientos de desempeño esperado e inferior al esperado.

## Datos

El proyecto utiliza dos conjuntos de datos:

- `telecom_dataset_new.csv`: registros de llamadas, con información sobre cliente, fecha, dirección de la llamada, tipo de llamada, operador, llamadas perdidas, cantidad de llamadas, duración y duración total.
- `telecom_clients.csv`: información de los clientes, incluyendo tarifa y fecha de inicio.

Los datos fueron integrados mediante `user_id` para incorporar la información del cliente al análisis de llamadas.

## Metodología

1. Exploración y validación inicial de los datos.
2. Tratamiento de fechas y eliminación de duplicados exactos.
3. Integración de los datasets.
4. Creación de métricas de tiempo de espera y duración promedio de llamada.
5. Análisis exploratorio de la distribución de llamadas, duración, tiempos de espera y comportamiento temporal.
6. Definición de métricas y criterios de desempeño mediante percentiles.
7. Clasificación de operadores según las métricas aplicables a su función.
8. Evaluación estadística de las diferencias entre grupos mediante pruebas de normalidad y Mann–Whitney U.
9. Preparación de los datos para visualización en Tableau.
10. Desarrollo de un dashboard para consultar los principales indicadores de desempeño.

## Herramientas utilizadas

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- Tableau

## Hallazgos clave

- El **45.6 %** de los operadores presentó algún nivel de desempeño inferior al esperado, frente a un **54.4 %** clasificado con desempeño esperado.
- Entre los operadores con desempeño inferior al esperado predominó la categoría de **Desempeño Bajo (61.24 %)**, seguida de **Desempeño Deficiente (38.35 %)**; dos operadores (**0.40 %**) fueron clasificados con **Desempeño Crítico**.
- En operadores especializados en llamadas entrantes, el **71.43 %** de los casos con desempeño inferior al esperado incumplió el criterio de tiempo promedio de espera, frente al **41.76 %** que incumplió el criterio de tasa de llamadas perdidas.
- La tasa de llamadas perdidas y el tiempo promedio de espera presentaron diferencias estadísticamente significativas entre los grupos comparados mediante la prueba de Mann–Whitney U, con un nivel de significancia de **α = 0.05**.
- La actividad de llamadas salientes presentó una alta dispersión, por lo que su interpretación se realizó considerando el tipo de operador y sus responsabilidades operativas.

## Recomendaciones

- Priorizar el seguimiento de operadores clasificados con **Desempeño Deficiente** y **Crítico**.
- Analizar los casos con tiempos de espera elevados considerando la carga operativa y los periodos de mayor demanda.
- Revisar la distribución de la carga de trabajo entre operadores para complementar la evaluación individual de desempeño.
- Utilizar el dashboard para facilitar el seguimiento de los indicadores y detectar áreas de oportunidad.

## Visualización / Dashboard

El análisis fue complementado con un dashboard interactivo desarrollado en Tableau.

**[Ver dashboard en Tableau Public](https://public.tableau.com/views/DASH_17870968103470/Dashboard1?:language=es-ES&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**

## Estructura del repositorio

```text
CallMeMaybe/
├── CallMeMaybe Detección de Operadores Ineficaces.ipynb
├── telecom_clients.csv
├── telecom_dataset_new.csv
├── telecom_data_tableau.csv
├── Presentación Proyecto Final CallMeMaybe.pptx
└── README.md
```

- `CallMeMaybe.ipynb`: Notebook del desarrollo completo del análisis.
- `telecom_clients.csv`: Datos de clientes.
- `telecom_dataset_new.csv`: Datos de llamadas utilizados en el análisis.
- `telecom_data_tableau.csv`: Dataset preparado para el dashboard.
- `Presentación Proyecto Final CallMeMaybe.pptx`: Presentación del desarrollo del proyecto y sus resultados.

## Reproducción del análisis

1. Clonar o descargar el repositorio.
2. Abrir `CallMeMaybe.ipynb` en Jupyter Notebook o un entorno compatible.
3. Mantener los archivos CSV en las rutas utilizadas por el notebook.
4. Ejecutar las celdas en orden para reproducir el análisis.

### Fuentes de referencia

Durante el desarrollo se consultó documentación oficial de las principales librerías utilizadas:

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)

## Autor
**Adrian Novoa Monzón**  
Data Analyst en Formación – TripleTen

## Datos de contacto

- **CV:** <a href="https://github.com/ADRIAN-NOVOA-MONZON/PORTAFOLIO/blob/main/CV%20ADRIAN%20NOVOA%20DATA%20ANALYST.pdf" target="_blank" rel="noopener noreferrer">PDF</a>
- **LinkedIn:** [adrian-novoa-monzon](https://www.linkedin.com/in/adrian-novoa-monzon)
- **Email:** [adrian-novoa-monzon@gmail.com](mailto:adrian-novoa-monzon@gmail.com)
