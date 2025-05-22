# Gruppenaufgabe: Quiz-Antwort prüfen mit Python
Willkommen zur Gruppenarbeit im Rahmen des Git-Workshops. 
In dieser Aufgabe schreibt ihr eine kleine Funktion, die prüft, ob eine gegebene Antwort richtig ist.


## Ziel
Schreibt eine Funktion `is_correct(...)`, die erkennt, ob eine gewählte Antwort korrekt ist. 

---

## Startdatei: `check_answer.py`
In der Startdatei ist ein Beispiel enthalten. Ihr erweitert es Schritt für Schritt. 

---

## So gehts
1. Legt ein Dictionary namens `question` mit diesen Feldern an:
   - `"Text"`: Die Frage als String
   - `"options"`: Eine Liste mit **vier** Antwortmöglichkeiten
   - `"correct"`: Der Index (0-3) der richtigen Antwort
2. Schreibt die Funktion:

  python def is_correct(question, answer_index):
  return question ["correct"] == answer_index


3. Testet eure Funktion:
- Legt z.B. fest: `answer =1`
Gebt mit `print(...)` aus, ob die Antwort richtig ist (`True` oder `False`)
