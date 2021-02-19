import sys
from math import floor

import numpy as np
import pandas as pd
import xlrd

def main():
    wb = xlrd.open_workbook(r'Tools-und-Werkzeuge.xlsx', encoding_override='utf8')
    df = pd.read_excel (wb)

    groupedTechnologies = parse_rows(df)

    sb = []

    print_technologies(sb, groupedTechnologies)

    latexPage = '\n'.join(sb)

    latexPageUtf8 = latexPage.encode('utf8')

    sys.stdout.buffer.write(latexPageUtf8)

def parse_rows(df):
    groupedTechnologies = {}

    gruppe = None
    ignore = False
    for index, row in df.head(n=999).iterrows():
        cur_gruppe = row['Gruppe']
        cur_ignore = row['Ignore']
        technologie = row['Technologie']

        if pd.isnull(cur_gruppe) and pd.isnull(technologie):
            previousWasEmpty = True
        elif pd.isnull(technologie):
            gruppe = cur_gruppe
            
            ignore = not pd.isnull(cur_ignore)
        else:
            if technologie == "TABLE_END":
                break

            if ignore:
                continue

            previousWasEmpty = False

            technologie = sanitize(row['Technologie'])
            kostenfrei = sanitize(row['Kostenfrei'])
            support = sanitize(row['Support für Webanw.'])
            onPremise = sanitize(row['On Premise'])
            saas = sanitize(row['SaaS (z. B. Cloud)'])
            standardisierung = sanitize(row['Standardisierung'])
            multifunktional = sanitize(row['Multifunktional'])
            zielgruppe = sanitize(row['Zielgruppe'])

            newTech = RatedTechnology(technologie, kostenfrei, support, onPremise, saas, standardisierung, multifunktional, zielgruppe)

            if groupedTechnologies.get(gruppe) == None:
                groupedTechnologies[gruppe] = []
            
            groupedTechnologies[gruppe].append(newTech)

    return groupedTechnologies

PAGE_BREAK_AFTER = 7
def print_technologies(sb, groupedTechnologies):
    technologieCount = 0
    tableNum = 1
    
    print_header(sb, tableNum)

    totalGroupCount = len(groupedTechnologies)
    groupCount = 0

    for group in groupedTechnologies:
        sb.append("\\hline")
        sb.append("\\hline")
        sb.append("\\multicolumn{7}{|p{15.75cm}|}{%s} \\\\" % (group))

        technologies = groupedTechnologies[group]

        groupCount += 1
        
        for technology in technologies:
            print_technology(sb, technology)
            technologieCount += 1
        
        if technologieCount >= PAGE_BREAK_AFTER and groupCount < totalGroupCount:
            print_footer(sb, tableNum)
            ## sb.append("")
            ## sb.append("\\newpage")
            sb.append("")
                    
            tableNum += 1
                    
            print_header(sb, tableNum)
            
            technologieCount = 0

    print_footer(sb, tableNum)

def print_header(sb, tableNum):
    sb.append("\hvFloat[rotAngle=90,nonFloat=true,capWidth=w]%")
    sb.append("{table}%")
    sb.append("{")
    sb.append("\\begin{tabular}{|p{2.25cm}|p{2.0cm}|p{2.0cm}|p{2.0cm}|p{1.5cm}|p{2.0cm}|p{1.5cm}|p{2.5cm}|}")
    sb.append("\\hline")
    sb.append("%s & %s & %s & %s & %s & %s & %s & %s \\\\" %
     ("Technologie", "Kostenfrei", "Support f. Webanw.", "On Premise", "SaaS", "Standard.", "Multif.", "Zielgruppe"))

def print_footer(sb, tableNum):
    sb.append("\\hline")
    sb.append("\\end{tabular}")
    sb.append("}")
    sb.append("{Bewertung der untersuchten Technologien, Teil %d}" % (tableNum))
    sb.append("{tab:technologie-bewertung-teil%d}" % (tableNum))

def print_technology(sb, t):
    sb.append("\\hline")
    sb.append("%s & %s & %s & %s & %s & %s & %s & %s \\\\" %
        (t.technologie, t.kostenfrei, t.support, t.onPremise, t.saas, t.standardisierung, t.multifunktional, t.zielgruppe))

def sanitize(val):
    val = nanToEmptyString(val)
    
    val = val.replace("&", "\\&")
    
    return val

def nanToEmptyString(val):
    # see https://stackoverflow.com/a/944712/3858121
    if val != val:
        return ""
    else:
        return val

def print_empty_line(sb):
    sb.append("\\hline")


class RatedTechnology:
    def __init__(self, technologie, kostenfrei, support, onPremise, saas, standardisierung, multifunktional, zielgruppe):
        self.technologie = technologie
        self.kostenfrei = kostenfrei
        self.support = support
        self.onPremise = onPremise
        self.saas = saas
        self.standardisierung = standardisierung
        self.multifunktional = multifunktional
        self.zielgruppe = zielgruppe

    def __cmp__(self, other):
        return cmp(self.technologie, other.technologie)

    def __lt__(self, other):
        return self.technologie < other.technologie


if __name__ == "__main__":
    # execute only if run as a script
    main()
