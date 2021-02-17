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
    for index, row in df.head(n=999).iterrows():
        cur_gruppe = row['Gruppe']
        technologie = row['Technologie']

        if pd.isnull(cur_gruppe) and pd.isnull(technologie):
            previousWasEmpty = True
        elif pd.isnull(technologie):
            gruppe = cur_gruppe
        else:
            if technologie == "TABLE_END":
                break

            previousWasEmpty = False
            
            technologie = sanitize(row['Technologie'])
            apm = sanitize(row['APM'])
            rum = sanitize(row['RUM'])
            errorMonitoring = sanitize(row['Error-Monitoring'])
            logManagement = sanitize(row['Log-Management'])
            tracing = sanitize(row['Tracing'])
            sessionReplay = sanitize(row['Session-Replay'])

            newTech = Technologie(technologie, apm, rum, errorMonitoring, logManagement, tracing, sessionReplay)

            if groupedTechnologies.get(gruppe) == None:
                groupedTechnologies[gruppe] = []
            
            groupedTechnologies[gruppe].append(newTech)

    return groupedTechnologies

PAGE_BREAK_AFTER = 12
def print_technologies(sb, groupedTechnologies):
    technologieCount = 0
    tableNum = 1
    
    print_header(sb, tableNum)

    for group in groupedTechnologies:
        sb.append("\\hline")
        sb.append("\\multicolumn{7}{|p{15.75cm}|}{%s} \\\\" % (group))

        technologies = groupedTechnologies[group]
        
        for technology in technologies:
            print_technology(sb, technology)
            technologieCount += 1
        
        if technologieCount >= PAGE_BREAK_AFTER:
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
    sb.append("\\begin{tabular}{|p{2.25cm}|p{1.5cm}|p{2.0cm}|p{3.0cm}|p{3.0cm}|p{1.5cm}|p{2.5cm}|}")
    sb.append("\\hline")
    sb.append("%s & %s & %s & %s & %s & %s & %s \\\\" %
     ("Technologie", "APM", "RUM", "Error-Mo\\-ni\\-tor\\-ing", "Log-Management", "Tracing", "Session-Replay"))

def print_footer(sb, tableNum):
    sb.append("\\hline")
    sb.append("\\end{tabular}")
    sb.append("}")
    sb.append("{Übersicht der untersuchten Technologien, Teil %d}" % (tableNum))
    sb.append("{tab:technologie-kategorisierung-teil%d}" % (tableNum))

def print_technology(sb, t):
    sb.append("\\hline")
    sb.append("%s & %s & %s & %s & %s & %s & %s \\\\" %
        (t.technologie, t.apm, t.rum, t.errorMonitoring, t.logManagement, t.tracing, t.sessionReplay))

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


class Technologie:
    def __init__(self, technologie, apm, rum, errorMonitoring, logManagement, tracing, sessionReplay):
        self.technologie = technologie
        self.apm = apm
        self.rum = rum
        self.errorMonitoring = errorMonitoring
        self.logManagement = logManagement
        self.tracing = tracing
        self.sessionReplay = sessionReplay

    def __cmp__(self, other):
        return cmp(self.technologie, other.technologie)

    def __lt__(self, other):
        return self.technologie < other.technologie


if __name__ == "__main__":
    # execute only if run as a script
    main()
