from auxHandler import getProcessesListWithHeaders


def parseProcessList(headers, processListBody):
    colsCount = len(headers) - 1

    def rowStringToCols(rowStr):
        return rowStr.split(None, colsCount)

    def colsToNamedCols(row):
        namedCol = {}
        for idx, col in enumerate(row):
            colName = headers[idx]
            namedCol[colName] = col

        return namedCol

    def convertRowColsTypeToTargetType(row):
        row['%CPU'] = float(row['%CPU'])
        row['%MEM'] = float(row['%MEM'])

    processesTable = list(map(rowStringToCols, processListBody))

    processesTableWithNamedCells = list(map(colsToNamedCols, processesTable))
    for row in processesTableWithNamedCells:
        convertRowColsTypeToTargetType(row)

    return processesTableWithNamedCells


def parseAux():
    processesListHeaders, processListBody = getProcessesListWithHeaders()

    return parseProcessList(processesListHeaders, processListBody)
