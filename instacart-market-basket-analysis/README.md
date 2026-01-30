# Instacart Market Basket Analysis

## Introducción
Análisis exploratorio de datos del dataset público de **Instacart**, enfocado en comprender patrones de compra, comportamiento de usuarios y características de los pedidos dentro de una plataforma de e-commerce.

---

## Descripción

Este proyecto presenta un **análisis exploratorio de datos (EDA)** del dataset público **Instacart Market Basket Analysis**, el cual contiene información detallada sobre pedidos, productos y comportamiento de usuarios dentro de una plataforma de e-commerce de alimentos.

El objetivo principal del análisis es **comprender los patrones de compra de los usuarios**, así como identificar tendencias relacionadas con la frecuencia de pedidos, el número de productos por orden y el comportamiento de recompra. A través de la exploración y visualización de los datos, se busca transformar datos crudos en insights accionables que permitan entender cómo interactúan los usuarios con la plataforma.

El análisis se apoya en **visualizaciones claras y descriptivas** que facilitan la interpretación de los resultados y permiten detectar patrones relevantes de manera intuitiva.

Este proyecto fue desarrollado como parte de mi **portafolio profesional**, con el objetivo de demostrar habilidades en:
- Limpieza y exploración de datos
- Análisis descriptivo
- Visualización de datos
- Comunicación de resultados a partir de datos reales

---

## Objetivos del proyecto
- Analizar la estructura y relación entre pedidos, productos y usuarios.
- Explorar la distribución del número de productos por pedido.
- Identificar patrones de recompra de productos.
- Detectar usuarios con alta frecuencia de pedidos.
- Comunicar hallazgos mediante visualizaciones descriptivas.
---

## Fuentes de Datos

Los datos utilizados fueron **proporcionados por TripleTen** con fines educativos.  
Estos datasets están **basados en el conjunto de datos público *Instacart Market Basket Analysis***, pero han sido **preprocesados y modificados** por TripleTen para su uso académico.

Archivos utilizados:
- `instacart_orders.csv`: Información general de los pedidos.
- `order_products.csv`: Relación pedidos–productos.
- `products.csv`: Catálogo de productos.
- `aisles.csv`: Catálogo de pasillos.
- `departments.csv`: Catálogo de departamentos.

Fuente original de referencia:  
https://www.kaggle.com/competitions/instacart-market-basket-analysis

---

## Tecnologías utilizadas
- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Jupyter Notebook**

---

## Estructura del proyecto
```text
instacart-market-basket-analysis/
├── README.md                               # Documentación del proyecto
├── departments.csv                         # Catálogo de departamentos
├── instacart_orders.csv                    # Información de pedidos
├── instacart-market-basket-analysis.ipynb  # Notebook con el análisis exploratorio
├── order_products.csv                      # Relación pedidos-productos
├── products.csv                            # Catálogo de productos
└── aisles.csv                              # Catálogo de pasillos
```

--- 

## Metodología

- Carga de los datasets proporcionados por TripleTen.
- Revisión de la estructura de los datos y detección de valores faltantes.
- Limpieza básica y preparación de los datos para el análisis.
- Análisis exploratorio enfocado en:
- Número de pedidos por usuario.
- Cantidad de productos por pedido.
- Frecuencia de recompra de productos.
- Generación de visualizaciones descriptivas para identificar patrones.
- Interpretación de resultados y documentación de hallazgos dentro del notebook.

---

## Resultados y Conclusiones

El análisis exploratorio permitió identificar patrones claros en el comportamiento de compra de
los usuarios, tanto en frecuencia como en recompra y preferencias de producto.

Los pedidos se concentran principalmente entre las **10:00 a.m. y 4:00 p.m.**, con mayor actividad
los **domingos y lunes**, y la mayoría de los usuarios realiza un nuevo pedido en un intervalo de
**1 a 10 días**. A nivel de productos, existe una alta recompra en artículos **orgánicos y frescos**,
lo que refleja hábitos de consumo recurrentes.

En conjunto, los resultados evidencian la coexistencia de **usuarios esporádicos**, **clientes
recurrentes** y un grupo reducido de **usuarios altamente fieles**. Este análisis es descriptivo y
se basa en datos históricos, por lo que algunas hipótesis planteadas requerirían estudios
adicionales para su validación.

---

## Insights Principales

### 1. Alta recompra de productos, baja recompra de usuarios
Los clientes son fieles a los productos, pero no necesariamente a la plataforma.  
**Recomendación:** estrategias de retención y programas de lealtad post-compra.

### 2. Picos de pedidos entre 10 a.m. y 4 p.m., domingos y lunes
Los usuarios compran cuando disponen de más tiempo libre o al inicio de la semana.  
**Recomendación:** campañas en horarios pico y promociones en horas de baja actividad.

### 3. Pedidos pequeños con promedio de 10 productos
Predominan pedidos de tamaño moderado (1–20 artículos).  
**Recomendación:** incentivos para aumentar el tamaño del carrito.

### 4. Preferencia por productos básicos y orgánicos
Frutas, verduras y lácteos orgánicos lideran en ventas y recompra.  
**Recomendación:** fortalecer la categoría *Healthy* y explorar modelos de suscripción.

### 5. Clientes conservadores en su elección de productos
La mayoría repite los mismos artículos y explora poco.  
**Recomendación:** venta cruzada y recomendaciones personalizadas.

---

## Autor
Adrian Novoa Monzón<br>
Data Analyst en Formación – TripleTen 

---

## Datos de Contacto

- **Cv:** <a href="https://github.com/ADRIAN-NOVOA-MONZON/PORTAFOLIO/blob/main/ADRIAN%20NOVOA%20CV%20DATA%20ANALYST.pdf" target="_blank" rel="noopener noreferrer"> Pdf </a>
- **LinkedIn:** [adrian-novoa-monzon](https://www.linkedin.com/in/adrian-novoa-monzon)
- **Email:** [adrian-novoa-monzon@gmail.com](mailto:adrian-novoa-monzon@gmail.com)