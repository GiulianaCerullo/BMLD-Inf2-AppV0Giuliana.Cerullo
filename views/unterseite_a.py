import streamlit as st

st.title("Gram-positive Bakterien identifizieren")

morphologie = st.radio(
    "Wähle die Morphologie:",
    ["Kokken", "Bazillen", "fadenförmige Bakterien"]
)

if morphologie == "Kokken":
    katalase = st.radio(
        "Wie ist der Katalase-Test?",
        ["Katalase positiv", "Katalase negativ"]
    )

    if katalase == "Katalase positiv":
        st.write("=> Staphylokokken")

        koagulase = st.radio(
            "Wie ist der Koagulase-Test?",
            ["Koagulase positiv", "Koagulase negativ"]
        )

        if koagulase == "Koagulase positiv":
            st.success("""
Bakterium: S. aureus
""")
            st.write("Dieser Pfad ist fertig.")

        elif koagulase == "Koagulase negativ":
            novobiocin = st.radio(
                "Wie ist der Novobiocin-Test?",
                ["Novobiocin empfindlich", "Novobiocin resistent"]
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
        kettenform = st.radio(
            "Wie liegen die Kokken vor?",
            ["lange/paar Ketten", "kurze Ketten"]
        )

        if kettenform == "lange/paar Ketten":
            haemolyse = st.radio(
                "Welche Hämolyse liegt vor?",
                ["alpha-Hämolyse", "beta-Hämolyse", "gamma-Hämolyse"]
            )

            if haemolyse == "alpha-Hämolyse":
                alpha_typ = st.radio(
                    "Wie stark ist die alpha-Hämolyse?",
                    ["starke alpha-Hämolyse", "leichte alpha-Hämolyse"]
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
                beta_typ = st.radio(
                    "Wie stark ist die beta-Hämolyse?",
                    ["viel beta-Hämolyse", "wenig beta-Hämolyse"]
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
    sauerstoff = st.radio(
        "Wie ist das Sauerstoffverhalten?",
        ["anaerob", "aerob"]
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
    sauerstoff = st.radio(
        "Wie ist das Sauerstoffverhalten?",
        ["anaerob", "aerob"]
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
