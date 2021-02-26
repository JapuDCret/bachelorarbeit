import sys

import numpy as np
import pandas as pd
import xlrd

def main():
    wb = xlrd.open_workbook(r'Anforderungsliste.xlsx', encoding_override='utf8')
    df = pd.read_excel (wb)

    sb = []
    
    for index, row in df.head(n=999).iterrows():
        groupTitle = row['Gruppe']

        if pd.isnull(groupTitle):
            printAnforderung(sb, row)
        else:
            printGruppe(sb, groupTitle)

    latexPage = '\n'.join(sb)

    latexPageUtf8 = latexPage.encode('utf8')

    sys.stdout.buffer.write(latexPageUtf8)

def printAnforderung(sb, row):
    id = sanitize(row['Id'])
    kano = sanitize(row['Kano-Modell'])
    funkt = sanitize(row['Funktionsart'])
    quelle = sanitize(row['Quelle'])
    titel = sanitize(row['Titel'])
    beschr = sanitize(row['Beschreibung'])
    
    sb.append("")
    sb.append("\\begin{anf}{anf:%d}{%d}{%s}{%s}{%s}{%s}" % (id, id, titel, kano, funkt, quelle))
    sb.append("\\multicolumn{5}{|p{14.05cm}|}{%s} \\\\" % (beschr))
    sb.append("\\hline")
    sb.append("\\end{anf}")

def printGruppe(sb, group):
    sb.append("")
    sb.append("\\subsubsection{" + group + "}")
    sb.append("")

def sanitize(cellValue):
    if type(cellValue) == int or type(cellValue) == float:
        return cellValue
    
    text = cellValue
    
    text = text.replace(" \"", " \\enquote{")
    text = text.replace("\"", "}")
    
    return text

if __name__ == "__main__":
    # execute only if run as a script
    main()
