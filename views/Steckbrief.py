import streamlit as st

def lade_css():
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

lade_css()

st.markdown("""
<div class="custom-card">
    <h1>Bakterien Steckbriefe</h1>
    <p class="small-note">
        Hier wird dir jedes Bakterium mit einem Steckbrief beschrieben, damit du die wichtigsten Informationen auf einen Blick hast. 
    </p>
</div>
""", unsafe_allow_html=True)

steckbriefe = [
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Listerien",
        "inhalt": """
- Stäbchenförmige Bakterien
- Wichtigste krankmachende Art: Listeria monocytogenes
- Beweglich durch Geißeln
- Vermehren sich auch bei Kühlschranktemperaturen (ca. 4 °C)
- Sehr widerstandsfähig gegen Umweltbedingungen 
- Listerien können die Krankheit Listeriose auslösen.
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Bacillus",
        "inhalt": """
- Stäbchenförmige Bakterien
- Können Sporen bilden
- Viele Arten beweglich durch Geißeln
- Meist aerob 
- Wichtige Arten:
   - Bacillus subtilis: Meist harmlos, wird in der Forschung genutzt
   - Bacillus cereus: Kann Lebensmittelvergiftungen verursachen
   - Bacillus anthracis: Erreger von Milzbrand
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Corynebakterien",
        "inhalt": """
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
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Clostridien",
        "inhalt": """
- Stäbchenförmige Bakterien
- Viele Arten leben im Boden oder im Darm von Mensch und Tier
- Bilden widerstandsfähige Sporen
- Meist aerob
- Vorbeugung durch gute Hygiene und Tetanusimpfung                
- Wichtige Arten:
    - Clostridium tetani: Verursacht Wundstarrkrampf (Tetanus)
    - Clostridium botulinum: Bildet das Botulinumtoxin                                                                                                               
    - Clostridium difficile: Kann schwere Darminfektionen verursachen
    - Clostridium perfringens: Verursacht Lebensmittelvergiftungen
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Cutibakterien",
        "inhalt": """
- Stäbchenförmige Bakterien
- Früherer Name: Propionibacterium
- Gehören zur normalen Hautflora
- Wachsen bevorzugt ohne Sauerstoff (anaerob)
- Wichtige Arten
    - Cutibacterium acnes → beteiligt an Akne  
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Staphylococcus aureus",
        "inhalt": """
- Kugelförmig (Kokken), traubenförmig angeordnet
- Katalase positiv
- Koagulase positiv
- Beta-Hämolyse
- Widerstandsfähig gegen Umwelteinflüsse
- Bildet oft gelbliche Kolonien („aureus“ = golden)
- Manche Stämme sind antibiotikaresistent
- Wichtige Form:
    - MRSA = Methicillin-resistenter Staphylococcus aureus
    → resistent gegen viele Antibiotika
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Staphylococcus epidermidis",
        "inhalt": """
- Kugelförmiges Bakterium (Kokken)
- Katalase positiv
- Koagulase negativ
- Keine Hämolyse                                               
- Teil der normalen Hautflora des Menschen                
- Novobiocinsensitiv
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Staphylococcus saprophyticus",
        "inhalt": """
- Kugelförmig (Kokken), traubenförmig angeordnet
- Fakultativ pathogen (meist harmlos, kann aber Krankheiten auslösen)
- Katalase positiv
- Koagulase negativ
- Novobiocinresistent 
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Streptococcus pneumoniae",
        "inhalt": """
- Kugelförmig (Kokken), meist paarweise angeordnet (Diplokokken)
- Pneumokokken
- Bakterium mit schützender Kapsel (wichtig für die Krankheitsauslösung) – schleimige Kolonien
- Opportunistischer Erreger (macht vor allem bei geschwächtem Körper krank)
- Alpha-Hämolyse 
- Katalase negativ
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Streptococcus pyogenes",
        "inhalt": """
- Kugelförmig (Kokken), kettenförmig angeordnet
- Gehört zur Gruppe A der Streptokokken (A-Streptokokken)
- Produziert verschiedene Giftstoffe (Toxine)
- Beta-Hämolyse
- Katalase negativ 
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Streptococcus agalactiae",
        "inhalt": """
- Kugelförmig (Kokken), kettenförmig angeordnet
- B-Streptokokken (GBS = Group B Streptococcus)
- Wichtiger Erreger bei Neugeboreneninfektionen
- Beta-Hämolyse
- Katalase negativ
- CAMP positiv
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Streptococcus bovis",
        "inhalt": """
- Kugelförmiges Bakterium (Kokken)
- Meist anaerob oder fakultativ anaerob
- Bilden Ketten aus mehreren Bakterienzellen
- Teil der normalen Darmflora
- PYR-Wachstum
- Wachstum in 6.5 % NaCl
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Enterococcus",
        "inhalt": """
- Kugelförmige Bakterien (Kokken), meist paarweise oder in kurzen Ketten
- Sehr widerstandsfähig gegen Austrocknung und Hitze
- Katalase negativ
- Wachstum in 6.5 % NaCl
- Aesculin positiv
- Wichtige Arten:
    - Enterococcus faecalis
    - Enterococcus faecium
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Nocardia",
        "inhalt": """
- Verzweigte, fadenförmige Bakterien
- Obligat aerob
- Teilweise säurefest
- Verursachen Nokardiose
- Verursachen opportunistische Infektionen
"""
    },
    {
        "gruppe": "Grampositive Bakterien",
        "name": "Actinomyces",
        "inhalt": """
- Verzweigte, fadenartige Stäbchen (sehen „pilzähnlich“ aus)
- Anaerob oder mikroaerophil (leben schlecht mit viel Sauerstoff)
- Nicht säurefest
- Katalase variabel                
- Wichtige Art:
    - Actinomyces israelii 
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Neisseria meningitidis",
        "inhalt": """
- Kugelförmige Bakterien (Diplokokken – paarweise)
- Meningokokken
- Kann schwere, schnell verlaufende Infektionen auslösen
- Besitzt eine Kapsel (wichtig für die Krankheitsauslösung)
- Aerob
- Maltoseverwerter
- Wachstum auf GC-Platte                
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Neisseria gonorrhoeae",
        "inhalt": """
- Bohnenförmige Diplokokken
- Gonokokken
- Aerob
- Oxidase positiv
- Wachstum auf GC-Platte  
- Katalase positiv
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Moraxella",
        "inhalt": """
- Kugelförmige Bakterien (Diplokokken, paarweise)
- Aerob
- Kein Maltoseverwerter
- Wichtige Art:
    - Moraxella catarrhalis
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Campylobacter jejuni",
        "inhalt": """
- Gebogene, spiral- oder kommaförmige Stäbchen
- Einer der häufigsten Erreger von bakteriellen Durchfallerkrankungen
- Oxidase positiv
- Beweglich durch Geißeln (schraubenartige Bewegung)
- Wächst bevorzugt bei Körpertemperatur (ca. 42 °C)
- Sehr empfindlich gegenüber Austrocknung und Sauerstoff
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Vibrio cholerae",
        "inhalt": """
- Kommaförmige, gebogene Stäbchen
- Stark beweglich durch polare Geißel
- Fakultativ anaerob
- Oxidase positiv
- Obligat pathogen                
- Verursacht Cholera
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Helicobacter pylori",
        "inhalt": """
- Spiral- bzw. schraubenförmig
- Kann im sehr sauren Milieu des Magens überleben
- Bildet das Enzym Urease
- Oxidase positiv
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "E. coli",
        "inhalt": """
- Stäbchenförmiges Bakterium
- Häufigster natürlicher Bewohner des menschlichen Darms
- Einige Stämme sind krankheitserregend
- Aerob 
- Schnelle Laktosefermentation 
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Klebsiella",
        "inhalt": """
- Kurze Stäbchen
- Stark ausgeprägte Kapsel (Schleimbildung)
- Nicht beweglich
- Fakultativ anaerob
- Laktosefermentation
- Opportunisten
- Wichtigste Art:   
    - Klebsiella pneumoniae
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Enterobacter",
        "inhalt": """
- Stäbchenförmiges Bakterium
- Häufig in Umwelt und Darm vorkommend, teils Krankenhauskeim
- Aerob
- Schnelle Laktosefermentation
- Wichtige Arten:
    - Enterobacter cloacae (medizinisch besonders relevant)
    - Enterobacter aerogenes (heute oft als Klebsiella aerogenes eingeordnet) 
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Citrobacter",
        "inhalt": """
- Stäbchenförmiges Bakterium
- Kommt häufig im Darm und in der Umwelt vor
- Opportunistischer Erreger
- Aerob
- Langsame Laktosefermentation
- Wichtige Arten:
    - Citrobacter freundii (am häufigsten medizinisch relevant)
    - Citrobacter koseri (besonders bei Neugeborenen wichtig)
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Serratia",
        "inhalt": """
- Stäbchenförmiges Bakterium
- Kann rötliche Farbstoffe bilden
- Wasser und feuchte Umgebungen
- Opportunistischer Erreger
- Aerob
- Langsame Laktosefermentation
- Wichtige Art: 
    - Serratia marcescens
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Pseudomonas aeruginosa",
        "inhalt": """
- Schlanke Stäbchen (Bazillen)
- Stark beweglich durch polare Geißeln
- Flache Kolonien
- Oxidase positiv
- Obligat aerob                
- Keine Laktosefermentation
- Lindenblütenduft                
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Legionella",
        "inhalt": """
- Stäbchenförmiges Bakterium
- Lebt bevorzugt in warmem Wasser und kann schwere Lungenentzündung verursachen
- Aerob
- Keine Laktosefermentation
- Oxidase positiv
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Burkholderia",
        "inhalt": """
- Stäbchenförmiges Bakterium
- Umweltbakterien, einige Arten sind wichtige Krankheitserreger
- Können Biofilme bilden
- Aerob
- Keine Laktosefermentation
- Oxidase positiv
- Wichtige Arten:
    - Burkholderia pseudomallei
    - Burkholderia cepacia (Komplex)
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Salmonella enterica",
        "inhalt": """
- Stäbchen (Bazillen)
- Beweglich
- Fakultativ anaerob
- Keine Laktosefermentation
- Wächst auf HEKT-Platte schwarz
- Verursacht häufig Gastroenteritis
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Proteus",
        "inhalt": """
- Stäbchenförmiges Bakterium
- Sehr beweglich („Schwarmbewegung“) und typischer Harnwegskeim
- Kann Harnstoff spalten (Urease-positiv)
- Aerob
- Oxidase negativ                
- Keine Laktosefermentation
- Schwefelwasserstoffbildung auf TSI-Agar
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Shigella",
        "inhalt": """
- Stäbchenförmiges Bakterium
- Sehr infektiös – schon wenige Bakterien reichen für eine Infektion
- Aerob
- Oxidase negativ
- Keine Laktosefermentation
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Yersinia",
        "inhalt": """
- Kleine Stäbchen
- Fakultativ anaerob
- Wächst gut bei kühlen Temperaturen
- Unbeweglich
- Keine Laktosefermentation
- Oxidase negativ   
- Wichtige Arten:
    - Yersinia pestis: nicht beweglich 
    - Yersinia enterocolitica: beweglich bei niedrigen Temperaturen                                            
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Bacteroides",
        "inhalt": """
- Stäbchenförmiges Bakterium
- Obligate Anaerobier (leben nur ohne Sauerstoff)
- Wichtigster Bestandteil der menschlichen Darmflora
- Wichtige Arten:
    - Bacteroides fragilis (medizinisch besonders wichtig)
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Haemophilus influenzae",
        "inhalt": """
- Kleine Stäbchen
- Kapsel
- Verursachen Meningitis, Epiglottitis, Otitis media
- Wachstum auf Schoggi-Platte
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Bordetella pertussis",
        "inhalt": """
- Kokkoide Stäbchen
- Obligat aerob
- Toxinbildung
- Impfung vorhanden    
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Pasteurella multocida",
        "inhalt": """
- Kleine Stäbchen
- Bestandteile der Tierflora
- Übertragung durch Biss/Kratzer
- Schnelle lokale Ausbreitung
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Brucella",
        "inhalt": """
- Kleine Stäbchen
- Katalase positiv
- Oxidase positiv
- Häufigste Laborinfektion                
- Zoonose
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Francisella tularensis",
        "inhalt": """
- Sehr kleine Stäbchen
- Hochinfektiös
- Übertragung durch Zecken, Tiere
- Potentiell schwerer Verlauf
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Acinetobacter baumannii",
        "inhalt": """
- Kokkoide Stäbchen
- Aerob
- Non-fermenter
- Multiresistent
- Typischer Krankenhauskeim
"""
    },
    {
        "gruppe": "Gramnegative Bakterien",
        "name": "Coxiella burnetii",
        "inhalt": """
- Obligat intrazellulär
- Extrem widerstandsfähig
- Verursacht Q-Fieber
"""
    }
]

aktuelle_gruppe = None
for bakterium in steckbriefe:
    if bakterium["gruppe"] != aktuelle_gruppe:
        st.markdown(f"## {bakterium['gruppe']}")
        aktuelle_gruppe = bakterium["gruppe"]

    with st.expander(f"**{bakterium['name']}**"):
        st.markdown(bakterium["inhalt"])
