import pandas as pd
import random
import math
import streamlit as st


"""
Bienvenue sur les petits gestes !

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""

uploaded_file = st.file_uploader("Sélectionnez un fichier")

df_releve = pd.read_csv(uploaded_file)

df_releve_filtre = df_releve[df_releve["Montant (EUR)"] < 0]

df_releve_filtre["Arrondis_depenses"] = df_releve_filtre["Montant (EUR)"].apply(lambda x : math.ceil(-x) + x)

df_releve_filtre['mois'] = pd.DatetimeIndex(df_releve_filtre['Date']).month

mois = st.number_input(label = 'Quel mois arrondir ?', min_value = 1, max_value = 12)

montant = df_releve_filtre[df_releve_filtre['mois'] == mois]["Arrondis_depenses"].sum()

st.write(montant)
