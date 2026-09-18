# Análisis de marketing, rendimiento y rentabilidad

Análisis exploratorio de un servicio digital para comprender el comportamiento de sus usuarios, las ventas y la eficiencia del gasto de marketing. El proyecto relaciona visitas, pedidos y costos para examinar la conversión por cohorte y canal, el valor de compra y las métricas de adquisición y retorno.

## Objetivo

Identificar patrones de uso y compra, comparar los resultados de las fuentes de adquisición y aportar evidencia para revisar la distribución del presupuesto de marketing.

## Datos y metodología

Se utilizan tres archivos CSV incluidos en el repositorio:

| Archivo | Contenido |
| --- | --- |
| `visits_log_us.csv` | Sesiones, dispositivos, marcas de tiempo y fuentes de adquisición. |
| `orders_log_us.csv` | Fechas e ingresos de los pedidos. |
| `costs_us.csv` | Gastos diarios por fuente de marketing. |

El notebook comprende limpieza y exploración de datos; métricas DAU, WAU y MAU; duración y frecuencia de las sesiones; conversión por cohorte y canal; pedidos e ingresos; y análisis de LTV, CAC y ROMI según las definiciones empleadas en el proyecto. Para el análisis por canal, cada comprador se asocia a la fuente de su primera visita (*first-touch*).

El período principal de observación abarca de junio de 2017 a mayo de 2018. Los importes se presentan en las unidades monetarias del conjunto de datos; la moneda no está especificada.

## Resultados principales

- Ingresos observados: aproximadamente **252,057** unidades monetarias; gasto de marketing: aproximadamente **329,132** durante el período analizado.
- El **75 % de los compradores** realizó su primera compra dentro de los dos primeros días desde la primera visita, según el análisis de tiempo hasta la conversión.
- En la comparación por canal, **Channel 1** presenta un ROMI aproximado de **1.49**, mientras que **Channel 3** registra aproximadamente **0.39** con la definición utilizada en el notebook.

Las conclusiones y recomendaciones, junto con los gráficos y los cálculos completos, se encuentran en el notebook.

## Estructura del repositorio

```text
.
├── Análisis de marketing, rendimiento y rentabilidad.ipynb
├── visits_log_us.csv
├── orders_log_us.csv
├── costs_us.csv
├── README.md
├── requirements.txt
└── .gitignore
```

## Reproducción

Se recomienda **Python 3.13**. Desde la carpeta del repositorio, crea y activa un entorno virtual, instala las dependencias y abre el notebook:

```bash
pip install -r requirements.txt
Jupyter notebook "Análisis de marketing, rendimiento y rentabilidad.ipynb"
```

Selecciona el kernel del entorno donde instalaste las dependencias y ejecuta las celdas de arriba abajo. Los tres CSV deben permanecer en la misma carpeta que el notebook. Las versiones del archivo `requirements.txt` son una propuesta fijada para reproducibilidad y deben comprobarse mediante una ejecución completa en un entorno limpio antes de publicar.

## Autor
**Adrian Novoa Monzón** <br>
Data Analyst en Formación - TripleTen

## Datos de contacto
- **CV:** <a href="https://github.com/ADRIAN-NOVOA-MONZON/PORTAFOLIO/blob/main/CV%20ADRIAN%20NOVOA%20DATA%20ANALYST.pdf" target="_blank" rel="noopener noreferrer">PDF</a>
- **LinkedIn:** [adrian-novoa-monzon](https://www.linkedin.com/in/adrian-novoa-monzon)
- **Email:** [adrian-novoa-monzon@gmail.com](mailto:adrian-novoa-monzon@gmail.com)
