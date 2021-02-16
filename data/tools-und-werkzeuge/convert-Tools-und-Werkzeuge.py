import sys
from math import floor

import numpy as np
import pandas as pd
import xlrd

LINE_BREAK_AFTER = 12

def main():
    wb = xlrd.open_workbook(r'Tools-und-Werkzeuge.xlsx', encoding_override='utf8')
    df = pd.read_excel (wb)

    sb = []
    
    previousWasEmpty = True
    technologieCount = 0
    tableNum = 1
    
    printHeader(sb, tableNum)
    
    for index, row in df.head(n=999).iterrows():
        technologie = row['Technologie']

        if pd.isnull(technologie):
            if previousWasEmpty:
                break
            previousWasEmpty = True
        else:
            if technologie == "TABLE_BREAK":
                printFooter(sb, tableNum)
                sb.append("")
                sb.append("\\newpage")
                sb.append("")
                
                tableNum += 1
                
                printHeader(sb, tableNum)
            elif technologie == "TABLE_END":
                printFooter(sb, tableNum)
                break
            else:
                technologieCount += 1
                printRow(sb, row, previousWasEmpty)
                previousWasEmpty = False

    latexPage = '\n'.join(sb)

    latexPageUtf8 = latexPage.encode('utf8')

    sys.stdout.buffer.write(latexPageUtf8)

def printHeader(sb, tableNum):
    sb.append("\hvFloat[rotAngle=90,nonFloat=true,capWidth=w]%")
    sb.append("{table}%")
    sb.append("{")
    sb.append("\\begin{tabular}{|p{2.25cm}|p{1.1cm}|p{1.4cm}|p{1.5cm}|p{1.1cm}|p{1.25cm}|p{1.25cm}|p{1.5cm}|p{1.25cm}|p{1.25cm}|p{1.35cm}|}")
    sb.append("\\hline")
    sb.append("%s & %s & %s & %s & %s & %s & %s & %s & %s & %s \\\\" %
     ("Technologie", "APM", "RUM", "Error-Mo\\-ni\\-tor\\-ing", "Log-Mgmt", "Tracing", "Session-Replay", "Kosten\\-frei", "Web\\-support", "Deploy\\-ment"))


def printFooter(sb, tableNum):
    sb.append("\\hline")
    sb.append("\\end{tabular}")
    sb.append("}")
    sb.append("{Übersicht der untersuchten Technologien, Teil %d}" % (tableNum))
    sb.append("{tab:technologie-uebersicht-teil%d}" % (tableNum))

def printRow(sb, row, previousWasEmpty):
    if previousWasEmpty:
        printEmptyRow(sb)
    
    technologie = sanitize(row['Technologie'])
    apm = sanitize(row['APM'])
    rum = sanitize(row['RUM'])
    errorMonitoring = sanitize(row['Error-Monitoring'])
    logManagement = sanitize(row['Log-Management'])
    tracing = sanitize(row['Tracing'])
    sessionReplay = sanitize(row['Session-Replay'])
    kostenfrei = sanitize(row['Kostenfrei'])
    websupport = sanitize(row['Websupport'])
    deployment = sanitize(row['Deployment'])
    
    sb.append("\\hline")
    sb.append("%s & %s & %s & %s & %s & %s & %s & %s & %s & %s \\\\" %
        (technologie, apm, rum, errorMonitoring, logManagement, tracing, sessionReplay, kostenfrei, websupport, deployment))

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

def printEmptyRow(sb):
    sb.append("\\hline")


if __name__ == "__main__":
    # execute only if run as a script
    main()
