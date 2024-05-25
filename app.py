import streamlit as st
import pandas as pd

# Daten laden
@st.cache_data  # Use cache_data for caching data
def load_data():
    data = pd.read_csv('bfs_data.csv', delimiter=';')  # Semikolon als Trennzeichen
    return data

data = load_data()

# App-Titel und Beschreibung
st.title('Bevölkerungsstatistik der Stadt Zürich')
st.write("""
Diese App ermöglicht die Visualisierung der Bevölkerungsdaten von Zürich nach Postleitzahl und Jahr.
Wählen Sie ein Jahr aus, um die Bevölkerungsdaten für alle Züricher Postleitzahlen zu sehen.
""")

# Benutzerinterface
year_to_filter = st.radio('Jahr wählen', options=data['Jahr'].unique())
filtered_data = data[data['Jahr'] == year_to_filter]

# Daten visualisieren
st.write(f"Bevölkerungsdaten für das Jahr {year_to_filter}")
st.bar_chart(filtered_data[['Postleitzahl', 'Total']].set_index('Postleitzahl'))
