import streamlit as st

st.set_page_config(
    page_title="Canton Time predict app",
    page_icon="🛤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar design
st.sidebar.title("🚞 TIME CANTON PREDICT")
#st.sidebar.image("https://img.icons8.com/fluency/96/bank.png")

st.title("🚞 Simulation du temps de libération de canton par Intelligence Artificielle")

st.markdown("""
### Bienvenue 👋

Cette application est une simulation d'estimation la **durée de la libération d'un canton à la suite d'un incident** à l'aide d'un modèle de **Regression linéaire** entraîné sur un jeu de données de  **160 observations** synthétiques et générés à partir de certaines ressources opensource de la SNCF.

---

### 🚀 Fonctionnalités

- Évaluation automatisée de la durée de libération de canton par Intelligence Artificielle
- Prédiction de la durée de liberation du canton avec une plage d'intervalle de 85% en temps reel
- Explication des prédictions grâce à SHAP (IA explicable)
""")

# Cartes d'information
col1, col2, col3, col4 = st.columns(4)

col1.metric("Taille du jeu de données", "150")
col2.metric("Modèle utilisé", "Regression Linèaire")
col3.metric("RMSE", "8.65")
col4.metric("MAE", "2.48")

st.divider()

st.info("Utilisez le menu de navigation situé à gauche pour accéder aux différentes fonctionnalités de l'application.")