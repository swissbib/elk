## Allgemeine Informationen
Die Navigation zwischen den Dashboards ist möglich mit den Naviationslinks oben auf jedem Dashboard. Jedes Dashboard stellt Visualisierungen zum Thema im Titel des Dashboards zusammen. Eine Zusammenfassung der Dashboards kann unten eingesehen werden.

### Zeitspanne

Alle Dashboards haben eine Voreinstellung der Zeitspanne von 30 Tagen. Das heisst die dargestellten Zahlen und Diagramme repäsentieren nur Daten welche in den letzten 30 Tagen gesammelt wurden.

Wenn man weiter zurück gehen möchte, kann man dies machen indem man die Zeitspanne ändert. Dazu klicked man rechts oben auf den Timepicker (angeschrieben mit `Last 30 Days` wenn nichts geändert wurde). Nach dem Klick öffnet sich ein Menu in dem man eine Zeitspanne auswählen kann. 

### Wie kann ich etwas in einem Dashboard ändern?
Solange eine Änderung in einem Dashboard nicht gespeichert wird, gehen alle Änderungen verloren.

Damit man eine Änderung an einem Dashboard vorgenommen werden kann, muss auf `Edit` in der Menuleiste rechts oben rechts gedrückt werden.

### Was ist der Unterschied zwischen IP Adresse und Session ID?
In manchen Visualisierungen sind die Daten nach IP Adresse oder Session ID zusammengefasst. Die IP Adresse bezieht sich auf den PC/Netzwerk von dem auf Swissbib zugegriffen wird, während die Session ID jedesmal wenn man neu auf die Webseite kommt neu generiert werden kann (manchmal kann auch eine Session weitergeführt werden, solange man den Browser nicht schliesst). Das heisst, wenn Daten basierend auf den Session IDs sollten immer höher sein als bei Zahlen basierend auf IP Adressen.

Erkennen kann man das ganze am Titel der Visualisierung. Wenn dort IP Adresse oder Session ID drin steht, werden die Daten danach Zusammengefasst.

Achtung: Nicht alle Datensätze haben eine Session ID oder eine IP Adresse, d.h. diese Angaben sind mit Vorsicht zu geniessen. 

### Was wird auf den einzelnen Dashboards dargestellt?
**Allgemein (Letzter Monat):** Ein kompletter Überblick über die Nutzungszahlen der Webseiten. Jede Zahl bezieht sich auf alle Aufrufe.

**Allgemein (Letztes Jahr):** Beinhaltet allgemeine Fragen zur Nutzung basierend auf Anzahl Klicks Total. Bezieht sich auf das letzte Jahr. Ältere Daten werden ignoriert. Bezieht sich eigentlich immer auf alle Aufrufe und unterteilt nicht nach einzelnen Nutzern.

**Statisiken Besucher:** Ein Besucher ist eine Person mit der selben IP-Adresse oder Session-ID. Diese sind aber nicht zu 100% verlässlich und geben auch unterschiedliche Resultate.

**Facetten Auswertung:** Zeigt die Nutzung aller Facetten. Beinhaltet auch facetten suchen aus erweiterten suchen. Zält eine Suche nach zwei Bibliotheken oder nach zwei Sprachen als eine einzige Suche an. Unterscheidet nicht zwischen Facetten von Normalen und Erweiterten Suchen. Die Kreise zeigen jeweils die 10 am meisten genutzten Facetten-Werte jeder Facette.

**Erweiterte Suchen:** Zeigt wie die erweiterte suche genutzt wird: Suchfeld Typen, Suchfeldverknüpfungen, Suchgruppenverküpfungen, Publikationsdaten, Treffer pro Seite und Total. Gesamtbetrachtungen der Suchen sind nur schwer möglich. Es ist nicht möglich allgemein zu sehen welches Suchfeld mit welchen Suchfeldverknüpfungen genutzt wird, ausser wenn man sich eine individuelle Suchanfrage anschaut.

**Geografische Auswertung:** Land, Stadt & Koordinaten. Nicht nach Nutzer aufgeteilt.

**Records:** Welcher Verbund Angesteuert wird. Welche die meistgesuchten Bücher waren. Nutzung der Reiter, Speicher und Export Funktionen. Hat links mit welchen man direkt zu einem Buch kommt, welches man sucht.

**MyResearch:** Nutzungszahlen zu den MyResearch Seiten.

**Lionels Dashboard:** Fragestellungen Lionel (Login, Nationallizenzen Flyer).

**Technische Daten:** Geräte, OS, Browser, Verweis von. Hier sind die Daten nach Session (Nutzer) unterteilt. Diese Daten sind aber mit vorsicht zu geniessen, da sie auf der Auswertung des Useragents basieren. Dieser kann manipuliert werden und ist nicht immer sehr eindeutig. z.B. können Tablets kaum erkannt werden da diese sich nicht als solche zu erkennen geben.

**Verschiedenes:** Vor allem wie gesucht wird: Suchoperatoren, Sortierungen der Suchresultate, Anzahl Treffer pro Seite und Filter Publikationsdatum von->bis.

### Was sind die Filter?

Grundsätzlich sind alle Anfragen von Bots und über Touchpoint gefiltert. 

Neue Filter können erstellt werden, in dem auf die Daten geklick wird in den Visualisierungen. Diese erscheinen dann oben unter dem Suchschlitz. Dort können sie deaktiviert, gepinnt, umgekehrt/negiert, gelöscht und geändert werden.

Ein deaktivierter Filter hat keinen Effekt mehr auf die Daten, dies sieht man daran, dass er ausgegraut ist. 

Wenn ein Filter gepinnt wird ist bleibt er auch vorhanden, wenn man zu einem anderen Dashboard oder zum Discover wechselt. Neue Filter sind standard-mässig gepinnt.

Das ändern eines Filters muss in der [DSL-Query Syntax](https://www.elastic.co/guide/en/elasticsearch/reference/5.3/query-dsl.html) geschehen. Und man kann einem Filter ein Label geben.

### Wie Suche ich in der Suchleiste oben am Dashboard?

Die Suche im Suchschlitz basiert auf der Lucene Syntax. [Genaue Dokumentation kann hier gefunden werden](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html).
