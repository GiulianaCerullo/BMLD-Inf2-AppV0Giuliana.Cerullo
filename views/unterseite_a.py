import streamlit as st


st.markdown("""
<style>
.stApp {
    background-color: #eefaf4;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 850px;
}

h1, h2, h3 {
    color: #1f5c4a;
}

div.stButton > button {
    background-color: #2f7d65;
    color: white;
    border-radius: 14px;
    border: none;
    padding: 0.65rem 1.1rem;
    font-weight: 600;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.12);
}

div.stButton > button:hover {
    background-color: #256651;
    color: white;
}

div[data-testid="stRadio"] > label {
    font-weight: 600;
    color: #1f5c4a;
}

div[role="radiogroup"] > label {
    background-color: #ffffff;
    padding: 0.35rem 0.75rem;
    border-radius: 10px;
    margin-bottom: 0.35rem;
    border: 1px solid #d7e9e1;
}

.custom-card {
    background-color: white;
    padding: 1.2rem;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
    margin-bottom: 1rem;
}

.small-note {
    color: #4d6b60;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="custom-card">
    <h1>Gram-positive Bakterien identifizieren</h1>
    <p class="small-note">
        Wähle Schritt für Schritt die passenden Merkmale aus, um grampositive Bakterien einzuordnen.
    </p>
</div>
""", unsafe_allow_html=True)

reset_keys = [
    "morphologie",
    "katalase",
    "koagulase",
    "novobiocin",
    "kettenform",
    "haemolyse",
    "alpha_typ",
    "beta_typ",
    "sauerstoff_bazillen",
    "sauerstoff_faden"
]

if st.button("Alles zurücksetzen"):
    for key in reset_keys:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

morphologie = st.radio(
    "Wähle die Morphologie:",
    ["Kokken", "Bazillen", "fadenförmige Bakterien"],
    key="morphologie",
    index=None
)

if morphologie == "Kokken":
    if "katalase" not in st.session_state:
        st.session_state.katalase = None

    katalase = st.radio(
        "Wie ist der Katalase-Test?",
        ["Katalase positiv", "Katalase negativ"],
        key="katalase",
        index=None
    )

    if katalase == "Katalase positiv":
        st.write("=> Staphylokokken")

        if "koagulase" not in st.session_state:
            st.session_state.koagulase = None

        koagulase = st.radio(
            "Wie ist der Koagulase-Test?",
            ["Koagulase positiv", "Koagulase negativ"],
            key="koagulase",
            index=None
        )

        if koagulase == "Koagulase positiv":
            st.success("""
Bakterium: S. aureus
""")
            st.write("Dieser Pfad ist fertig.")

        elif koagulase == "Koagulase negativ":
            if "novobiocin" not in st.session_state:
                st.session_state.novobiocin = None

            novobiocin = st.radio(
                "Wie ist der Novobiocin-Test?",
                ["Novobiocin empfindlich", "Novobiocin resistent"],
                key="novobiocin",
                index=None
            )

            if novobiocin == "Novobiocin empfindlich":
                st.success("""
Bakterium: S. epidermidis
""")
                st.write("Dieser Pfad ist fertig.")

            elif novobiocin == "Novobiocin resistent":
                st.success("""
Bakterium: S. saprophyticus
""")
                st.write("Dieser Pfad ist fertig.")

    elif katalase == "Katalase negativ":
        if "kettenform" not in st.session_state:
            st.session_state.kettenform = None

        kettenform = st.radio(
            "Wie liegen die Kokken vor?",
            ["lange/paar Ketten", "kurze Ketten"],
            key="kettenform",
            index=None
        )

        if kettenform == "lange/paar Ketten":
            if "haemolyse" not in st.session_state:
                st.session_state.haemolyse = None

            haemolyse = st.radio(
                "Welche Hämolyse liegt vor?",
                ["alpha-Hämolyse", "beta-Hämolyse", "gamma-Hämolyse"],
                key="haemolyse",
                index=None
            )

            if haemolyse == "alpha-Hämolyse":
                if "alpha_typ" not in st.session_state:
                    st.session_state.alpha_typ = None

                alpha_typ = st.radio(
                    "Wie stark ist die alpha-Hämolyse?",
                    ["starke alpha-Hämolyse", "leichte alpha-Hämolyse"],
                    key="alpha_typ",
                    index=None
                )

                if alpha_typ == "starke alpha-Hämolyse":
                    st.success("""
Bakterium: S. pneumoniae  
Merkmal: Kapselbildung
""")
                    st.write("Dieser Pfad ist fertig.")

                elif alpha_typ == "leichte alpha-Hämolyse":
                    st.success("""
Bakteriengruppe: vergrünende Bakterien (Viridans streptococci)  
Beispiele: S. mutans oder S. mitis  
Merkmal: keine Kapselbildung
""")
                    st.write("Dieser Pfad ist fertig.")

            elif haemolyse == "beta-Hämolyse":
                if "beta_typ" not in st.session_state:
                    st.session_state.beta_typ = None

                beta_typ = st.radio(
                    "Wie stark ist die beta-Hämolyse?",
                    ["viel beta-Hämolyse", "wenig beta-Hämolyse"],
                    key="beta_typ",
                    index=None
                )

                if beta_typ == "viel beta-Hämolyse":
                    st.success("""
Bakterium: S. pyogenes
""")
                    st.write("Dieser Pfad ist fertig.")

                elif beta_typ == "wenig beta-Hämolyse":
                    st.success("""
Bakterium: S. agalactiae
""")
                    st.write("Dieser Pfad ist fertig.")

            elif haemolyse == "gamma-Hämolyse":
                st.success("""
Bakterium: S. bovis
""")
                st.write("Dieser Pfad ist fertig.")

        elif kettenform == "kurze Ketten":
            st.success("""
Bakteriengruppe: Enterococcus  
Beispiele: E. faecium, E. faecalis
""")
            st.write("Dieser Pfad ist fertig.")

elif morphologie == "Bazillen":
    if "sauerstoff_bazillen" not in st.session_state:
        st.session_state.sauerstoff_bazillen = None

    sauerstoff = st.radio(
        "Wie ist das Sauerstoffverhalten?",
        ["anaerob", "aerob"],
        key="sauerstoff_bazillen",
        index=None
    )

    if sauerstoff == "anaerob":
        st.success("""
Bakteriengruppe: anaerobe Bazillen  
Beispiele: Clostridium, Cutibacterium
""")
        st.write("Dieser Pfad ist fertig.")

    elif sauerstoff == "aerob":
        st.success("""
Bakteriengruppe: aerobe Bazillen  
Beispiele: Listeria, Bacillus, Corynebakterium
""")
        st.write("Dieser Pfad ist fertig.")

elif morphologie == "fadenförmige Bakterien":
    if "sauerstoff_faden" not in st.session_state:
        st.session_state.sauerstoff_faden = None

    sauerstoff = st.radio(
        "Wie ist das Sauerstoffverhalten?",
        ["anaerob", "aerob"],
        key="sauerstoff_faden",
        index=None
    )

    if sauerstoff == "anaerob":
        st.success("""
Bakteriengruppe: anaerobe fadenförmige Bakterien  
Beispiel: Actinomyces
""")
        st.write("Dieser Pfad ist fertig.")

    elif sauerstoff == "aerob":
        st.success("""
Bakteriengruppe: aerobe fadenförmige Bakterien  
Beispiel: Nocardia
""")
        st.write("Dieser Pfad ist fertig.")
