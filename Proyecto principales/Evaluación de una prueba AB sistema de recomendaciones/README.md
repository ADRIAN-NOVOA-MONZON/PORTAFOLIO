# Evaluación de una prueba A/B: sistema de recomendaciones

Análisis de una prueba A/B de una tienda en línea para evaluar si un sistema de recomendaciones mejorado (grupo B) aumenta la conversión frente al grupo de control (A). El proyecto revisa la calidad de los datos, valida la población experimental, compara el comportamiento de los usuarios y contrasta las tasas de conversión mediante pruebas estadísticas.

## Objetivo

Comprobar si el grupo B alcanza un **incremento relativo de al menos el 10 %** en cada uno de los eventos `product_page`, `product_cart` y `purchase` durante los 14 días posteriores al registro, y si existe evidencia estadística de una mejora frente a A.

## Datos y metodología
Se utilizan cuatro archivos CSV:
- `final_ab_new_users_upd_us.csv`: registros de nuevos usuarios.
- `final_ab_participants_upd_us.csv`: asignaciones a las pruebas A/B.
- `final_ab_events_upd_us.csv`: eventos de comportamiento de los usuarios.
- `ab_project_marketing_events_us.csv`: calendario de campañas de marketing.
El análisis comprende:

1. Revisión de tipos de datos, valores ausentes y duplicados.
2. Validación de fechas, región, asignaciones y disponibilidad de seguimiento; exclusión de participantes presentes en otras pruebas.
3. Construcción de una cohorte analítica con **14 días completos de observación** por usuario.
4. Comparación de actividad, distribución temporal y proporción de usuarios con cada evento.
5. Prueba z unilateral para dos proporciones, con hipótesis alternativa **B > A** y nivel de significancia **α = 0.05**, junto con el criterio de mejora relativa mínima del 10 %.

**Alcance del embudo:** las tasas se calculan como usuarios únicos que registraron cada evento divididos entre el total del grupo. No se exige que un usuario complete los eventos anteriores en orden; por tanto, no es un embudo secuencial.

## Resultados principales

Tras aplicar los criterios de selección, la cohorte analítica contiene **1,419 usuarios: 969 en A y 450 en B**.

| Evento | Conversión A | Conversión B | Cambio relativo de B frente a A | p-value unilateral |
|---|---:|---:|---:|---:|
| `product_page` | 64.29 % | 56.22 % | −12.55 % | 0.9982 |
| `product_cart` | 30.96 % | 27.78 % | −10.28 % | 0.8883 |
| `purchase` | 29.51 % | 27.56 % | −6.64 % | 0.7757 |

El grupo A registró **6.73 eventos por usuario** y B, **5.57**. Ninguna etapa alcanzó la mejora relativa del 10 % y ninguna prueba unilateral produjo evidencia estadísticamente significativa de una mejora de B. **Los resultados de esta prueba no respaldan presentar el nuevo sistema como una mejora de conversión.** No rechazar la hipótesis nula no demuestra equivalencia entre los grupos ni permite afirmar, mediante estas pruebas unilaterales, que A sea estadísticamente superior.

### Limitaciones

- La cohorte analítica tiene tamaños desiguales entre A y B.
- Se excluyeron usuarios que también participaron en otras pruebas; había **887 participantes de esta prueba** presentes en otras pruebas.
- En el período de inscripción, **3,481 de 39,466 nuevos usuarios de EU** participaron en la prueba (**8.82 %**, frente al **15 %** previsto).
- Las ventanas de observación coincidieron parcialmente con `Christmas&New Year Promo` para el **64.50 % de A** y el **44.22 % de B**. Esta coincidencia temporal no prueba exposición efectiva ni un efecto causal de la campaña.

Estas condiciones limitan la interpretación causal de las diferencias observadas.

## Herramientas

**Python · Pandas · NumPy · Matplotlib · Statsmodels · Jupyter Notebook**

## Estructura del proyecto

```text
Test A-B/
├── README.md
├── test_ab_recommender_system.ipynb
├── ab_project_marketing_events_us.csv
├── final_ab_events_upd_us.csv
├── final_ab_new_users_upd_us.csv
└── final_ab_participants_upd_us.csv
```

## Cómo reproducir el análisis

1. Coloca el notebook y los cuatro CSV en la misma carpeta.
2. Instala las dependencias en tu entorno de Python:

   ```bash
   pip install -r requirements.txt
   ```

3. Abre `Evaluación de una prueba A/B: sistema de recomendaciones.ipynb` en Jupyter Notebook o VS Code, selecciona un kernel de Python con esas dependencias y ejecuta las celdas en orden desde un kernel limpio.

Las rutas de lectura del notebook son relativas; ejecútalo desde la carpeta que contiene los CSV. Los datos corresponden a un ejercicio analítico; no se presupone acceso a una plataforma de experimentación en vivo.

## Autor
**Adrian Novoa Monzón**  
Data Analyst en Formación – TripleTen

## Datos de contacto

- **CV:** <a href="https://github.com/ADRIAN-NOVOA-MONZON/PORTAFOLIO/blob/main/ADRIAN%20NOVOA%20CV%20DATA%20ANALYST.pdf" target="_blank" rel="noopener noreferrer">PDF</a>
- **LinkedIn:** [adrian-novoa-monzon](https://www.linkedin.com/in/adrian-novoa-monzon)
- **Email:** [adrian-novoa-monzon@gmail.com](mailto:adrian-novoa-monzon@gmail.com)
