import pandas as pd
import random
import math
import streamlit as st

uploaded_file = st.file_uploader("Sélectionnez un fichier")

df_releve = pd.read_csv(uploaded_file)

df_releve_filtre = df_releve[df_releve["Montant (EUR)"] < 0]

df_releve_filtre["Arrondis_depenses"] = df_releve_filtre["Montant (EUR)"].apply(lambda x : math.ceil(-x) + x)

df_releve_filtre['mois'] = pd.DatetimeIndex(df_releve_filtre['Date']).month

mois = input("Quel mois souhaiez-vous arrondir ?")

montant = df_releve_filtre[df_releve_filtre['mois'] == mois]["Arrondis_depenses"].sum()

st.write(montant)
