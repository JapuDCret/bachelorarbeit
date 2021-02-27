# Anleitung zum Übersetzen der Arbeit

## Voraussetzungen

 - MiKTeX
	https://miktex.org/
 - TexMaker
	https://www.xm1math.net/texmaker/
	
## Initiale Kommandos und Anpassungen

### Submodules

 1. Untermodule laden
 	`git submodule update --init --recursive`

### Texmaker

 1. PDF Shellescape muss aktiviert werden, dafür das "PdfLaTeX" Kommando austauschen zum
	`pdflatex -synctex=1 -shell-escape --extra-mem-bot=10000000 -interaction=nonstopmode %.tex`

 2. Das Kommando "makeindex" muss auf folgenden Wert gesetzt werden
	`makeindex %.nlo -s nomencl.ist -o %.nls`

### Erstmaliges Übersetzen

Damit alle notwendigen Dateien\* generiert werden, muss das Dokument mehrfach komplett übersetzt werden, da die Bibliotheken gegenseitige Abhängigkeiten aufweisen. Wie man richtig übersetzt, findet sich im nächsten Abschnitt.

\* wie `main.aux`, `tikz-figures/` usw.

## Übersetzen

In Texmaker kann nun mit der Taste **F1** der Text übersetzt werden.
Damit das Literaturverzeichnis auch aktualisiert wird, muss es durch Tastendruck **F11** übersetzt werden.
Damit das Abkürzungsverzeichnis auch aktualisiert wird, muss es durch Tastendruck **F12** übersetzt werden.
