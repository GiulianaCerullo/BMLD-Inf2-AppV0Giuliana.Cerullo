import streamlit as st

st.set_page_config(page_title="Gram-negative Bakterien", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #FFF0F5;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 850px;
}

h1, h2, h3 {
    color: #7a1f2b;
}

div.stButton > button {
    background-color: #b33b4d;
    color: white;
    border-radius: 14px;
    border: none;
    padding: 0.65rem 1.1rem;
    font-weight: 600;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.12);
}

div.stButton > button:hover {
    background-color: #922f3f;
    color: white;
}

div[data-testid="stRadio"] > label {
    font-weight: 600;
    color: #7a1f2b;
}

div[role="radiogroup"] > label {
    background-color: #ffffff;
    padding: 0.35rem 0.75rem;
    border-radius: 10px;
    margin-bottom: 0.35rem;
    border: 1px solid #f0cfd6;
}

.custom-card {
    background-color: white;
    padding: 1.2rem;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
    margin-bottom: 1rem;
}

.small-note {
    color: #6b4b51;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="custom-card">
    <h1>Gram-negative Bakterien identifizieren</h1>
    <p class="small-note">
        Wähle Schritt für Schritt die passenden Merkmale aus, um gramnegative Bakterien einzuordnen.
    </p>
</div>
""", unsafe_allow_html=True)

reset_keys = [
    "morphologie_gn",
    "maltose",
    "sauerstoff_bazillen_gn",
    "laktose",
    "oxidase_laktose",
    "oxidase_keine_laktose",
    "h2s",
    "gekruemmt",
]

if st.button("Alles zurücksetzen"):
    for key in reset_keys:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

morphologie = st.radio(
    "Wähle die Morphologie:",
    ["Diplokokken", "Bazillen", "gekrümmte Bakterien", "Kokkenbazillen"],
    key="morphologie_gn",
    index=None
)

if morphologie == "Diplokokken":
    st.info("""
Gemeinsame Eigenschaften:
- aerob
- oxidase positiv
""")

    if "maltose" not in st.session_state:
        st.session_state.maltose = None

    maltose = st.radio(
        "Wird Maltose verwertet?",
        ["Maltose-Verwertung", "keine Maltose-Verwertung"],
        key="maltose",
        index=None
    )

    if maltose == "Maltose-Verwertung":
        st.success("""
Bakterium: N. meningitidis
""")
        st.write("Dieser Pfad ist fertig.")

    elif maltose == "keine Maltose-Verwertung":
        st.success("""
Bakterien: N. gonorrhoeae, Moraxella
""")
        st.write("Dieser Pfad ist fertig.")

elif morphologie == "Bazillen":
    if "sauerstoff_bazillen_gn" not in st.session_state:
        st.session_state.sauerstoff_bazillen_gn = None

    sauerstoff = st.radio(
        "Wie ist das Sauerstoffverhalten?",
        ["anaerob", "aerob"],
        key="sauerstoff_bazillen_gn",
        index=None
    )

    if sauerstoff == "anaerob":
        st.success("""
Bakteriengruppe: anaerobe gramnegative Bazillen
Beispiele: Bacteroides, Fusobakterien
""")
        st.write("Dieser Pfad ist fertig.")

    elif sauerstoff == "aerob":
        if "laktose" not in st.session_state:
            st.session_state.laktose = None

        laktose = st.radio(
            "Wird Laktose verwertet?",
            ["Laktose-Verwertung", "keine Laktose-Verwertung"],
            key="laktose",
            index=None
        )

        if laktose == "Laktose-Verwertung":
            if "oxidase_laktose" not in st.session_state:
                st.session_state.oxidase_laktose = None

            oxidase_laktose = st.radio(
                "Wie ist das Oxidase-Verhalten?",
                ["oxidase negativ (schnell)", "oxidase negativ (langsam)"],
                key="oxidase_laktose",
                index=None
            )

            if oxidase_laktose == "oxidase negativ (schnell)":
                st.success("""
Bakterien: E. coli, Klebsiella, Enterobacter
""")
                st.write("Dieser Pfad ist fertig.")

            elif oxidase_laktose == "oxidase negativ (langsam)":
                st.success("""
Bakterien: Citrobacter, Serratia
""")
                st.write("Dieser Pfad ist fertig.")

        elif laktose == "keine Laktose-Verwertung":
            if "oxidase_keine_laktose" not in st.session_state:
                st.session_state.oxidase_keine_laktose = None

            oxidase_keine_laktose = st.radio(
                "Wie ist das Oxidase-Verhalten?",
                ["oxidase positiv", "oxidase negativ"],
                key="oxidase_keine_laktose",
                index=None
            )

            if oxidase_keine_laktose == "oxidase positiv":
                st.success("""
Bakterien: Pseudomonas, Legionella, Burkholderia
Merkmal: Non-Fermenter
""")
                st.write("Dieser Pfad ist fertig.")

            elif oxidase_keine_laktose == "oxidase negativ":
                if "h2s" not in st.session_state:
                    st.session_state.h2s = None

                h2s = st.radio(
                    "Liegt eine H2S-Produktion auf TSI-Agar vor?",
                    ["H2S-Produktion auf TSI-Agar", "keine H2S-Produktion auf TSI-Agar"],
                    key="h2s",
                    index=None
                )

                if h2s == "H2S-Produktion auf TSI-Agar":
                    st.success("""
Bakterien: Salmonella, Proteus
""")
                    st.write("Dieser Pfad ist fertig.")

                elif h2s == "keine H2S-Produktion auf TSI-Agar":
                    st.success("""
Bakterien: Shigella, Yersinia
""")
                    st.write("Dieser Pfad ist fertig.")

elif morphologie == "gekrümmte Bakterien":
    st.info("""
Gemeinsame Eigenschaften:
- oxidase positiv
- Glukose-Verwertung
- Laktose-negativ
""")

    if "gekruemmt" not in st.session_state:
        st.session_state.gekruemmt = None

    gekruemmt = st.radio(
        "Welches Zusatzmerkmal liegt vor?",
        ["Wachstum bei 42°C", "Wachstum im alkalischen Medium", "produziert Urease"],
        key="gekruemmt",
        index=None
    )

    if gekruemmt == "Wachstum bei 42°C":
        st.success("""
Bakterium: Campylobacter jejuni
""")
        st.write("Dieser Pfad ist fertig.")

    elif gekruemmt == "Wachstum im alkalischen Medium":
        st.success("""
Bakterium: Vibrio cholerae (mikroaerophil)
""")
        st.write("Dieser Pfad ist fertig.")

    elif gekruemmt == "produziert Urease":
        st.success("""
Bakterium: Helicobacter pylori (mikroaerophil)
""")
        st.write("Dieser Pfad ist fertig.")

elif morphologie == "Kokkenbazillen":
    st.success("""
Bakterien:
- Haemophilus influenzae
- Bordetella pertussis
- Pasteurella
- Brucella
- Francisella tularensis
- Acinetobacter baumannii
- Coxiella
""")
    st.write("Dieser Pfad ist fertig.")
