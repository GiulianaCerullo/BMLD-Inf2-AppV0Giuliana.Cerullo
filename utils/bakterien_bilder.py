"""Hilfsfunktionen zum Laden und Anzeigen der Bakterienbilder aus dem Word-Dokument."""

from functools import lru_cache
from pathlib import Path
from zipfile import BadZipFile, ZipFile

import streamlit as st


BILDER_DOKUMENTPFADE: tuple[Path, ...] = (
    Path("Bilder.docx"),
    Path("docs") / "Bilder.docx",
    Path(r"c:\Users\aless\OneDrive - ZHAW\Bilder.docx"),
)

BAKTERIEN_BILDER: dict[str, str] = {
    "S. aureus": "word/media/image1.png",
    "S. epidermidis": "word/media/image2.jpeg",
    "S. saprophyticus": "word/media/image3.jpeg",
    "S. pneumoniae": "word/media/image4.jpeg",
    "S. mutans": "word/media/image5.jpeg",
    "S. pyogenes": "word/media/image6.jpeg",
    "S. agalactiae": "word/media/image7.png",
    "S. bovis": "word/media/image8.jpeg",
    "E. faecium": "word/media/image9.jpeg",
    "E. faecalis": "word/media/image10.jpeg",
    "Listeria": "word/media/image11.jpeg",
    "Bacillus": "word/media/image12.jpeg",
    "Corynebakterium": "word/media/image13.jpeg",
    "Clostridium": "word/media/image14.jpeg",
    "Cutibacterium acnes": "word/media/image15.jpeg",
    "Nocardia": "word/media/image16.jpeg",
    "Actinomyces": "word/media/image17.jpeg",
    "N. meningitidis": "word/media/image19.jpeg",
    "Moraxella catarrhalis": "word/media/image20.png",
    "N. gonorrhoeae": "word/media/image21.jpeg",
    "Bacteroides": "word/media/image22.jpeg",
    "Fusobakterien": "word/media/image23.jpeg",
    "Enterobacter cloacae": "word/media/image24.jpeg",
    "Klebsiella oxytoca": "word/media/image25.jpeg",
    "E. coli": "word/media/image26.jpeg",
    "Serratia liquefaciens": "word/media/image27.jpeg",
    "Citrobacter freundii": "word/media/image28.jpeg",
    "Pseudomonas aeruginosa": "word/media/image29.png",
    "Legionella pneumophila": "word/media/image30.jpeg",
    "Burkholderia cepacia": "word/media/image31.jpeg",
    "Salmonella typhimurium": "word/media/image32.jpeg",
    "Proteus vulgaris": "word/media/image33.jpeg",
    "Shigella dysenteriae": "word/media/image34.jpeg",
    "Yersinia": "word/media/image35.jpeg",
    "Campylobacter jejuni": "word/media/image36.jpeg",
    "Vibrio cholerae": "word/media/image37.jpeg",
    "Helicobacter pylori": "word/media/image38.jpeg",
    "Haemophilus influenzae": "word/media/image39.png",
    "Bordetella pertussis": "word/media/image40.jpeg",
    "Pasteurella": "word/media/image41.jpeg",
    "Brucella abortus": "word/media/image42.jpeg",
    "Francisella tularensis": "word/media/image43.jpeg",
    "Acinetobacter baumannii": "word/media/image44.jpeg",
    "Coxiella": "word/media/image45.jpeg",
}


def finde_bilder_dokument() -> Path | None:
    """Gibt den ersten vorhandenen Pfad zum Word-Dokument mit den Bakterienbildern zurück."""
    for pfad in BILDER_DOKUMENTPFADE:
        if pfad.exists():
            return pfad
    return None


@lru_cache(maxsize=1)
def lade_bilder_aus_dokument() -> dict[str, bytes]:
    """Lädt die benötigten Bilddateien aus Bilder.docx als Bytes in den Speicher."""
    dokument_pfad = finde_bilder_dokument()

    if dokument_pfad is None:
        return {}

    try:
        with ZipFile(dokument_pfad) as dokument:
            bilder: dict[str, bytes] = {}
            for bild_pfad in set(BAKTERIEN_BILDER.values()):
                try:
                    bilder[bild_pfad] = dokument.read(bild_pfad)
                except KeyError:
                    continue
            return bilder
    except (BadZipFile, OSError):
        return {}


def zeige_bakterienbilder(bakteriennamen: list[str]) -> None:
    """Zeigt passende Bakterienbilder an und bleibt stabil, falls ein Bild fehlt."""
    bilder = lade_bilder_aus_dokument()
    sichtbare_bilder: list[tuple[str, bytes]] = []
    fehlende_bilder: list[str] = []

    for bakterienname in bakteriennamen:
        bild_pfad = BAKTERIEN_BILDER.get(bakterienname)
        bilddaten = bilder.get(bild_pfad) if bild_pfad else None

        if bilddaten is None:
            fehlende_bilder.append(bakterienname)
        else:
            sichtbare_bilder.append((bakterienname, bilddaten))

    if sichtbare_bilder:
        for start in range(0, len(sichtbare_bilder), 3):
            zeile = sichtbare_bilder[start:start + 3]
            spalten = st.columns(len(zeile))

            for spalte, (bakterienname, bilddaten) in zip(spalten, zeile):
                with spalte:
                    st.image(
                        bilddaten,
                        caption=bakterienname,
                        use_container_width=True,
                    )

    if fehlende_bilder:
        st.caption(
            "Bild aktuell nicht verfügbar für: "
            + ", ".join(fehlende_bilder)
        )