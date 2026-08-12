import streamlit as st
from matplotlib import pyplot as plt
from utils.shap import load_shape
import shap


#VARIABLES
explainer, shap_values, expected_value, dataset = load_shape() #Chargement des infos d'explicabilité Shap


#FONCTIONS


#INTERFACE
#==========================================================
# TITRE
#==========================================================
st.title("🔍 Explicabilité du modèle")
st.layout = "wide"

 
st.markdown("""
Cette section présente l'interprétation globale des décisions du modèle **Regression Linéaire** grâce à la méthode **SHAP (SHapley Additive exPlanations)**.

L'objectif est d'identifier les variables qui influencent le plus les prédictions et de comprendre leur impact sur l'évaluation de la durée de dégagement de canton.
""")

st.divider()


# ==========================================================
# IMPORTANCE GLOBALE
# ==========================================================

st.subheader("🏆 Importance globale des variables")

st.markdown("""
Ce graphique présente le classement des variables selon leur contribution moyenne aux décisions du modèle.

Il permet d'identifier rapidement les facteurs les plus déterminants dans l'évaluation du risque de crédit.
""")

fig2, ax2 = plt.subplots(figsize=(10, 6))

shap.summary_plot(
    shap_values,
    dataset,
    plot_type="bar",
    show=False
)

fig2 = plt.gcf()

st.pyplot(fig2)

plt.close(fig2)


st.divider()


# ==========================================================
# CONCLUSION
# ==========================================================

st.success("""
Grâce à SHAP, le modèle de Regression Linéaire devient plus transparent en permettant d'identifier les facteurs influençant ses décisions.

Cette interprétabilité est essentielle dans les domaines financiers, où les modèles doivent combiner performance prédictive, fiabilité et capacité d'explication.
""")