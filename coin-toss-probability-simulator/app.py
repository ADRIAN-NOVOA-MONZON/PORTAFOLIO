"""
Aplicación de Streamlit que simula lanzamientos de una moneda y muestra cómo
la media acumulada cambia conforme aumentan los intentos.

El módulo permite:
- Ejecutar simulaciones de lanzamientos.
- Visualizar la media acumulada en una gráfica.
- Registrar los resultados básicos de cada experimento.
"""


# IMPORTAR LIBRERIAS
import time

import pandas as pd
import scipy.stats
import streamlit as st


# VARIABLES DE ESTADO DE LA SESIÓN
# Contador de experimentos
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

# DataFrame para almacenar resultados de experimentos
if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(
        columns=['no', 'iteraciones', 'media'])

# TÍTULO DE LA APLICACIÓN
st.header('Lanzar una moneda')


# GRÁFICA DE RESULTADOS
chart = st.line_chart([0.5])


# FUNCIÓN PARA SIMULAR LANZAMIENTOS DE MONEDA
def toss_coin(n):
    """
    Esta función simula el lanzamiento de una moneda n veces y actualiza la gráfica
    con la media acumulada de resultados (cara = 1, cruz = 0).
    """
    # Simular lanzamientos de moneda
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    # Inicializar contadores
    current_mean = None
    outcome_no = 0
    outcome_1_count = 0

    # Calcular media acumulada y actualizar gráfica
    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        current_mean = outcome_1_count / outcome_no
        chart.add_rows([current_mean])
        time.sleep(0.05)

    return current_mean


# INTERFAZ DE USUARIO
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

# Al hacer click en el botón de iniciar
if start_button:
    # Ejecutar la simulación y guardar el resultado
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    st.session_state['experiment_no'] += 1
    mean = toss_coin(number_of_trials)
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        pd.DataFrame(data=[[st.session_state['experiment_no'],
                            number_of_trials,
                            mean]],
                     columns=['no', 'iteraciones', 'media'])
    ],
        axis=0)
    st.session_state['df_experiment_results'] = (
        st.session_state['df_experiment_results']
        .reset_index(
            drop=True)
    )


# MOSTRAR RESULTADOS DE EXPERIMENTOS
st.subheader('Resultados de experimentos')
st.write(
    st.session_state['df_experiment_results'].rename(
        columns={'no': 'Número de experimento',
                 'iteraciones': 'Número de intentos',
                 'media': 'Media'
                 }
    )
)
