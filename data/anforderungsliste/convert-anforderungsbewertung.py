import sys

import numpy as np
import pandas as pd
import xlrd

def main():
    wb = xlrd.open_workbook(r'Anforderungsliste.xlsx', encoding_override='utf8')
    df = pd.read_excel(wb,converters={'Id':str,'Erf{\\"u}llungsgrad':str})

    groupedAnforderungen = parse_rows(df)
    
    sb = []

    print_anforderungen(sb, groupedAnforderungen)

    latexPage = '\n'.join(sb)

    latexPageUtf8 = latexPage.encode('utf8')

    sys.stdout.buffer.write(latexPageUtf8)

def parse_rows(df):
    groupedAnforderungen = {}

    gruppe = None
    for index, row in df.head(n=999).iterrows():
        cur_gruppe = row['Gruppe']
        id = row['Id']

        if pd.isnull(cur_gruppe) and pd.isnull(id):
            break
        elif pd.isnull(id):
            gruppe = cur_gruppe
        else:
            id = sanitize(row['Id'])
            kano = sanitize(row['Kano-Modell'])
            funktionsart = sanitize(row['Funktionsart'])
            quelle = sanitize(row['Quelle'])
            titel = sanitize(row['Titel'])
            beschreibung = sanitize(row['Beschreibung'])
            erfuellungsGrad = sanitize(row['Erf{\\"u}llungsgrad'])

            newAnf = Anforderung(id, kano, funktionsart, quelle, titel, beschreibung, erfuellungsGrad)

            if groupedAnforderungen.get(gruppe) == None:
                groupedAnforderungen[gruppe] = []
            
            groupedAnforderungen[gruppe].append(newAnf)

    return groupedAnforderungen

def print_anforderungen(sb, groupedAnforderungen):
    print_header(sb)
    
    for group in groupedAnforderungen:
        sb.append("\\hline")
        sb.append("\\multicolumn{6}{|l|}{%s} \\\\" % (group))

        anforderungen = groupedAnforderungen[group]
        
        for anforderung in anforderungen:
            print_anforderung(sb, anforderung)

    print_footer(sb)

    return sb

def print_header(sb):
    sb.append("\\begingroup")
    sb.append("\\centering")
    sb.append("\\setlength{\LTleft}{-20cm plus -1fill}")
    sb.append("\\setlength{\LTright}{\LTleft}")
    sb.append("\\begin{longtable}{|p{0.85cm}|p{6.2cm}|p{1.55cm}|p{1.75cm}|p{1.1cm}|p{1.8cm}|}")
    sb.append("\\hline")
    sb.append("%s & %s & %s & %s & %s & %s \\\\" %
     ("Id", "Titel", "Kano-Modell", "Funktions\\-art", "Quelle", "Erfüllungs\\-grad"))
    sb.append("\\endhead")

def print_footer(sb):
    sb.append("\\hline")
    sb.append("\\caption{Tabellarische Bewertung der Anforderungen}")
    sb.append("\\label{tab:anforderungsbewertung}")
    sb.append("\\end{longtable}")
    sb.append("\\endgroup")
    sb.append("")

def print_anforderung(sb, a):
    sb.append("\\hline")
    sb.append("%s & %s & %s & %s & %s & %s \\\\" %
        (a.id, a.titel, a.kano, a.funktionsart, a.quelle, a.erfuellungsGrad))

def sanitize(cellValue):
    cellValue = nanToEmptyString(cellValue)
    
    text = cellValue
    
    text = text.replace(" \"", " \\enquote{")
    text = text.replace("\"", "}")
    
    text = text.replace("%", "\\%")
    
    return text

def nanToEmptyString(val):
    # see https://stackoverflow.com/a/944712/3858121
    if val != val:
        return ""
    else:
        return val

class Anforderung:
    def __init__(self, id, kano, funktionsart, quelle, titel, beschreibung, erfuellungsGrad):
        self.id = id
        self.kano = kano
        self.funktionsart = funktionsart
        self.quelle = quelle
        self.titel = titel
        self.beschreibung = beschreibung
        self.erfuellungsGrad = erfuellungsGrad

if __name__ == "__main__":
    # execute only if run as a script
    main()
