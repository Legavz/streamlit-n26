import pandas as pd
import random
import math
import streamlit as st

df_releve = pd.read_csv("C:/Users/Alexis/Documents/Python/Projets/N26/releve_17_10")

df_releve_filtre = df_releve[df_releve["Montant (EUR)"] < 0]

df_releve_filtre["Arrondis_depenses"] = df_releve_filtre["Montant (EUR)"].apply(lambda x : math.ceil(-x) + x)

df_releve_filtre['mois'] = pd.DatetimeIndex(df_releve_filtre['Date']).month

st.dataframe(df_releve_filtre)  # Same as st.write(df)
