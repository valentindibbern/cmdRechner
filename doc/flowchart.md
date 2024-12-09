## Programmflow

````mermaid
graph TD
    A[Programmstart] --> B[Warte auf Benutzereingabe]
    B --> C[Tokenize Funktion]
    C -->|Fehler/keine Tokens| D[Fehlermeldung ausgeben]
    D --> B
    C -->|Erfolgreich| E[Prüfe, ob Eingabe 'exit' ist]
    E -->|Ja| F[Programm beenden]
    F --> Z[Ende]
    E -->|Nein| G[AST erstellen]
    G -->|Fehler im Aufbau| D
    G -->|Erfolgreich| H[(zukünftige Implementierung)]
    H --> I[Warte auf neue Eingabe]
    I --> B
````

### Tokanize Funktion
````mermaid
graph TD
    A[Tokenize Funktion aufrufen] --> B[Eingabestring erhalten]
    B --> C[RegEx-Muster anwenden]
    C -->|Kein Match| F[Fehler: Keine gültigen Tokens]
    F --> Z[Rückgabe: Leere Liste]
    C -->|Tokens gefunden| D[Jedes Token verarbeiten]
    D --> E[Typ bestimmen]
    E -->|Ganzzahl| G[Token in 'int' umwandeln]
    E -->|Gleitkommazahl| H[Token in 'float' umwandeln]
    E -->|Text/Operator| I[Als 'str' speichern]
    G --> J[Token speichern]
    H --> J
    I --> J
    J -->|Weitere Tokens vorhanden| D
    J -->|Keine weiteren Tokens| K[Rückgabe: Tokenliste]

````