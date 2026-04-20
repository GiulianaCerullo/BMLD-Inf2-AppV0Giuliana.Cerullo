import streamlit as st

st.title("Gram-negative Bakterien identifizieren")

morphologie = st.radio(
    "Wähle die Morphologie:",
    ["Diplokokken", "Bazillen", "gekrümmte Bakterien", "Kokkenbazillen"]
)

if morphologie == "Diplokokken":
    st.info("""
Gemeinsame Eigenschaften:
- aerob
- oxidase positiv
""")

    maltose = st.radio(
        "Wird Maltose verwertet?",
        ["Maltose-Verwertung", "keine Maltose-Verwertung"]
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
    sauerstoff = st.radio(
        "Wie ist das Sauerstoffverhalten?",
        ["anaerob", "aerob"]
    )

    if sauerstoff == "anaerob":
        st.success("""
Bakteriengruppe: anaerobe gramnegative Bazillen
Beispiele: Bacteroides, Fusobakterien
""")
        st.write("Dieser Pfad ist fertig.")

    elif sauerstoff == "aerob":
        laktose = st.radio(
            "Wird Laktose verwertet?",
            ["Laktose-Verwertung", "keine Laktose-Verwertung"]
        )

        if laktose == "Laktose-Verwertung":
            oxidase_laktose = st.radio(
                "Wie ist das Oxidase-Verhalten?",
                ["oxidase negativ (schnell)", "oxidase negativ (langsam)"]
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
            oxidase_keine_laktose = st.radio(
                "Wie ist das Oxidase-Verhalten?",
                ["oxidase positiv", "oxidase negativ"]
            )

            if oxidase_keine_laktose == "oxidase positiv":
                st.success("""
Bakterien: Pseudomonas, Legionella, Burkholderia
Merkmal: Non-Fermenter
""")
                st.write("Dieser Pfad ist fertig.")

            elif oxidase_keine_laktose == "oxidase negativ":
                h2s = st.radio(
                    "Liegt eine H2S-Produktion auf TSI-Agar vor?",
                    ["H2S-Produktion auf TSI-Agar", "keine H2S-Produktion auf TSI-Agar"]
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

    gekruemmt = st.radio(
        "Welches Zusatzmerkmal liegt vor?",
        ["Wachstum bei 42°C", "Wachstum im alkalischen Medium", "produziert Urease"]
    )

    if gekruemmt == "Wachstum bei 42°C":
        st.success("""
Bakterium: Campylobacter jejuni
""")
        st.write("Dieser Pfad ist fertig.")

    elif gekruemmt == "Wachstum im alkalischen Medium":
        st.success("""
Bakterium: Vibrio cholerae
Merkmal: mikroaerophil
""")
        st.write("Dieser Pfad ist fertig.")

    elif gekruemmt == "produziert Urease":
        st.success("""
Bakterium: Helicobacter pylori
Merkmal: mikroaerophil
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
