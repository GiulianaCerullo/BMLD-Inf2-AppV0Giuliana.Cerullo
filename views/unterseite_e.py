import streamlit as st

st.set_page_config(page_title="Steckbriefe von Bakterien", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #FFC0CB;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 850px;
}

h1, h2, h3 {
    color: #35627a;
}

div.stButton > button {
    background-color: #6fa8dc;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #5a92c6;
    color: white;
}

div[data-testid="stRadio"] > label {
    font-weight: 600;
    color: #35627a;
}

.custom-card {
    background-color: white;
    padding: 1.2rem;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
    margin-bottom: 1rem;
}

.small-note {
    color: #5c7380;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="custom-card">
    <h1>Bakterien Steckbriefe</h1>
    <p class="small-note">
        Hier wird dir jedes Bakterium mit einem Steckbrief beschrieben, damit du die wichtigsten Informationen auf einen Blick hast. 
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="custom-card">
    <h1>Bakterien Steckbriefe</h1>
    <p class="small-note">
        Hier wird dir jedes Bakterium mit einem Steckbrief beschrieben, damit du die wichtigsten Informationen auf einen Blick hast. 
    </p>
</div>
""", unsafe_allow_html=True)

st.write("Hier könnte jetzt dein Menü oder die erste Auswahl kommen.")
