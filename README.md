# Abschlussarbeit
# Entwicklung eines automatisierten Feedbacksystems von ER-Modellen

## Ziel: 
- Abgabedatum: 03.03.2025

## Ausblick ✅✅✅
### in Progress  🚀
    - [] Hinzufügen von Magic-Bibliothek 
    - [] Optimierung der Kantenüberprüfung 

### Planning 🚀
    - [] Optimierung der Fehlererkennung bei Knoten
    - [] Überarbeitung der Fehlerlassifizierung bei Folgefehlern
    - [] Erstellen einer GUI 

## Guideline to start
### Projekt klonen

### How to start Docker: 
    - docker build -t er_model_checker . 
    - docker run -p 8000:8000 er_model_checker
    
### Mermaid in Visual Studio Code nutzen 

### Template Code für POST- und GET-API Aufruf in Code-Zelle

## Documentation
### Übersicht der Mermaid-Syntax 
Wichtige Infos: 
* Entitäten die Teil einer IS-A Beziehung sind müssen als erstes definiert werden
* es dürfen keine Leerzeichen in einer Zeile sein (Einrückung am Beginn ist erlaubt)
* zwischen einer (schwachen) Entität und Relationship muss immer eine Kardinalität angegeben werden
* Kardinalitäten werden mit Min-Max-Notation angegeben

| Darstellungselemente | Syntax | Beschreibung | Beispiel in Diagramm |
|----------------------|--------|--------------|----------------------|
| Entität(Subtyp) und Entität(Supertyp) | `Subtyp---IS-A{{IS-A}}---Supertyp` | Stellt eine IS-A Beziehung zwischen einem Subtyp und einem Supertyp von Entitäten dar. | `PKW---IS-A{{IS-A}}---Fahrzeug` |
| Entität(Subtyp) | `Subtyp---IS-A{{IS-A}}` | Stellt eine IS-A Beziehung mit einem Subtyp dar. Supertyp muss zuvor einmalig genannt werden. | `LKW---IS-A{{IS-A}}` |
| Entität | `Entität---AttribuID([Attributname])` | Stellt eine Entität mit Attribut dar.| `Kunde---K1([Name])` |
|         | `schwacheEntität[[schwacheEntität]]---AttributID([Attributname])` | Darstellung einer schwachen Entität. | `Kunde[[Kunde]]---K1([Name)]` |
| Primärschlüssel-Attribut | `Entität---AttributID(["<ins>Attributname</ins>"])` | Stellt eine Entität und ein Primärschlüssel-Attribut dar. | `Land---L1(["<ins>KFZ</ins>"])` |
|                          | `schwacheEntität[[schwacheEntität]]---AttributID(["<ins>Attributname</ins>"])` | Stellt eine schwache Entität und ein Primärschlüssel-Attribut dar. |  `Provinz[[Provinz]]---P1(["<ins>Name</ins>"])` |
| mehrwertiges Attribut | `Entität---(((Attributname)))` | Verknüpfung zu einem mehrwertigen Attribut. | `Angestellter---A1(((Zertifikate)))` |
|                       | `schwache_Entität[[schwache_Entität]]---(((Attributname)))` |  | `Angestellter---A1(((Zertifikate)))` |
| zusammengesetztes Attribut | `Entität---AttributID([Attributname])` | Verknüpfung zu einem zusammengesetzten Attribut. | `Angestellte---A3([Anschrift])` |
|                            | `AttributID([Attributname])---AttributID([Attributname])` | | `A3([Anschrift])---A4([Stadt])` |
|                            |                                                           |       | `A3([Anschrift])---A4([Straße])` |
| Relationship | `Entität--(x,y)---Relationship{Relationship}` | Relationship und Entität mit einer Kardinalität(Min-Max-Notation). | `Land--(1,*)---liegt{liegt}` |
|              | `Relationship{Relationship}--(x,y)---Entität` |                                                                    | `ist_HS{ist_HS}--(1,1)---Land` |
|              | `schwache_Entität[[schwache_Entität]]--(x,y)---Relationship{Relationship}` |Relationship und schwache Entität mit einer Kardinalität(Min-Max-Notation). | `Provinz[[Provinz]]--(1,1)---liegt{liegt}` |
|              | `Relationship{Relationship}--(x,y)---schwache_Entität[[schwache_Entität]]` |                                       | `ist_HS{ist_HS}--(0,1)---Stadt[[Stadt]]` |

### ERM Modellierungsregeln 
## Entitäten: 
* Die Form ist immer ein Rechteck.
* Zwischen zwei Entitäten muss immer ein Relationship liege, das heißt diese sind nie direkt miteinander verbunden.
* Eine Entität kann durch Attribute (normales Attribut, zusammengesetztes Attribut oder mehrwertiges Attribut) detaillierter beschrieben werden.
* Eine Entität hat immer genau ein Primärschlüssel-Attribut.

## Relationships:
* Ein Relationship liegt immer zwischen zwei Entitäten.
* Ein Relationship ist nie mit anderen Relationships verbunden.
* Ein Relationship kann durch Attribute (kein Primärschlüssel-Attribut) genauer beschrieben werden.
* Ein Relationship kann eine rekurisve Beziehung haben, das heißt in diesem Fall ist es nur mit einer Entität verbunden und besitzt zwei Kanten zu dieser.

## Attribute:
* Attribute beschreiben Entitäten oder Relationships genauer.
* Nur ein zusammengesetztes Attribut kann mit anderen Attributen (normales Attribut, mehrwertiges Attribut oder Primärschlüssel-Attribut) verbunden sein.

## Kardinalitäten
- Kardinalitäten können nur auf Kanten zwischen Entität und Relationships sein.
- Nach Min-Max-Notation wird die minimal und maximal zulässige Anzahl von Verbindungen zwischen einer Entität und einem Relationship beschrieben.
    - <b>Min</b>: Die minimale Anzahl von Verbindungen, die eine Entität zu einem Relationship haben muss.
    - <b>Max</b>: Die maximale Anzahl von Verbindungen, die eine Entität zu einem Relationship haben muss.
    - <b>Zulässige Werte sind hier</b>:
        - <code>0</code> = keine Verbindung erforderlich
        - <code>1</code> = genau eine Verbindung
        - <code>*</code> = eine beliebige Anzahl von Verbindungen ist möglich











