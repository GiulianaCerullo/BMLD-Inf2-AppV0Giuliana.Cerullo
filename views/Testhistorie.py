"""Streamlit-Seite zur Anzeige der gespeicherten Quiz-Testhistorie.

Die Daten werden in der App bereits nach dem Login aus der Switch-Drive-Datei
`data.csv` geladen und in `st.session_state["data_df"]` gespeichert.
Diese Seite zeigt die gespeicherten Einträge als einfache Liste an.
"""

import pandas as pd
import streamlit as st


st.markdown("""
<style>
.stApp {
    background-color: #FFF8DC;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 900px;
}

h1, h2, h3 {
    color: #7a6535;
}

.custom-card {
    background-color: white;
    padding: 1.2rem;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
    margin-bottom: 1rem;
}

.small-note {
    color: #7b725c;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="custom-card">
    <h1>Testhistorie</h1>
    <p class="small-note">
        Hier siehst du deine gespeicherten Ergebnisse aus dem Lernmodus.
    </p>
</div>
""", unsafe_allow_html=True)


st.subheader("Gespeicherte Testergebnisse")

data_df = st.session_state.get("data_df", pd.DataFrame())

if data_df.empty:
    st.info("Es sind noch keine gespeicherten Testergebnisse vorhanden.")
else:
    data_df = data_df.copy()

    if "timestamp" in data_df.columns:
        data_df["timestamp"] = pd.to_datetime(data_df["timestamp"], errors="coerce")
        data_df = data_df.sort_values("timestamp", ascending=False)

    for nummer, (_, eintrag) in enumerate(data_df.iterrows(), start=1):
        punkte = eintrag.get("punkte", "-")
        anzahl_fragen = eintrag.get("anzahl_fragen", "-")
        result = eintrag.get("result", None)
        timestamp = eintrag.get("timestamp", None)

        if pd.notna(result):
            prozent = round(float(result) * 100)
            ergebnis_text = f"{prozent}%"
        else:
            ergebnis_text = "-"

        if pd.notna(timestamp):
            zeit_text = pd.to_datetime(timestamp).strftime("%d.%m.%Y %H:%M")
        else:
            zeit_text = "Zeitpunkt unbekannt"

        st.write(
            f"{nummer}. {zeit_text} - "
            f"{punkte} von {anzahl_fragen} Punkten - "
            f"Ergebnis: {ergebnis_text}"
        )