# Purpose

The included Python script converts the excel file to a latex file, that will then be imported in the bachelor's thesis.

# Install Requirements

```bash
pip install -r requirements.txt
```

# Generate Overview from Excel File

## Dry Run

```bash
python convert-TuW-to-overview.py
```

## Write to file

```bash
python convert-TuW-to-overview.py > tools-und-werkzeuge_uebersicht.tex
```

# Generate Grouping from Excel File

## Dry Run

```bash
python convert-TuW-to-grouping.py
```

## Write to file

```bash
python convert-TuW-to-grouping.py > tools-und-werkzeuge_kategorisierung.tex
```

# Generate Rated Overview from Excel File

## Dry Run

```bash
python convert-TuW-to-rated.py
```

## Write to file

```bash
python convert-TuW-to-rated.py > tools-und-werkzeuge_bewertung.tex
```
