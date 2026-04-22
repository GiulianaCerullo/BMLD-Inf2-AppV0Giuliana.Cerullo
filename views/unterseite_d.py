import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #F0F8FF;
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
    <h1>Bakterien lernen</h1>
    <p class="small-note">
        Hier kannst du mit verschiedenen Lernmethoden üben und dein Wissen wiederholen.
    </p>
</div>
""", unsafe_allow_html=True)


quiz_daten = {
    "Multiple Choice": [
        {
            "frage": "Welches Bakterium gehört zu den gramnegativen Diplokokken und verwertet Maltose?",
            "optionen": ["N. gonorrhoeae", "Moraxella", "N. meningitidis", "Pseudomonas"],
            "antwort": "N. meningitidis"
        },
        {
            "frage": "Welches Bakterium wächst bei 42°C?",
            "optionen": ["Helicobacter pylori", "Campylobacter jejuni", "Vibrio cholerae", "Shigella"],
            "antwort": "Campylobacter jejuni"
        },
        {
            "frage": "Welches Bakterium gehört zu den nicht Laktose-verwertenden, oxidase-positiven gramnegativen Bazillen?",
            "optionen": ["E. coli", "Citrobacter", "Pseudomonas", "Klebsiella"],
            "antwort": "Pseudomonas"
        },
        {
            "frage": "Welches Bakterium ist H2S-positiv auf TSI-Agar?",
            "optionen": ["Shigella", "Yersinia", "Salmonella", "Moraxella"],
            "antwort": "Salmonella"
        }
    ],
    "Richtig / Falsch": [
        {
            "frage": "Campylobacter jejuni wächst bei 42°C.",
            "optionen": ["Richtig", "Falsch"],
            "antwort": "Richtig"
        },
        {
            "frage": "Helicobacter pylori produziert Urease.",
            "optionen": ["Richtig", "Falsch"],
            "antwort": "Richtig"
        },
        {
            "frage": "Shigella ist H2S-positiv auf TSI-Agar.",
            "optionen": ["Richtig", "Falsch"],
            "antwort": "Falsch"
        },
        {
            "frage": "E. coli gehört zu den Laktose-verwertenden gramnegativen Bazillen.",
            "optionen": ["Richtig", "Falsch"],
            "antwort": "Richtig"
        }
    ],
    "Reihenfolge-Fragen": [
        {
            "frage": "Bringe die Schritte der Einteilung gramnegativer Bazillen in die richtige Reihenfolge.",
            "optionen": [
                "Oxidase-Test",
                "Morphologie bestimmen",
                "Laktose-Verwertung prüfen",
                "Sauerstoffverhalten prüfen"
            ],
            "antwort": [
                "Morphologie bestimmen",
                "Sauerstoffverhalten prüfen",
                "Laktose-Verwertung prüfen",
                "Oxidase-Test"
            ]
        },
        {
            "frage": "Bringe die Einteilung der nicht Laktose-verwertenden, oxidase-negativen Bazillen in die richtige Reihenfolge.",
            "optionen": [
                "H2S-Produktion auf TSI-Agar prüfen",
                "Morphologie bestimmen",
                "Oxidase-Test",
                "Laktose-Verwertung prüfen"
            ],
            "antwort": [
                "Morphologie bestimmen",
                "Laktose-Verwertung prüfen",
                "Oxidase-Test",
                "H2S-Produktion auf TSI-Agar prüfen"
            ]
        }
    ]
}

lernmodus = st.radio(
    "Wähle eine Lernmethode:",
    list(quiz_daten.keys())
)

if "quiz_modus" not in st.session_state:
    st.session_state.quiz_modus = lernmodus
    st.session_state.frage_index = 0
    st.session_state.punkte = 0
    st.session_state.beantwortet = False
    st.session_state.feedback = ""

if lernmodus != st.session_state.quiz_modus:
    st.session_state.quiz_modus = lernmodus
    st.session_state.frage_index = 0
    st.session_state.punkte = 0
    st.session_state.beantwortet = False
    st.session_state.feedback = ""

fragen = quiz_daten[lernmodus]
aktuelle_nummer = st.session_state.frage_index
anzahl_fragen = len(fragen)

if aktuelle_nummer < anzahl_fragen:
    frage = fragen[aktuelle_nummer]

    st.write(f"**Frage {aktuelle_nummer + 1} von {anzahl_fragen}**")
    st.progress((aktuelle_nummer) / anzahl_fragen)
    st.subheader(frage["frage"])

    if lernmodus in ["Multiple Choice", "Richtig / Falsch"]:
        auswahl = st.radio(
            "Wähle deine Antwort:",
            frage["optionen"],
            key=f"antwort_{lernmodus}_{aktuelle_nummer}"
        )

        if not st.session_state.beantwortet:
            if st.button("Antwort prüfen"):
                if auswahl == frage["antwort"]:
                    st.session_state.punkte += 1
                    st.session_state.feedback = "Richtig!"
                else:
                    st.session_state.feedback = f"Falsch. Richtig ist: {frage['antwort']}"
                st.session_state.beantwortet = True
                st.rerun()

    elif lernmodus == "Reihenfolge-Fragen":
        user_reihenfolge = []
        for i in range(len(frage["optionen"])):
            schritt = st.selectbox(
                f"Schritt {i+1}",
                frage["optionen"],
                key=f"reihenfolge_{aktuelle_nummer}_{i}"
            )
            user_reihenfolge.append(schritt)

        if not st.session_state.beantwortet:
            if st.button("Reihenfolge prüfen"):
                if user_reihenfolge == frage["antwort"]:
                    st.session_state.punkte += 1
                    st.session_state.feedback = "Richtig!"
                else:
                    richtige_text = " → ".join(frage["antwort"])
                    st.session_state.feedback = f"Falsch. Richtige Reihenfolge: {richtige_text}"
                st.session_state.beantwortet = True
                st.rerun()

    if st.session_state.beantwortet:
        if st.session_state.feedback == "Richtig!":
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

        if st.button("Nächste Frage"):
            st.session_state.frage_index += 1
            st.session_state.beantwortet = False
            st.session_state.feedback = ""
            st.rerun()

    st.info(f"Punktestand: {st.session_state.punkte} / {anzahl_fragen}")

else:
    st.success(f"Quiz beendet! Du hast {st.session_state.punkte} von {anzahl_fragen} Punkten erreicht.")

    if st.session_state.punkte == anzahl_fragen:
        st.balloons()
        st.write("Super gemacht!")
    elif st.session_state.punkte >= anzahl_fragen / 2:
        st.write("Gut gemacht!")
    else:
        st.write("Weiter üben lohnt sich.")

    if st.button("Quiz neu starten"):
        st.session_state.frage_index = 0
        st.session_state.punkte = 0
        st.session_state.beantwortet = False
        st.session_state.feedback = ""
        st.rerun()
