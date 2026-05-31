# Finales User-Testing

**Projekt:** Bakterien Identifikations- und Lern-App  
**Testperson:** David Hascher, BMLD-Student im 2. Semester  
**Testdatum:** 27.05.2026  
**Dauer:** ca. 20 Minuten  
**Testgerät:** Laptop  
**Status:** Finales Testing mit der funktionierenden App

---

## 1. Ziel des Tests

Ziel des finalen User-Testings war es, die fertig umgesetzte App mit einer Person aus der Zielgruppe zu testen. Dabei wurde überprüft, ob die App verständlich aufgebaut ist, ob die wichtigsten Funktionen ohne grössere Hilfe verwendet werden können und ob die App beim Lernen und Identifizieren von Bakterien hilfreich ist.

Besonders getestet wurden:

| Bereich | Ziel |
|---|---|
| Navigation | Die wichtigsten Seiten sollen schnell gefunden werden. |
| Grampositive Identifikation | Ein Bakterium soll Schritt für Schritt identifiziert werden können. |
| Gramnegative Identifikation | Ein komplexerer Identifikationspfad soll nachvollziehbar sein. |
| Testbeschreibungen | Fachbegriffe sollen verständlich erklärt werden. |
| Lernmodus | Fragen sollen verständlich beantwortet werden können. |
| Steckbriefe | Informationen zu einzelnen Bakterien sollen schnell auffindbar sein. |

Zusätzlich sollte geprüft werden, ob die App für BMLD-Studierende einen sinnvollen Lernnutzen hat und ob die Inhalte auch ohne zusätzliche Erklärung durch die Entwicklerinnen und Entwickler nachvollziehbar sind.

---

## 2. Testperson

| Angabe | Beschreibung |
|---|---|
| Name | David Hascher |
| Ausbildung | BMLD-Student |
| Semester | 2. Semester |
| Bezug zum Thema | Kennt Grundlagen der Bakterienidentifikation aus dem Studium |
| Gerät | Laptop |
| Datum | 27.05.2026 |
| Dauer | ca. 20 Minuten |

---

## 3. Testdurchführung

Der Test wurde mit der fertig umgesetzten Streamlit-App durchgeführt. David Hascher erhielt nacheinander konkrete Aufgaben und sollte die App möglichst selbstständig bedienen.

Während des Tests wurde beobachtet:

- ob die Navigation verständlich ist
- ob die Identifikationspfade logisch nachvollzogen werden können
- ob die Testbeschreibungen beim Verständnis helfen
- ob der Lernmodus intuitiv nutzbar ist
- ob die Steckbriefe schnell gefunden werden

---

## 4. Hypothesen

| Nr. | Hypothese |
|---|---|
| 1 | David findet sich in der Navigation der App ohne Hilfe zurecht. |
| 2 | David kann ein grampositives Bakterium mithilfe der App identifizieren. |
| 3 | David kann ein gramnegatives Bakterium mithilfe der App identifizieren. |
| 4 | Die Testbeschreibungen helfen dabei, Fachbegriffe besser zu verstehen. |
| 5 | Der Lernmodus ist verständlich und eignet sich zum Wiederholen des Wissens. |
| 6 | Die Steckbriefe sind hilfreich, um wichtige Informationen zu einzelnen Bakterien schnell nachzuschauen. |

---

## 5. Testaufgaben

### Aufgabe 1: App starten und Navigation prüfen

David öffnet die App, meldet sich an und schaut sich die Navigation an.

**Erwartung:** David erkennt die wichtigsten Bereiche der App und versteht, wofür die einzelnen Seiten gedacht sind.

### Aufgabe 2: Grampositives Bakterium identifizieren

David geht zur Seite **Gram-positiv** und wählt folgenden Pfad:

```text
Kokken -> Katalase positiv -> Koagulase positiv
```

**Erwartung:** David kommt zum Ergebnis **Staphylococcus aureus**.

### Aufgabe 3: Gramnegatives Bakterium identifizieren

David geht zur Seite **Gram-negativ** und wählt folgenden Pfad:

```text
Bazillen -> aerob -> keine Laktose-Verwertung -> oxidase negativ -> H2S-Produktion auf TSI-Agar
```

**Erwartung:** David kommt zum Ergebnis **Salmonella / Proteus**.

### Aufgabe 4: Testbeschreibung suchen

David sucht die Beschreibung des **Katalase-Tests**.

**Erwartung:** David findet die Testbeschreibung und versteht den Zweck des Tests.

### Aufgabe 5: Lernmodus verwenden

David öffnet den Lernmodus und beantwortet mehrere Fragen.

**Erwartung:** David versteht, wie er Antworten auswählt und wie das Ergebnis angezeigt wird.

### Aufgabe 6: Steckbrief suchen

David sucht einen Steckbrief zu einem Bakterium, zum Beispiel **Staphylococcus aureus**, **Escherichia coli** oder **Salmonella**.

**Erwartung:** David findet den Steckbrief und kann wichtige Informationen daraus entnehmen.

---

## 6. Testprotokoll

| Aufgabe | Beobachtung | Ergebnis | Verbesserungsidee |
|---|---|---|---|
| App starten und Navigation prüfen | David konnte die App öffnen, sich orientieren und die wichtigsten Seiten in der Navigation erkennen. Die Trennung zwischen Gram-positiv, Gram-negativ, Testbeschreibungen, Lernen und Steckbriefen war nachvollziehbar. | Erfolgreich | Keine zwingende Verbesserung. |
| Grampositives Bakterium identifizieren | Der Pfad `Kokken -> Katalase positiv -> Koagulase positiv` konnte ohne grössere Hilfe ausgewählt werden. Das Ergebnis **Staphylococcus aureus** war verständlich. | Erfolgreich | Bei einzelnen Fachbegriffen könnte ein kurzer Hinweis direkt bei der Auswahl hilfreich sein. |
| Gramnegatives Bakterium identifizieren | Der Pfad `Bazillen -> aerob -> keine Laktose-Verwertung -> oxidase negativ -> H2S-Produktion auf TSI-Agar` konnte abgeschlossen werden. Die Begriffe Oxidase und H2S waren fachlich bekannt, wurden aber als anspruchsvoller empfunden. | Erfolgreich | Fachbegriffe direkt im Identifikationspfad kurz erklären oder mit den Testbeschreibungen verknüpfen. |
| Testbeschreibung suchen | Die Beschreibung des Katalase-Tests wurde schnell gefunden. Die Erklärung war verständlich und passte zum Zweck der App. | Erfolgreich | Keine zwingende Verbesserung. |
| Lernmodus verwenden | David konnte den Lernmodus starten, Fragen beantworten und das Ergebnis nachvollziehen. Die verschiedenen Fragetypen machten den Lernmodus abwechslungsreicher. | Erfolgreich | Ein sichtbarer Verlauf früherer Ergebnisse wäre hilfreich. |
| Steckbrief suchen | Der Steckbrief konnte gefunden werden. Die wichtigsten Informationen zum Bakterium waren übersichtlich dargestellt. | Erfolgreich | Eine Suchfunktion für Steckbriefe wäre für eine spätere Version praktisch. |

---

## 7. Interviewfragen und Antworten

### 1. War die App verständlich aufgebaut?

Ja. Die App war verständlich aufgebaut. Die einzelnen Seiten waren klar voneinander getrennt und die Navigation war logisch.

### 2. Hast du gewusst, wo du klicken musst?

Meistens war klar, wo geklickt werden musste. Bei einigen Fachbegriffen musste kurz überlegt werden, aber die Struktur der App war nachvollziehbar.

### 3. Welche Funktion war am hilfreichsten?

Am hilfreichsten waren die Identifikationspfade und die Testbeschreibungen. Die Identifikationspfade helfen, Schritt für Schritt zum Ergebnis zu kommen. Die Testbeschreibungen helfen, wenn ein Begriff nicht sofort klar ist.

### 4. Was war unklar oder verwirrend?

Teilweise waren Fachbegriffe wie Oxidase, Laktose-Verwertung oder H2S-Produktion anspruchsvoll. Wenn man diese Begriffe nicht mehr gut im Kopf hat, wären kurze Erklärungen direkt bei der Auswahl hilfreich.

### 5. Würdest du die App zum Lernen verwenden?

Ja. Die App wäre vor allem zum Wiederholen vor Praktika oder Prüfungen nützlich. Sie eignet sich gut für kurze Lerneinheiten.

### 6. Was würdest du verbessern?

Hilfreich wären kurze Erklärungen direkt bei schwierigen Auswahlmöglichkeiten, ein sichtbarer Lernfortschritt im Lernmodus und eventuell eine Suchfunktion bei den Steckbriefen.

---

## 8. Auswertung

David konnte die wichtigsten Funktionen der App verwenden. Die Navigation war insgesamt verständlich und die Identifikationspfade konnten nachvollzogen werden. Besonders positiv war, dass die App die komplexe Bakterieneinteilung in einzelne Schritte aufteilt. Dadurch wirkt die Identifikation weniger unübersichtlich als in einer grossen Tabelle oder in einem Skript.

Die Hypothesen konnten grösstenteils bestätigt werden. David fand sich in der Navigation zurecht, konnte beide Identifikationspfade abschliessen und verstand den Zweck des Lernmodus. Die Testbeschreibungen wurden als hilfreich wahrgenommen, besonders wenn ein Fachbegriff nicht sofort klar war. Die App eignet sich deshalb grundsätzlich für kurze Lerneinheiten und zur Wiederholung vor Praktika oder Prüfungen.

### Positiv aufgefallen

- Die Navigation ist klar und die wichtigsten Bereiche sind schnell auffindbar.
- Die Identifikationspfade sind logisch aufgebaut und führen Schritt für Schritt zum Ergebnis.
- Die Testbeschreibungen helfen beim Verständnis der wichtigsten mikrobiologischen Tests.
- Der Lernmodus ist einfach zu bedienen und eignet sich zum Wiederholen.
- Die Steckbriefe bieten eine gute Übersicht zu einzelnen Bakterien.

### Unklar oder schwierig

- Einzelne Fachbegriffe sind anspruchsvoll, wenn man sie nicht mehr gut kennt.
- Bei schwierigen Begriffen wäre eine kurze Erklärung direkt im Identifikationspfad hilfreich.
- Im Lernmodus wird zwar ein Ergebnis angezeigt, ein sichtbarer Verlauf früherer Ergebnisse wäre aber noch besser.
- Bei vielen Steckbriefen wäre eine Suchfunktion praktisch, damit man schneller zum gewünschten Bakterium kommt.

### Technische Probleme

- Es sind beim Test keine grösseren technischen Probleme aufgetreten.
- Die App konnte bedient werden und die getesteten Funktionen waren nutzbar.

---

## 9. Bewertung der Hypothesen

| Hypothese | Bewertung | Begründung |
|---|---|---|
| David findet sich in der Navigation ohne Hilfe zurecht. | Bestätigt | Die wichtigsten Seiten wurden schnell gefunden. |
| David kann ein grampositives Bakterium identifizieren. | Bestätigt | Der Pfad zu **Staphylococcus aureus** wurde erfolgreich abgeschlossen. |
| David kann ein gramnegatives Bakterium identifizieren. | Bestätigt | Der Pfad zu **Salmonella / Proteus** wurde erfolgreich abgeschlossen. |
| Die Testbeschreibungen helfen beim Verständnis der Fachbegriffe. | Bestätigt | Die Beschreibung des Katalase-Tests wurde gefunden und als hilfreich bewertet. |
| Der Lernmodus ist verständlich und eignet sich zum Wiederholen. | Bestätigt | Der Lernmodus konnte ohne grössere Hilfe verwendet werden. |
| Die Steckbriefe helfen beim schnellen Nachschauen. | Bestätigt | Die gesuchten Informationen konnten gefunden werden. |

---

## 10. Schlussfolgerung

Das finale User-Testing zeigt, dass die App grundsätzlich funktionsfähig und für die Zielgruppe verständlich ist. Die wichtigsten Funktionen konnten getestet werden. David konnte die Navigation, die Identifikation grampositiver und gramnegativer Bakterien, die Testbeschreibungen, den Lernmodus und die Steckbriefe nutzen.

Damit erfüllt die App ihr Hauptziel: Sie unterstützt Studierende dabei, Bakterien schrittweise zu identifizieren und wichtige Inhalte in kurzen Lerneinheiten zu wiederholen. Besonders die Kombination aus Identifikationspfaden, Testbeschreibungen, Steckbriefen und Lernmodus passt gut zur Zielgruppe.

Aus dem Test ergeben sich folgende Schlussfolgerungen:

- Die Grundstruktur der App funktioniert für die Zielgruppe gut.
- Die schrittweise Identifikation ist hilfreich, weil sie komplexe Inhalte in kleinere Entscheidungen aufteilt.
- Die Testbeschreibungen sind wichtig, damit Fachbegriffe besser verstanden werden.
- Der Lernmodus ist geeignet, um Wissen zu wiederholen und den Lernstand zu prüfen.
- Für eine zukünftige Version wären kurze Erklärungen direkt bei den Auswahlfragen und eine bessere Anzeige des Lernfortschritts sinnvoll.

---

## 11. Geplante oder umgesetzte Verbesserungen

Aufgrund des finalen User-Testings werden folgende Punkte umgesetzt oder für eine zukünftige Version festgehalten:

| Verbesserung | Priorität | Status |
|---|---|---|
| Schwierige Fachbegriffe direkt im Identifikationspfad kurz erklären | Mittel | Für zukünftige Version |
| Lernfortschritt sichtbarer darstellen, zum Beispiel mit Tabelle oder Diagramm | Mittel | Für zukünftige Version |
| Suchfunktion für Steckbriefe ergänzen | Niedrig | Für zukünftige Version |
| Bestehende Struktur der App beibehalten | Hoch | Wird beibehalten |
| Testbeschreibungen als wichtigen Bestandteil der App beibehalten | Hoch | Wird beibehalten |

---

## 12. Fazit

Das finale User-Testing mit David Hascher zeigt, dass die App für BMLD-Studierende verständlich und nützlich ist. Die wichtigsten Funktionen konnten erfolgreich genutzt werden. Besonders die klare Navigation, die schrittweise Identifikation und der Lernmodus wurden positiv bewertet.

Die App ist damit für die Abgabe in einem funktionsfähigen Zustand. Weitere Verbesserungen betreffen vor allem Komfortfunktionen und zusätzliche Erklärungen, nicht die Grundfunktion der App.
*** End Patch
``` 
