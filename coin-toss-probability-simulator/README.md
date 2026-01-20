# 🎲 coin-toss-probability-simulator
### Simulador de Lanzamientos de Moneda (Streamlit)

Aplicación en **Streamlit** que simula lanzamientos de una moneda y muestra cómo evoluciona la **media acumulada** conforme aumentan los intentos.

## 🚀 Funcionalidad
- Simulación de lanzamientos usando distribución Bernoulli.  
- Gráfica dinámica con la media acumulada.  
- Registro de cada experimento (número, intentos y media final).  
- Interfaz sencilla e interactiva.

## 🧠 Descripción breve
Cada lanzamiento asigna:
- **1 = Cara**
- **0 = Cruz**

La aplicación calcula la media acumulada y la grafica en tiempo real, mostrando su convergencia al valor esperado de **0.5**.

# ⚙️ Instalación local
```bash
git clone https://github.com/ADRIAN-NOVOA-MONZON/coin-toss-probability-simulator.git
cd coin-toss-probability-simulator
python -m venv venv
venv\Scripts\activate   # En Windows
pip install -r requirements.txt
```

# ▶️ Ejecución
streamlit run app.py

# 👨‍💻 Autor
Adrian Novoa Monzón<br>
Data Analyst en Formación – TripleTen