echo "Generiere Übersicht.."
python convert-TuW-to-overview.py > tools-und-werkzeuge_uebersicht.tex

echo "Generiere Kategorisierung.."
python convert-TuW-to-grouping.py > tools-und-werkzeuge_kategorisierung.tex

echo "Generiere Bewertungstabellen.."
python convert-TuW-to-rated.py