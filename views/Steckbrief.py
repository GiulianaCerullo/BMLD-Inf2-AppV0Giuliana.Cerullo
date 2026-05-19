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
- Oft unregelmässige Anordnung („V-“ oder „Y-Form“)
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

with st.expander("**Streptococcus pneumoniae"):
    st.markdown("""
- Kugelförmig (Kokken), meist paarweise angeordnet (Diplokokken)
- Pneumokokken
- Bakterium mit schützender Kapsel (wichtig für Krankheitsauslösung)-schleimige Kolonien
- Opportunistischer Erreger (macht vor allem bei geschwächtem Körper krank)
- Alpha-Hämolyse 
- Katalase negativ
""")

with st.expander("**Streptococcus pyogenes**"):
    st.markdown("""
- Kugelförmig (Kokken), kettenförmig angeordnet
- Gehört zur Gruppe A der Streptokokken (A-Streptokokken)
- Produziert verschiedene Giftstoffe (Toxine)
- Betha-Hämolyse
- Katalase negativ 
""")

with st.expander("**Streptococcus agalactiae**"):
    st.markdown("""
- Kugelförmig (Kokken), kettenförmig angeordnet
- B-Streptokokken (GBS = Group B Streptococcus)
- Wichtiger Erreger bei Neugeboreneninfektionen
- Betha-Hämolyse
- Katalase negativ
- CAMP positiv
""")
 
with st.expander("**Streptococcus bovis**"):
    st.markdown("""
- Kugelförmiges Bakterium (Kokken)
- Meist anaerob oder fakultativ anaerob
- Bilden Ketten aus mehreren Bakterienzellen
- Teil der normalen Darmflora
- PYR Wachstum
- Wachstum in 6.5% Nacl
""")

with st.expander("**Enterococcus**"):
    st.markdown("""
- Kugelförmige Bakterien (Kokken), meist paarweise oder in kurzen Ketten
- Sehr widerstandsfähig gegen Austrocknung und Hitze
- Katalase negativ
- Wachstum in 6.5% NaCl
- Aesculin positiv
- Wichtige Arten:
    - Enterococcus faecalis
    - Enterococcus faecium
""")

with st.expander("**Nocardia**"):
    st.markdown("""
- Verzweigte, fadenförmige Bakterien
- Obligat aerob
- Teilweise säurefest
- Verursachen Nokardiose
- Verursachen opportunistische Infektionen
""")

with st.expander("**Actinomyces**"):
    st.markdown("""
- Verzweigte, fadenartige Stäbchen (sehen „pilzähnlich“ aus)
- Anaerob oder mikroaerophil (leben schlecht mit viel Sauerstoff)
- Nicht säurefest
- Katalase variabel                
- Wichtige Art
    - Actinomyces israelii 
""")
    
st.markdown("##Gramnegativ")

with st.expander("**Neisseria meningitidis"):
    st.markdown("""
- Kugelförmige Bakterien (Diplokokken – paarweise)
- Meningokokken
- Kann schwere, schnell verlaufende Infektionen auslösen
- Besitzt eine Kapsel (wichtig für Krankheitsauslösung)
- Aerob
- Maltosverwerter
- Wachstum auf GC-Platte                
""")

with st.expander("**Neisseria gonorrhoeae**"):
    st.markdown("""
- Bohnenförmige Diplokokken
- Gonokokken
- Aerob
- Oxidase positiv
- Wachstum auf GC-Platte  
- Katalase positiv
""")
    
with st.expander("**Moraxella**"):
    st.markdown("""
- Kugelförmige Bakterien (Diplokokken, paarweise)
- Aerob
- Kein Maltoseverwerter
- Wichtige Art
    - Moraxella catarrhalis
""")                

with st.expander("**Campylobacter jejuni**"):
    st.markdown("""
- Gebogene, spiral- oder kommaförmige Stäbchen
- Einer der häufigsten Erreger von bakteriellen Durchfallerkrankungen
- Oxidase positiv
- Beweglich durch Geisseln (schraubenartige Bewegung)
- Wächst bevorzugt bei Körpertemperatur (ca. 42 °C)
- Sehr empfindlich gegenüber Austrocknung und Sauerstoff
""")

with st.expander("**Vibrio cholerae**"):
    st.markdown("""
- Kommaförmige, gebogene Stäbchen
- Stark beweglich durch polare Geissel
- Fakultativ anaerob
- Oxidase positiv
- Obligat Pathogen                
- Verursacht Cholera
""")

with st.expander("**Helicobacter pylori**"):
    st.markdown("""
- Spiral- bzw. schraubenförmig
- Kann im sehr sauren Milieu des Magens überleben
- Bildet das Enzym Urease
- Oxidase positiv
""")

with st.expander("**E.coli**"):
    st.markdown("""
- Stäbchenförmiges Bakterium
- Häufigster natürlicher Bewohner des menschlichen Darms
- Einige Stämme sind krankheitserregend
- Aerob 
- Schnelle Laktosefermentation 
""")

with st.expander("**Klebsiella**"):
    st.markdown("""
- Kurze Stäbchen
- Stark ausgeprägte Kapsel (schleimbildung)
- Nicht beweglich
- Fakultativ anaerob
- Laktosefermentation
- Opportunisten
- Wichtigste Art:   
    - Klebsiella pneumoniae
""")

with st.expander("**Enterobacter**"):
    st.markdown("""
- Stäbchenförmiges Bakterium
- Häufig in Umwelt und Darm vorkommend, teils Krankenhauskeim
- Aerob
- Schnelle Laktosefermentation
- Wichtige Arten:
    - Enterobacter cloacae (medizinisch besonders relevant)
    - Enterobacter aerogenes (heute oft als Klebsiella aerogenes eingeordnet) 
""")

with st.expander("**Citrobacter**"):
    st.markdown("""
- Stäbchenförmiges Bakterium
- Kommt häufig im Darm und in der Umwelt vor
- Opportunistischer Erreger
- Aerob
- Langsame Laktosefermentation
- Wichtige Arten:
    - Citrobacter freundii (am häufigsten medizinisch relevant)
    - Citrobacter koseri (besonders bei Neugeborenen wichtig)
""")

with st.expander("**Serratia**"):
    st.markdown("""
- Stäbchenförmiges Bakterium
- Kann rötliche Farbstoffe bilden
- Wasser und feuchte Umgebungen
- Opportunistischer Erreger
- Aerob
- Langsame Laktosefermentation
- Wichtige Art: 
    - Serratia marcescens
""")

with st.expander("**Pseudomonas aeruginosa**"):
    st.markdown("""
- Schlanke Stäbchen (Bazillen)
- Stark beweglich durch polare Geisseln
- Flache Kolonien
- Oxidase positiv
- Obligat aerob                
- Keine Laktosefermentation$
- Lindenbütenduft                
""")

with st.expander("**Legionella**"):
    st.markdown("""
- Stäbchenförmiges Bakterium
- Lebt bevorzugt in warmem Wasser und kann schwere Lungenentzündung verursachen
- Aerob
- Keine Laktosefermentation
- Oxidase positiv
""")

with st.expander("**Burkholderia**"):
    st.markdown("""
- Stäbchenförmiges Bakterium
- Umweltbakterien, einige Arten sind wichtige Krankheitserreger
- Können Biofilme bilden
- Aerob
- Keine Laktosefermentation
- Oxidase positiv
- Wichtige Arten
    - Burkholderia pseudomallei
    - Burkholderia cepacia (Komplex)
""")
    
with st.expander("**Salmonella enterica**"):
    st.markdown("""
- Stäbchen (Bazillen)
- Beweglich
- Fakultativ anaerob
- Keine Laktosefermentation
- Wächst auf HEKT-Platte schwarz
- Verursacht häufig Gastroentetitis
""")

with st.expander("**Proteus**"):
    st.markdown("""
- Stäbchenförmiges Bakterium
- Sehr beweglich („Schwarmbewegung“) und typischer Harnwegskeim
- Kann Harnstoff spalten (Urease-positiv)
- Aerob
- Oxidase negativ                
- Keine Laktosefermentation
- Schwefelwasserstoffbildun auf TSI-Agar
""")

with st.expander("**Shigella**"):
    st.markdown("""
- Stäbchenförmiges Bakterium
- Sehr infektiös – schon wenige Bakterien reichen für eine Infektion
- Aerob
- Oxidase negativ
- Keine Laktosefermentation
""")

with st.expander("**Yersinia**"):
    st.markdown("""
- Kleine Stäbchen
- Fakultativ anaerob
- Wächstum gut bei kühlen Temperaturen                                
- Unbeweglich
- Keine Laktosefermentation
- Oxidase negativ   
- Wichtige Arten:
    - Yersinia pestis: nicht beweglich 
    - Yersinia enterocolitica: beweglich bei niedrigen Temperaturen                                            
""")
    
with st.expander("**Bacteroides**"):
    st.markdown("""
- Stäbchenförmiges Bakterium
- Obligate Anaerobier (leben nur ohne Sauerstoff
- Wichtigster Bestandteil der menschlichen Darmflora
- Wichtige Arten
    - Bacteroides fragilis (medizinisch besonders wichtig)
""")
    
with st.expander("**Haemophilus influenzae**"):
    st.markdown("""
- Kleine Stäbchen
- Kapsel
- Verursachen Meningitis, Epiglottitis, Otitis media
- Wachstum auf Schoggi-Platte¨
""")

with st.expander("**Bordetetlla pertussis**"):
    st.markdown("""
- Kokkoide Stäbchen
- Obligat aerob
- Toxinbildung
- Impfung vorhanden    
""") 

with st.expander("**Pasteruella multocida**"):
    st.markdown("""
- Kleine Stäbchen
- Bestandteile der Tierflora
- Übertragung durch Biss/Kratzer
- Schnelle lokale Ausbreitung$
""")

with st.expander("**Brucella**"):
    st.markdown("""
- Kleine Stäbchen
- Katalase postitiv
- Oxidase positiv
- Häufigste Laborinfetkion                
- Zoonose
""")

with st.expander("**Francisella tularensis**"):
    st.markdown("""
- Sehr kleine Stäbchen
- Hochinfektiös
- Übertragung durch Zecken, Tiere
- Potentziell schwerer Verlauf
""")

with st.expander("**Acinetobacter baumannii**"):
    st.markdown("""
- Kokkoide Stäbchen
- Aerob
- Non-fermenter
- Multiresistent
- Typischer Krankenhauskeim
""")

with st.expander("**Coxiella burnetii**"):
    st.markdown("""
- Obligat intrazellulär
- Extrem Widerstandsfähig
- Verursacht Q-Fieber
""")                            
