echo "Generiere Anforderungsliste.."
python convert-anforderungsliste.py > anforderungsliste.tex

echo "Generiere Anforderungsbewertung.."
python convert-anforderungsbewertung.py > anforderungsbewertung.tex
