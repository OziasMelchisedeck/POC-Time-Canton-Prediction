import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from utils.prediction import pipeline_load_predict, make_prediction
import math


#VARIABLES
pipeline = pipeline_load_predict() #Chargement du pipeline
prediction = 0
resultatsOk = False

##FONCTIONS
#fonction permettant d'obtenir la plage horaire
def getPlageHoraire(temps) :
    heures, minutes, secondes =  str(temps).split(':')
    heures = int(heures)
    minutes = int(minutes)
    if heures < 18 and heures >= 6 :
        return 'journee'
    else :
        return 'nuit'

#fonction permettant l'obtention des heures sinus et cosinus
def getAlternativeTime(time):
    heure_sin = np.sin(2 * np.pi * (int(str(time).split(':')[0]) + int(str(time).split(':')[1]) / 24))
    heure_cos = np.cos(2 * np.pi * (int(str(time).split(':')[0]) + int(str(time).split(':')[1]) / 24))
    return heure_sin, heure_cos

#Fonction d'enregistrement des données de prediction
def save_prediction_data():
    hsin, hcos = getAlternativeTime(st.session_state.heure_detection_incident)
    pHoraire = getPlageHoraire(st.session_state.heure_detection_incident)
    data = pd.DataFrame(
        [{
             "heure_sin" : hsin,
             "heure_cos" : hcos,
             "plage_horaire" : pHoraire,
             "type_incident" : st.session_state.type_incident,
             "nombre_engins_derailles" : st.session_state.nombre_engins_derailles,
             "nombre_wagons_touches" : st.session_state.nombre_wagons_touches,
             "presence_marchandises_dangereuses" : st.session_state.presence_marchandises_dangereuses,
             "voie_unique" : st.session_state.voie_unique,
             "accessibilite_site" : st.session_state.accessibilite_site,
             "degats_infrastructure" : st.session_state.degats_infrastructure,
             "deviation_possible" : st.session_state.deviation_possible,
             "nombre_equipes_intervention" : st.session_state.nombre_equipes_intervention,
             "disponibilite_grue_secours" : st.session_state.disponibilite_grue_secours,
             "distance_depuis_base_secours_km" : st.session_state.distance_depuis_base_secours_km,
             "meteo_defavorable" : st.session_state.meteo_defavorable,
             "obscurite_nuit" : st.session_state.obscurite_nuit,
             "temps_balisage_securisation_min" : st.session_state.temps_balisage_securisation_min,
             "temps_constat_ret_min" : st.session_state.temps_constat_ret_min,
             "temps_releve_material_min" : st.session_state.temps_releve_material_min,
             "temps_reparation_voie_min" : st.session_state.temps_reparation_voie_min,
             "temps_essais_reprise_min" : st.session_state.temps_essais_reprise_min,
        }])
    return data

##INTERFACE

st.title("Simulation")
st.layout = "wide"

st.markdown("""
<style>
.big-font {
    font-size:18px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("#### Renseigner les informations indicatives et obtenez une prévision")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    heure_detection_incident = st.time_input("Heure de detection de l'incident", key="heure_detection_incident")
    type_incident = st.selectbox(
        "Type d'incident",
        ["Déraillement_simple", "Déraillement_multiple", "Collision_simple", "Collision_multiple", "Obstacle_voie"],
        key="type_incident"
    )
    nombre_engins_derailles = st.number_input("Nombre d'engins déraillés", min_value=0, key="nombre_engins_derailles")
    nombre_wagons_touches = st.number_input("Nombre de wagons touchés", min_value=0, key="nombre_wagons_touches")
    presence_marchandises_dangereuses = st.number_input("Présence des marchandises dangereuses ?", min_value= 0, max_value=1, key="presence_marchandises_dangereuses")
    voie_unique = st.number_input("Voie unique ?", min_value=0, max_value=1, key="voie_unique")

with col2:
        accessibilite_site = st.selectbox(
            "Accessibilité du site",
            ["Difficile", "Moyenne", "Facile"],
            key = "accessibilite_site"
        )
        degats_infrastructure = st.selectbox(
            "Dégats sur les infrastuctures",
            ["Élevés", "Moyens", "Faibles"],
            key = "degats_infrastructure"
        )
        deviation_possible = st.number_input("Déviation possible ?", min_value=0, max_value=1, key="deviation_possible")
        nombre_equipes_intervention = st.number_input("Nombre d'équipes d'intevention", min_value=0, key="nombre_equipes_intervention")
        disponibilite_grue_secours = st.number_input("Disponibilité grue de secours?", min_value=0, key="disponibilite_grue_secours")
        distance_depuis_base_secours_km = st.number_input("Distance depuis la base de secours en km", min_value=0, key="distance_depuis_base_secours_km")
    
with col3:
        meteo_defavorable = st.number_input("Météo défavorable ?", min_value=0, max_value=0, key="meteo_defavorable")
        obscurite_nuit = st.number_input("Obscurité nuit ?", min_value=0, max_value=0, key="obscurite_nuit")
        temps_balisage_securisation_min = st.number_input("Temps de balisage de securisation en minutes", min_value=0, key="temps_balisage_securisation_min")
        temps_essais_reprise_min = st.number_input("Temps essais reprise en minutes", min_value=0, key="temps_essais_reprise_min")

with col4:
        temps_constat_ret_min = st.number_input("Temps de constatation en minutes", min_value=0, key="temps_constat_ret_min")
        temps_releve_material_min = st.number_input("Temps de releve du materiel en minutes", min_value=0, key="temps_releve_material_min")
        temps_reparation_voie_min = st.number_input("Temps de reparation de la voie en minutes", min_value=0, key="temps_reparation_voie_min")

st.divider()

if st.button("🔮 Simulation"):
     data = save_prediction_data()
     prediction = make_prediction(pipeline, data)
     if prediction:
          st.metric(label="Durée probale de degagement du canton en minutes à intevalle de 85% comprise entre", value = f"[{math.ceil(prediction * 0.85)} - {math.ceil(prediction * 1.15)}]")