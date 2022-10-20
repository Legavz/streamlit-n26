import pandas as pd
import random
import math
import streamlit as st


"""
Bienvenue sur les petits gestes !

Le calculateur de vos arrondis mensuels qui va vous permettre de contribuer au bien commun :)

Pour cela, il vous suffit simplement de télécharger votre relevé de transactions sur N26 et de le mettre dans l'app
"""

uploaded_file = st.file_uploader("Sélectionnez votre relevé")

df_releve = pd.read_csv(uploaded_file)

df_releve_filtre = df_releve[df_releve["Montant (EUR)"] < 0]

df_releve_filtre["Arrondis_depenses"] = df_releve_filtre["Montant (EUR)"].apply(lambda x : math.ceil(-x) + x)

df_releve_filtre['mois'] = pd.DatetimeIndex(df_releve_filtre['Date']).month

mois = st.number_input(label = 'Quel mois arrondir ?', min_value = 1, max_value = 12)

montant = df_releve_filtre[df_releve_filtre['mois'] == mois]["Arrondis_depenses"].sum()
montant = round(montant, 1)

st.write("Le montant de ton don s'élève à", montant)
