import numpy as np
import pandas as pd
import streamlit as st
import random
import statistics
import matplotlib.pyplot as plt




st.write("Inserisci i parametri richiesti per calcolare il VAN e visualizzare la distribuzione.")
m = st.number_input("Inserisci taglia campionaria", min_value=1)
costo = st.number_input("Inserisci costo",min_value=1)
durata = st.number_input("Inserisci durata",min_value=1)


col1, col2 = st.columns(2)
with col2:
    tasso_min = st.number_input("Inserisci tasso minimo",max_value=0.99, min_value=0.000001)
    tasso_max = st.number_input("Inserisci tasso massimo",max_value=0.99, min_value=0.000001)
with col1:
    media_flussi = st.number_input("Inserisci media flussi",min_value=1)
    sd_flussi = st.number_input("Inserisci deviazione standard flussi",value=0)

elenco_van = []  # Lista per memorizzare i VAN di ogni simulazione

for _ in range(m):
    tasso = np.random.uniform(tasso_min, tasso_max)  # Genera un tasso per ogni simulazione
    van = -costo  # Inizializza il VAN con il costo iniziale
    for t in range(1, durata + 1):
        flusso = np.random.normal(media_flussi, sd_flussi)  # Genera un flusso di cassa per ogni anno
        van += flusso / (1 + tasso)**t  # Calcola il VAN attualizzato
    elenco_van.append(van)  # Aggiungi il VAN alla lista

media = np.mean(elenco_van)  # Calcola la media dei VAN

st.write("Media del VAN:", media)

plt.figure(figsize=(10, 6))
plt.hist(elenco_van, bins=10, color="skyblue", edgecolor="black")
plt.axvline(media, color="red", linewidth=2)
plt.title("Distribuzione del VAN")
plt.xlabel("VAN")
plt.ylabel("Frequenza")
plt.legend()

st.pyplot(plt)

