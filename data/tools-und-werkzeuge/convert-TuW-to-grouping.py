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
            im = sanitize(row['IM'])
            asm = sanitize(row['ASM'])
            rum = sanitize(row['RUM'])
            errorMonitoring = sanitize(row['Error-Monitoring'])
            tracing = sanitize(row['Tracing'])
            logManagement = sanitize(row['Log-Management'])
            sessionReplay = sanitize(row['Session-Replay'])

            newTech = Technology(technologie, im, asm, rum, errorMonitoring, tracing, logManagement, sessionReplay)

            if groupedTechnologies.get(gruppe) == None:
                groupedTechnologies[gruppe] = []
            
            groupedTechnologies[gruppe].append(newTech)

    return groupedTechnologies

PAGE_BREAK_AFTER = 14
def print_technologies(sb, groupedTechnologies):
    technologieCount = 0
    tableNum = 1
    
    print_header(sb, tableNum)

    for group in groupedTechnologies:
        sb.append("\\hline")
        sb.append("\\hline")
        sb.append("\\multicolumn{8}{|l|}{%s} \\\\" % (group))

        technologies = groupedTechnologies[group]
        
        for technology in technologies:
            print_technology(sb, technology)
            technologieCount += 1

    print_footer(sb, tableNum)

def print_header(sb, tableNum):
    sb.append("\\begingroup")
    sb.append("\\centering")
    sb.append("\\setlength{\LTleft}{-20cm plus -1fill}")
    sb.append("\\setlength{\LTright}{\LTleft}")
    sb.append("\\begin{longtable}{|p{4.10cm}|p{0.90cm}|p{0.90cm}|p{1.9cm}|p{1.75cm}|p{1.5cm}|p{1.4cm}|p{1.3cm}|}")
    sb.append("\\hline")
    sb.append("%s & %s & %s & %s & %s & %s & %s & %s \\\\" %
     ("Technologie", "IM", "ASM", "RUM", "Error-Montoring", "Log-Mgmt.", "Tracing", "Session-Replay"))
    sb.append("\\endhead")

def print_footer(sb, tableNum):
    sb.append("\\hline")
    sb.append("\\caption{Kategorisierung der untersuchten Technologien}")
    sb.append("\\label{tab:technologie-kategorisierung}")
    sb.append("\\end{longtable}")
    sb.append("\\endgroup")
    sb.append("")

def print_technology(sb, t):
    sb.append("\\hline")
    sb.append("%s & %s & %s & %s & %s & %s & %s & %s \\\\" %
        (t.technologie, t.im, t.asm, t.rum, t.errorMonitoring, t.logManagement, t.tracing, t.sessionReplay))

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


class Technology:
    def __init__(self, technologie, im, asm, rum, errorMonitoring, tracing, logManagement, sessionReplay):
        self.technologie = technologie
        self.im = im
        self.asm = asm
        self.rum = rum
        self.errorMonitoring = errorMonitoring
        self.tracing = tracing
        self.logManagement = logManagement
        self.sessionReplay = sessionReplay

    def __cmp__(self, other):
        return cmp(self.technologie, other.technologie)

    def __lt__(self, other):
        return self.technologie < other.technologie


if __name__ == "__main__":
    # execute only if run as a script
    main()
