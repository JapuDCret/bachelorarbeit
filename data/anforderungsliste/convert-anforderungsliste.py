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
    id = row['Id']
    kano = row['Kano-Modell']
    funkt = row['Funktionsart']
    quelle = row['Quelle']
    titel = row['Titel']
    beschr = row['Beschreibung']
    
    sb.append("")
    sb.append("\\begin{anf}{anf:%d}{%d}{%s}{%s}{%s}{%s}" % (id, id, titel, kano, funkt, quelle))
    sb.append("\\multicolumn{5}{|p{14.05cm}|}{%s} \\\\" % (beschr))
    sb.append("\\hline")
    sb.append("\\end{anf}")

def printGruppe(sb, group):
    sb.append("")
    sb.append("\\subsubsection{" + group + "}")
    sb.append("")


if __name__ == "__main__":
    # execute only if run as a script
    main()
