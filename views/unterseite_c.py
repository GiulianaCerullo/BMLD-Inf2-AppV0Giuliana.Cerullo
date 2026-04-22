import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #F8F8FF;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 850px;
}

h1, h2, h3 {
    color: #5a4a7a;
}

div.stButton > button {
    background-color: #8a74b8;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #735fa0;
    color: white;
}

div[data-testid="stRadio"] > label {
    font-weight: 600;
    color: #5a4a7a;
}

.custom-card {
    background-color: white;
    padding: 1.2rem;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
    margin-bottom: 1rem;
}

.small-note {
    color: #6a6280;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="custom-card">
    <h1>Testbeschreibungen</h1>
    <p class="small-note">
        Hier findest du kurze Erklärungen zu wichtigen mikrobiologischen Tests.
    </p>
</div>
""", unsafe_allow_html=True)



with st.expander("**Gram-Färbung**"):
    st.markdown("""
**Prinzip:**  
Die Gram-Färbung unterscheidet Bakterien anhand des Aufbaus ihrer Zellwand. Grampositive Bakterien behalten den Kristallviolett-Farbstoff und erscheinen violett, gramnegative Bakterien werden entfärbt und durch die Gegenfärbung rosa bis rot.  

**Wofür ist der Test wichtig?**  
Die Gram-Färbung ist oft der erste Schritt in der bakteriellen Einordnung, weil sie Morphologie und Zellwandtyp gleichzeitig grob einordnet.  

**Typisches Ergebnis:**  
- Grampositiv → violett  
- Gramnegativ → rosa / rot
""")

with st.expander("**Katalase-Test**"):
    st.markdown("""
**Prinzip:**  
Der Katalase-Test prüft, ob ein Bakterium das Enzym Katalase besitzt. Dieses Enzym spaltet Wasserstoffperoxid in Wasser und Sauerstoff.  

**Durchführung:**  
Zu einer Bakterienkolonie wird Wasserstoffperoxid gegeben.  

**Typisches Ergebnis:**  
- positiv → Bläschenbildung durch frei werdenden Sauerstoff  
- negativ → keine oder kaum Bläschen  

**Wofür ist der Test wichtig?**  
Er hilft zum Beispiel bei der Unterscheidung von Staphylokokken (meist katalase-positiv) und Streptokokken (katalase-negativ).
""")

with st.expander("**Koagulase-Test**"):
    st.markdown("""
**Prinzip:**  
Der Koagulase-Test prüft, ob ein Bakterium Koagulase bildet. Dieses Enzym führt zur Gerinnung von Plasma, indem Fibrinogen zu Fibrin umgewandelt wird.  

**Wofür ist der Test wichtig?**  
Der Test wird klassisch verwendet, um Staphylococcus aureus von koagulase-negativen Staphylokokken zu unterscheiden.  

**Typisches Ergebnis:**  
- positiv → Verklumpung oder Plasmagerinnung  
- negativ → keine Gerinnung
""")

with st.expander("**Oxidase-Test**"):
    st.markdown("""
**Prinzip:**  
Der Oxidase-Test weist das Enzym Cytochrom-c-Oxidase nach, das an der bakteriellen Atmungskette beteiligt ist.  

**Durchführung / Ergebnis:**  
Eine positive Reaktion führt nach Zugabe des Reagenzes zu einer dunklen blau-violetten Färbung. Eine negative Reaktion zeigt keinen entsprechenden Farbumschlag.  

**Wofür ist der Test wichtig?**  
Er hilft unter anderem bei der Unterscheidung oxidase-positiver Bakterien wie Neisseria, Pseudomonas, Campylobacter oder Vibrio von oxidase-negativen Gruppen wie vielen Enterobacteriaceae.
""")

with st.expander("**Maltose-Verwertung**"):
    st.markdown("""
**Prinzip:**  
Hier wird geprüft, ob ein Bakterium Maltose als Kohlenhydrat verwerten bzw. fermentieren kann. Wenn Maltose abgebaut wird, entstehen saure Stoffwechselprodukte und der pH-Wert sinkt.  

**Typisches Ergebnis:**  
- positiv → Farbumschlag des Indikators in den sauren Bereich  
- negativ → kein entsprechender Farbumschlag  

**Wofür ist der Test wichtig?**  
In deinem Schema hilft die Maltose-Verwertung bei der weiteren Einordnung bestimmter gramnegativer Diplokokken.
""")

with st.expander("**Laktose-Verwertung**"):
    st.markdown("""
**Prinzip:**  
Die Laktose-Verwertung prüft, ob ein Bakterium Laktose fermentieren kann. Bei der Fermentation entstehen saure Endprodukte, die einen pH-Indikator umschlagen lassen.  

**Typisches Ergebnis:**  
- positiv → Hinweis auf Laktose-Fermentation, oft mit Farbumschlag ins Gelbe  
- negativ → kein entsprechender Farbumschlag  

**Wofür ist der Test wichtig?**  
Dieser Test ist besonders wichtig bei gramnegativen Stäbchen, weil er bei der Unterscheidung von Laktose-Fermentern und Nicht-Fermentern hilft.
""")

with st.expander("**TSI-Agar und H2S-Produktion**"):
    st.markdown("""
**Prinzip:**  
TSI-Agar (Triple Sugar Iron Agar) dient dazu, Zuckerabbau und H2S-Produktion in einem Medium zu beurteilen. Manche Bakterien bilden aus schwefelhaltigen Bestandteilen Schwefelwasserstoff (H2S).  

**Typisches Ergebnis für H2S:**  
Wenn H2S entsteht, reagiert es mit Eisen im Medium und es entsteht ein schwarzer Niederschlag.  

**Bedeutung:**  
- H2S-positiv → schwarze Verfärbung / schwarzer Niederschlag im Medium  
- H2S-negativ → keine Schwarzfärbung  

**Wofür ist der Test wichtig?**  
In deinem Schema hilft dieser Test bei nicht Laktose-verwertenden, oxidase-negativen gramnegativen Bazillen, zum Beispiel zur Unterscheidung von Salmonella/Proteus gegenüber Shigella/Yersinia.
""")
