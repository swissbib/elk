## Allgemeine Informationen
Die Navigation zwischen den Dashboards ist möglich mit den Naviationslinks oben auf jedem Dashboard. Jedes Dashboard stellt Visualisierungen zum Thema im Titel des Dashboards zusammen. Eine Zusammenfassung der Dashboards kann unten eingesehen werden.

### Zeitspanne

Alle Dashboards haben eine Voreinstellung der Zeitspanne von 30 Tagen. Das heisst die dargestellten Zahlen und Diagramme repäsentieren nur Daten welche in den letzten 30 Tagen gesammelt wurden.

Wenn man weiter zurück gehen möchte, kann man dies machen indem man die Zeitspanne ändert. Dazu klicked man rechts oben auf den Timepicker (angeschrieben mit `Last 30 Days` wenn nichts geändert wurde). Nach dem Klick öffnet sich ein Menu in dem man eine Zeitspanne auswählen kann. 

### Wie kann ich etwas in einem Dashboard ändern?
Ein Dashboard kann bearbeitet werden, nachdem man auf den `Edit`-Button rechts oben in der Menuleiste drückt. Nun können Änderungen vorgenommen werden. **WICHTIG:** Änderungen werden nur gespeichert, wenn man explizit auf `Save` drückt und dann nocheinmal auf `Save` drückt. Einmal gespeichert, kann das alte Dashboard nicht einfach so wiederhergestellt werden. 

### Was ist der Unterschied zwischen IP Adresse und Session ID?
Wir sammlen die IP Adresse und Session IDs auf verschiedene Arten. 

Die IP Adresse ist fast immer dabei, ausser bei allen jusbib Datensätzen (ein Konfigurationsproblem, welches in Zukunft gelöst werden soll). Die IP Adresse designiert die Organisation/den PC von wo aus ein Aufruf gemacht wird. So haben alle Aufrufe, die an einem Bibliotheksrechner in Bern oder Basel gemacht haben je die gleichen IP Adressen.

Die Session ID wird über ein Cookie auf dem PC des Nutzers gespeichert und von dort übertragen. Ein Cookie bleibt bestehen bis es vom Nutzer gelöscht wird oder der Browser geschlossen wird.
Dies führt dazu, dass eine Reihe von Aufrufen keine Session ID haben. 
1. Immer der erste Aufruf eines Users hat keine Session ID.
2. Alle Aufrufe von Usern ohne Cookies haben keine Session ID.
3. Wenn ein Nutzer nach dem ersten Aufruf wieder geht oder nur Dinge macht, die keine Session ID erzeugen.

Etwa 20% aller Aufrufe haben keine Session ID. Davon sind etwa 8% erste Aufrufe einer Session.

Das heisst alle Visualisierungen bei welchen nach IP Adresse oder Session ID gezählt wird, muss dies bedacht werden, wenn man die Zahlen sich ansieht.

### Was sind die Filter?
Die eingestellten Filter werden oben links unter dem Suchschlitz dargestellt. Die Filter sind entweder rot oder grau und können leicht Transparent sein.

Filter funktionieren wie Facetten von Swissbib. Ein Filter kann auf ein einzeles Datenfeld angewendet werden. Ein grauer Filter entfernt alles, wo der Filter nicht zutrifft. Ein roter Filter entfernt alles, wo der Filter zutrifft. Transparente Filter sind nicht aktiv.

Voreingestellt sind insgesammt sechs Filter: 
- `Bots` (akitv) Entfernt alle Aufrufe die von Bots gemacht werden.
- `Zend Attribute Resolver` (akitv) Entfernt alle Aufrufe die vom Zend Framework gemacht werden.
- `Zurückgewiesene Aufrufe` (akitv) Entfernt alle Aufrufe die vom Server abgelehnt werden (z.B. wenn 404 zurück kommt).
- `Swissbib` (nicht akitv) Zeige nur Aufrufe die auf swissbib grün gemacht wurden.
- `Basel/Bern` (nicht akitv) Zeige nur Aufrufe die auf swissbib orange gemacht wurden.
- `Jusbib` (nicht akitv) Zeige nur Aufrufe die auf jusbib gemacht wurden.

**Bitte keine Filter löschen!**

Wenn man mit der Maus über einen Filter geht, erscheinen fünf Optionen:
- `Aktivieren` -> Ob der Filter aktiv ist oder nicht.
- `Pinnen` -> Der Filter wird angemacht und kommt mit, wenn man das Tab wechselt (z.B. vom `Dashbaord` in den `Discovery`-Bereich)
- `Lupensymbol` -> Führt dazu, dass der Filter negiert wird.
- `Abfall` -> Filter löschen.
- `Bleistift` -> Filter bearbeiten.

Ein Filter kann mit dem `Add a filter +` gemacht werden. Man muss hier 2 - 3 Felder ausfüllen. Zum einen muss man ein Datenfeld auswählen auf welches der Filter angewendet werden soll. Als zweites der Typ des Filters. Und drittes, je nach Typ, den Wert des Filters eingeben.

Eine detailierte Anleitung findet man [hier](https://www.elastic.co/guide/en/kibana/5.6/field-filter.html).

### Was wird auf den einzelnen Dashboards dargestellt?
**Allgemein (Letzter Monat):** Ein allgemeiner Überblick über die Nutzungszahlen. 

**Statisiken Besucher:** Ein Besucher ist eine Person mit der selben IP-Adresse oder Session-ID. 

**Facetten Auswertung:** Zeigt die Nutzung aller Facetten. Beinhaltet auch facetten suchen aus erweiterten suchen. Zält eine Suche nach zwei Bibliotheken oder nach zwei Sprachen als eine einzige Suche an. Unterscheidet nicht zwischen Facetten von Normalen und Erweiterten Suchen. Die Kreise zeigen jeweils die 10 am meisten genutzten Facetten-Werte jeder Facette.

**Erweiterte Suchen:** Zeigt wie die erweiterte suche genutzt wird: Suchfeld Typen, Suchfeldverknüpfungen, Suchgruppenverküpfungen, Publikationsdaten, Treffer pro Seite und Total. Gesamtbetrachtungen der Suchen sind nur schwer möglich. Es ist nicht möglich allgemein zu sehen welches Suchfeld mit welchen Suchfeldverknüpfungen genutzt wird, ausser wenn man sich eine individuelle Suchanfrage anschaut.

**Geografische Auswertung:** Land, Stadt & Koordinaten. Nicht nach Nutzer aufgeteilt.

**Records:** Welcher Verbund Angesteuert wird. Welche die meistgesuchten Bücher waren. Nutzung der Reiter, Speicher und Export Funktionen. Hat links mit welchen man direkt zu einem Buch kommt, welches man sucht.

**MyResearch:** Nutzungszahlen zu den MyResearch Seiten.

**Lionels Dashboard:** Fragestellungen Lionel (Login, Nationallizenzen Flyer).

**Technische Daten:** Geräte, OS, Browser, Verweis von. Hier sind die Daten nach Session (Nutzer) unterteilt. Diese Daten sind aber mit vorsicht zu geniessen, da sie auf der Auswertung des Useragents basieren. Dieser kann manipuliert werden und ist nicht immer sehr eindeutig. z.B. können Tablets kaum erkannt werden da diese sich nicht als solche zu erkennen geben.

**Verschiedenes:** Vor allem wie gesucht wird: Suchoperatoren, Sortierungen der Suchresultate, Anzahl Treffer pro Seite und Filter Publikationsdatum von->bis.

**Linked Data:** Visualisierungen zu den Linked Data Seiten (Knowledge Cards).

### Wie Suche ich in der Suchleiste oben am Dashboard?

Die Suche im Suchschlitz basiert auf der Lucene Syntax. [Genaue Dokumentation kann hier gefunden werden](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html). 
