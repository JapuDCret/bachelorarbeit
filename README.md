# Bachelorthesis

## Hilfreiches

 1. [:book: Anleitung zum Übersetzen der Arbeit](build.md)
 2. [:open_file_folder: Verzeichnis mit exportieren Versionen](export/)
 3. [:robot: Automatisch erzeugte Versionen](https://github.com/JapuDCret/bachelorarbeit/actions/workflows/build.yml)
 4. [:bookmark_tabs: Literaturrecherche.xlsx](Literatur/Literaturrecherche.xlsx)
 5. **[:computer: Demoanwendung (mit eingebauter Lösung)](https://github.com/JapuDCret/bachelorarbeit-demoanwendung/tree/loesung)**

## Kurzfassung
	
Im Projektalltag führen Probleme in JavaScript-basierten Webanwendungen zu teuren Ausfällen, die durch fehlende Informationen oftmals später behoben werden als vergleichbare Fehler in Backendsystemen. Aus diesem Grund wird in dieser Arbeit das Problem der Nachvollziehbarkeit bei Webanwendungen dieser Art untersucht.
	
Das Ziel der Arbeit ist es, herauszufinden, warum Entwickler und Betreiber von einer Webanwendung weniger relevante Informationen erhalten. Weiterhin ist zu ergründen, wie dieser Informationslücke entgegenwirkt werden kann. Wie sehen hierbei bewährte Ansätze aus und wie ist der Stand der Technik. Letztendlich ist ein Proof-of-Concept zu erstellen, anhand dessen die gefundenen Ansätze anzuwenden und zu veranschaulichen sind.

Um das Ziel der Arbeit zu erreichen, wurde zunächst die Ausgangssituation beschrieben, um festzustellen, welche besonderen Eigenschaften diese Webanwendungen besitzen. Folgend wurde die Nachvollziehbarkeit als solche ergründet und welche Methoden existieren, um eine bessere Nachvollziehbarkeit zu erreichen. Darauf aufbauend beleuchtet die Arbeit zudem den Stand der Technik, auf Basis dessen einige Technologien kriteriengeleitet ausgewählt wurden, um diese beim Proof-of-Concept zu verwenden.

Der Proof-of-Concept wurde auf Basis einer Demoanwendung erstellt, welche eine mit Angular erstellte SPA ist. Diese SPA stellt einen Checkout-Wizard dar, welcher eingebaute Fehlerszenarien enthält. Für den Proof-of-Concept wurde diese SPA in verschiedenen Aspekten erweitert, um bspw. Logs, Metriken, Traces und Fehler zu protokollieren. Diese Daten wurden an Partnersysteme (Splunk, Jaeger, LogRocket) weitergeleitet und somit den Entwicklern sowie Betreibern aufbereitet zur Verfügung gestellt.

Letztendlich wurde die erstellte Lösung durch zuvor definierte Anforderungen und Fehlerszenarien überprüft, dabei wurde festgestellt, dass der geforderte Mehrwert erreicht werden konnte. Weiterhin konnte eine Übertragbarkeit auf andere ähnliche Softwareprojekte aufgezeigt werden, sodass die erstellte Lösung auch hier anwendbar ist.

## Abstract

Failures in web applications that rely on JavaScript often result in costly outages. The time to fix can also be magnified compared to similar issues with backend applications, caused by missing crucial information needed to debug and fix the issue. Therefore, this thesis explores the problem of observability of web applications.

The goal of the work is therefore to bring forth an understanding, why relevant information is missing. Furthermore, it is to be explored, how this information can be obtained and if there are tried and tested methods to achieve this. Based on this gathered understanding, a proof of concept is to be developed, that uses the findings and illustrates their purpose.

To achieve the goal of the work, first and foremost the environment is investigated, e. g. which characteristics of web applications distinguish from backend applications. After that, the term "observability" is defined and examined. The state of the art regarding "observability" is studied, resulting in the knowledge of current methods and technologies. Based on these findings, some technologies are selected for use in the proof of concept.

The proof of concept is developed based on a demo application, that is in its core an Angular SPA. The SPA is a wizard for a webshop checkout, which also contains built-in issues. This demo application was then extended to yield more information, such as logs, metrics, traces and errors. These data was then forwarded to systems, that utilized them to enable developers and operators to "observe" the SPA. These systems were Splunk, Jaeger and LogRocket.

Finally, the created solution was verified based on requirements and its ability to reveal crucial information about the built-in issues. It was found that the solution yielded the required information and met the vast majority of previously defined requirements. Additionally, it was determined that the solution is applicable to similar software projects.