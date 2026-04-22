# !! WICHTIG: Eure Emails müssen in der App erscheinen!!
import streamlit as st
import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #FFF8DC;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 850px;
}

h1, h2, h3 {
    color: #7a6535;
}

div.stButton > button {
    background-color: #d4b04c;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #b89535;
    color: white;
}

div[data-testid="stRadio"] > label {
    font-weight: 600;
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
    <h1>App für die bakterille Identifikation, Beschreibungstexte und Lernmodus</h1>
    <p class="small-note">
    </p>
</div>
""", unsafe_allow_html=True)


st.subheader("Inhalt der App")
st.write("- Gram-positive Bakterien identifizieren")
st.write("- Gram-negative Bakterien identifizieren")
st.write("- Testbeschreibungen zur Identifizierung")
st.write("- Bakterien lernen")

st.subheader("Projektteam")

"""
Diese App wurde von folgenden Personen entwickelt:
- Sara Durrer (durresar@students.zhaw.ch)
- Alessandro Zandt (zandtale@students.zhaw.ch)
- Giuliana Cerullo (cerulgiu@students.zhaw.ch)
- Ladina Lozza (lozzalad@students.zhaw.ch)

Dozent: Samuel Wehrli (wehs@zhaw.ch)
"""
