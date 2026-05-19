import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #FFF1DC;
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
    color: #C08457;
    font-size: 0.95rem;
    text-decoration: none;
}
            
html, body, [class*="css"]  {
    color: black;
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


st.markdown("## Grampositiv")
with st.expander("**Listerien**"):
    st.markdown("""
- Stäbchenförmige Bakterien
- Wichtigste krankmachende Art: Listeria monocytogenes
- Beweglich durch Geisseln
- Vermehren sich auch bei Kühlschranktemperaturen (ca. 4 °C)
- Sehr widerstandsfähig gegen Umweltbedingungen 
- Listerien können die Krankheit Listeriose auslösen.
""")

with st.expander("**Bacillus**"):
    st.markdown("""
- Stäbchenförmige Bakterien
- Können Sporen bilden
- Viele Arten beweglich durch Geisseln
- Meist aerob 
- Wichtige Arten:
   - Bacillus Subtilis: Meist harmlos, wird in Forschung genutzt
   - Bacillus cereus: Kann Lebensmittelvergiftungen verursachen                                                                                         
   - Bacillus anthracis: Erreger von Milzbrand
""")

with st.expander("**Corynebakterien**"):
    st.markdown("""
- Keulenförmige Stäbchenbakterien
- Oft unregelmäßige Anordnung („V-“ oder „Y-Form“)
- Unbeweglich
- Bilden keine Sporen
- Aerob
- Bilden schwarze Kolonien               
- Einige Arten sind harmlos und gehören zur normalen Hautflora
- Wichtige Arten: 
    - Corynebacterium diphtheriae → verursacht Diphtherie
    - Corynebacterium jeikeium → kann Krankenhausinfektionen auslösen  
""")

with st.expander("**Clostridien**"):
    st.markdown("""
- Stäbchenförmige Bakterien
- Viele Arten leben im Boden oder im Darm von Mensch und Tier
- Bilden widerstandsfähige Sporen
- Meist aerob
- Vorbeugung durch gute Hygiene und Tetanus Impfung                
- Wichtige Arten:
    - Clostridium tetani: Verursacht Wundstarrkrampf (Tetanus)
    - Clostridium botulinum: Bildet das Botulinumtoxin                                                                                                               
    - Clostridum difficile: Kann schwere Darminfektionen verursachen
    - Clostridium perfringens: Verursacht Lebensmittelvergiftungen
""")

with st.expander("**Cutibakterien**"):
    st.markdown("""
- Stäbchenförmige Bakterien
- Früherer Name: Propionibacterium
- Gehören zur normalen Hautflora
- Wachsen bevorzugt ohne Sauerstoff (anaerob)
- Wichtige Arten
    - Cutibacterium acnes → beteiligt an Akn  
""")

with st.expander("**Staphylococcus aureus**"):
    st.markdown("""
- Kugelförmig (Kokken), traubenförmig angeordnet
- Katalase positiv
- Koagulase positiv
- Betha- Hämolyse
- Widerstandsfähig gegen Umwelteinflüsse
- Bildet oft gelbliche Kolonien („aureus“ = golden)
- Manche Stämme sind antibiotikaresistent
- Wichtige Form:
    - MRSA = Methicillin-resistenter Staphylococcus aureus
    → resistent gegen viele Antibiotika
""")

with st.expander("**Staphylococcus epidermidis**"):
    st.markdown("""
- Kugelförmiges Bakterium (Kokken)
- Katalase positiv
- Koagulase negativ
- keine Hämolyse                                               
- Teil der normalen Hautflora des Menschen                
- Novobiocinsensitiv
""")

with st.expander("**Staphylococcus saprophyticus**"):
    st.markdown("""
- Kugelförmig (Kokken), traubenförmig angeordnet
- Fakultativ pathogen (meist harmlos, kann aber Krankheiten auslösen)
- Katalase positiv
- Koagulase negativ
- Novobiocin resistent 
""")                                                       