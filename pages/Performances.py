import streamlit as st
from matplotlib import pyplot as plt


#VARIABLES



#FONCTIONS


#INTERFACE
import streamlit as st

# ==========================================================
# TITRE
# ==========================================================

st.title("🧠 Performances du modèle")

st.markdown("""
Cette page présente les principales métriques d'évaluation du modèle **Regression linéaire** utilisé pour prédire l'intervalle à 85% de taux de confiance de la durée estimative de dégagement d'un canton à la suite d'un incident.

Les performances ont été obtenues sur le jeu de validation à l'aide d'une validation croisée.
""")

st.divider()

# ==========================================================
# METRIQUES
# ==========================================================

st.subheader("📊 Indicateurs de performance")

col1, col2= st.columns(2)

with col1:
    st.metric(
        label="RMSE",
        value="8.65"
    )

with col2:
    st.metric(
        label="MAE",
        value="2.48"
    )
