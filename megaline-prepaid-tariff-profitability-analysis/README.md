# Megaline Prepaid Tariff Profitability Analysis

## Introducción
Este proyecto presenta un **análisis exploratorio y comparativo de rentabilidad** de planes de telefonía **prepago** ofrecidos por la empresa Megaline.  
El objetivo principal es identificar **qué plan genera mayores ingresos** y bajo qué patrones de uso, con el fin de apoyar la toma de decisiones relacionadas con precios, segmentación de clientes y estrategia comercial.

---

## Descripción Detallada
El análisis se centra en el comportamiento de los usuarios de planes prepago, considerando su consumo de **llamadas, mensajes y datos móviles** a lo largo del tiempo.  
A partir de estos patrones de uso, se calculan los ingresos generados por cada cliente y se comparan los resultados entre los distintos planes disponibles.

El proyecto combina limpieza de datos, agregaciones, análisis descriptivo y visualizaciones para evaluar la **rentabilidad real** de cada plan, más allá de su precio base.

---

## Objetivos
- Analizar el comportamiento de consumo de los usuarios de planes prepago.
- Calcular los ingresos generados por cliente y por plan.
- Comparar la rentabilidad entre los distintos planes de Megaline.
- Identificar qué tipo de usuarios resulta más rentable para cada plan.
- Proporcionar insights que apoyen decisiones de negocio basadas en datos.

---

## Fuentes de Datos

Los datos fueron **proporcionados por TripleTen con fines educativos** y corresponden a un dataset académico de clientes de la empresa Megaline.  
La documentación del proyecto no especifica si los datos son reales o sintéticos, por lo que se utilizan exclusivamente con fines de análisis y aprendizaje.

Archivos utilizados dentro del proyecto:
- `megaline_users.csv`: Información general de los usuarios.
- `megaline_plans.csv`: Detalles de los planes prepago.
- `megaline_calls.csv`: Registro de llamadas realizadas.
- `megaline_messages.csv`: Registro de mensajes enviados.
- `megaline_internet.csv`: Uso de datos móviles.


---

## Tecnologías Utilizadas
- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Jupyter Notebook**

---

## Estructura del Proyecto

```text
megaline-prepaid-tariff-profitability-analysis
├── README.md
├── megaline-prepaid-tariff-profitability-analysis.ipynb
├── megaline_calls.csv
├── megaline_internet.csv
├── megaline_messages.csv
├── megaline_plans.csv
└── megaline_users.csv
```

---

## Metodología
El análisis se desarrolló en un Jupyter Notebook y sigue los siguientes pasos:

1. Carga y revisión inicial de los datasets.
2. Limpieza de datos y manejo de valores faltantes.
3. Agregación del consumo mensual por usuario.
4. Cálculo de ingresos por cliente considerando las condiciones de cada plan.
5. Análisis comparativo de ingresos entre planes.
6. Visualización de resultados para identificar patrones y diferencias relevantes.
7. Interpretación de resultados con enfoque de negocio.

---

## Resultados y Conclusiones

El análisis permitió evaluar el comportamiento de consumo, ingresos y rentabilidad de los usuarios de Megaline a partir del uso mensual de llamadas, mensajes e internet, comparando el desempeño de los planes Surf y Ultimate.

Los resultados muestran diferencias claras tanto en **nivel de ingresos** como en **estabilidad y patrones de consumo** , lo que tiene implicaciones directas para la estrategia comercial y de publicidad.

## Insights Principales

### 1. Surf maximiza volumen; Ultimate maximiza rentabilidad
El plan Surf concentra mayores ingresos totales, mientras que Ultimate ofrece mayor ingreso promedio por cliente.  
**Implicación:** El presupuesto publicitario debe asignarse según el objetivo: volumen (Surf) o rentabilidad (Ultimate).

### 2. La volatilidad del plan Surf proviene del consumo excedente
La alta dispersión de ingresos en Surf se explica por usuarios que superan frecuentemente los límites incluidos.  
**Implicación:** Existe oportunidad de *upselling* hacia Ultimate o de ajuste en los límites del plan Surf.

### 3. Ultimate ofrece ingresos más estables y predecibles
La mayoría de los usuarios de Ultimate se mantiene dentro de los límites del plan, generando una distribución de ingresos concentrada alrededor del precio base.  
**Implicación:** Es un plan ideal para clientes de alto valor y planeación financiera estable.

### 4. Existen perfiles de cliente claramente diferenciados
Surf atrae usuarios con consumo variable y mayor sensibilidad a los límites, mientras que Ultimate concentra usuarios con consumo alto y comportamiento consistente.  
**Implicación:** Ambos planes deben tratarse como productos complementarios, no sustitutos.

### 5. La región influye en el comportamiento de consumo
Los usuarios de NY–NJ presentan patrones de ingresos significativamente distintos a los de otras regiones.  
**Implicación:** Las estrategias comerciales y de marketing pueden optimizarse con segmentación geográfica.

- En conjunto, los resultados sugieren que la estrategia óptima para Megaline no consiste en priorizar un solo plan, sino en combinar el crecimiento en volumen del plan Surf con la estabilidad y rentabilidad del plan Ultimate, alineando la oferta a distintos perfiles de cliente y contextos regionales.


---

## Autor
**Adrian Novoa Monzón**  
Data Analyst en formación – TripleTen  

---

## Datos de Contacto

- **Cv:** <a href="https://github.com/ADRIAN-NOVOA-MONZON/PORTAFOLIO/blob/main/ADRIAN%20NOVOA%20CV%20DATA%20ANALYST.pdf" target="_blank" rel="noopener noreferrer"> Pdf </a>
- **LinkedIn:** [adrian-novoa-monzon](https://www.linkedin.com/in/adrian-novoa-monzon)
- **Email:** [adrian-novoa-monzon@gmail.com](mailto:adrian-novoa-monzon@gmail.com)
