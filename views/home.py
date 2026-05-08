import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Startseite", layout="centered")

# ---------- Styling ----------
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

# ---------- Titel ----------
st.markdown("""
<div class="custom-card">
    <h1>App für die bakterielle Identifikation, Beschreibungstexte und Lernmodus</h1>
    <p class="small-note"></p>
</div>
""", unsafe_allow_html=True)

# ---------- Inhalt ----------
st.subheader("Inhalt der App")
st.write("- Gram-positive Bakterien identifizieren")
st.write("- Gram-negative Bakterien identifizieren")
st.write("- Testbeschreibungen zur Identifizierung")
st.write("- Bakterien lernen")

# ---------- Bilderpfade ----------

basis_ordner = Path(__file__).resolve().parent.parent
bilder_ordner = basis_ordner / "docs" / "picture" / "Bilder_Bakterien"

gram_pos = bilder_ordner / "Bild_Stammbaum_Gram_pos_Bakterien.png"
gram_neg = bilder_ordner / "Bild_Stammbaum_Gram_neg_Bakterien.png"


# ---------- Debug / Prüfung ----------
if not bilder_ordner.exists():
    st.error(f"Der Ordner wurde nicht gefunden: {bilder_ordner}")
else:
    vorhandene_dateien = [datei.name for datei in bilder_ordner.iterdir() if datei.is_file()]

    if not gram_pos.exists():
        st.error(f"Bild nicht gefunden: {gram_pos.name}")

    if not gram_neg.exists():
        st.error(f"Bild nicht gefunden: {gram_neg.name}")

    if gram_pos.exists() and gram_neg.exists():
        try:
            bild1 = Image.open(gram_pos)
            bild2 = Image.open(gram_neg)

            col1, col2 = st.columns(2)

            with col1:
                st.image(bild1, caption="Gram-positive Bakterien", use_container_width=True)

            with col2:
                st.image(bild2, caption="Gram-negative Bakterien", use_container_width=True)

        except Exception as e:
            st.error("Die Bilder konnten nicht geöffnet werden.")
            st.exception(e)
    else:
        st.write("Dateien im Ordner 'Bilder_Bakterien':")
        for name in vorhandene_dateien:
            st.write("-", name)

# ---------- Projektteam ----------
st.subheader("Projektteam")

st.markdown("""
Diese App wurde von folgenden Personen entwickelt:
- Sara Durrer (durresar@students.zhaw.ch)
- Alessandro Zandt (zandtale@students.zhaw.ch)
- Giuliana Cerullo (cerulgiu@students.zhaw.ch)
- Ladina Lozza (lozzalad@students.zhaw.ch)

Dozent: Samuel Wehrli (wehs@zhaw.ch)
""")
