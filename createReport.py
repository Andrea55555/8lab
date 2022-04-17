from parseAux import parseAux
import math 

# Отчёт о состоянии системы:
# Пользователи системы: 'root', 'user1', ...
# Процессов запущено: 833
# Пользовательских процессов:
# root: 533
# user1: 231
# ...
# Всего памяти используется: 45.7%
# Всего CPU используется: 33.2%
# Больше всего памяти использует: (%имя процесса, первые 20 символов если оно длиннее)
# Больше всего CPU использует: (%имя процесса, первые 20 символов если оно длиннее)

# print(firstProc['USER'])
# print(firstProc[procNameKey])
# print(firstProc['%CPU'])
# print(firstProc['%MEM'])
# print(firstProc['VSZ'])
# print(firstProc['RSS'])
# print(firstProc['TTY'])
# print(firstProc['STAT'])
# print(firstProc['START'])
# print(firstProc['TIME'])
# print(firstProc['COMMAND'])

userKey = 'USER'
procNameKey = 'COMMAND'
memResourceKey = '%MEM'
cpuResourceKey = '%CPU'

def countStats(processes):
    def updateMostRamIntensiveProc(proc, counter):
        resourceUsage = proc[memResourceKey]
        utilisationKey = memResourceKey
        if resourceUsage > counter[utilisationKey]:
            counter[procNameKey] = proc[procNameKey]
            counter[utilisationKey] = resourceUsage

    def updateMostCpuIntensiveProc(proc, counter):
        resourceUsage = proc[cpuResourceKey]
        utilisationKey = cpuResourceKey

        if resourceUsage > counter[utilisationKey]:
            counter[procNameKey] = proc[procNameKey]
            counter[utilisationKey] = resourceUsage

    def updateTotalUtilisationCounter(proc, counter):
        counter[memResourceKey] = counter[memResourceKey] + proc[memResourceKey]
        counter[cpuResourceKey] = counter[cpuResourceKey] + proc[cpuResourceKey]

    def updateUserProcCounter(proc, counter):
        userName = proc[userKey]
        if userName in counter:
            counter[userName] += 1
        else:
            counter[userName] = 1

    def createMostRamIntensiveProcCounter(process):
        counter = {}
        counter[procNameKey] = process[procNameKey],
        counter[memResourceKey] = process[memResourceKey]

        return counter

    def createMostCpuIntensiveProcCounter(process):
        counter = {}
        counter[procNameKey] = process[procNameKey],
        counter[cpuResourceKey] = process[cpuResourceKey]

        return counter

    def createTotalUtilisationCounter():
        counter = {}
        counter[memResourceKey] = 0.0
        counter[cpuResourceKey] = 0.0

        return counter

    usersProcessCount = {}
    totalUtilisationCounter = createTotalUtilisationCounter()
    mostRamIntensiveProcCounter = createMostRamIntensiveProcCounter(processes[0])
    mostCpuIntensiveProcCounter = createMostCpuIntensiveProcCounter(processes[0])
    
    for process in processes:
        updateMostRamIntensiveProc(process, mostRamIntensiveProcCounter)
        updateMostCpuIntensiveProc(process, mostCpuIntensiveProcCounter)
        updateTotalUtilisationCounter(process, totalUtilisationCounter)
        updateUserProcCounter(process, usersProcessCount)

 

    counters = {
        'mostRamIntensiveProc': mostRamIntensiveProcCounter,
        'mostCpuIntensiveProc': mostCpuIntensiveProcCounter,
        'processTotal': len(processes),
        'usersProcess': usersProcessCount,
        'totalUtilisation': totalUtilisationCounter
    }

    return counters

def formatReport(counters):
    mostRamIntensiveProc = counters['mostRamIntensiveProc']
    mostCpuIntensiveProc = counters['mostCpuIntensiveProc']
    processTotalCount = counters['processTotal']
    usersProcess = counters['usersProcess']
    totalUtilisation = counters['totalUtilisation']
    # print(usersProcess)

    reports = []

    reportHeader = 'Отчёт о состоянии системы:\n'
    
    reports = []

    def createUsersReport():
        label = 'Пользователи системы'
        users = usersProcess.keys()
        report = f'{label}:\n{", ".join(users)}'
        return report
        
    def createProcessTotalCountReport():
        label = 'Процессов запущено'
        report = f'{label}: {processTotalCount}'
        return report

    def createUserProceesReport():
        def converUserProcDictToStr(userProc):
            userName, procsCount = userProc
            return f'{userName}: {procsCount}'        

        usersProcessCountReportList = list(map(converUserProcDictToStr, usersProcess.items())) 
        usersProcessCountReportStr = "\n".join(usersProcessCountReportList)
        
        label = f'Пользовательских процессов'
        report = f'{label}:\n{usersProcessCountReportStr}'
        return report

    def createTotalResourceUtilisation():
        # Всего памяти используется: 45.7%
        # Всего CPU используется: 33.2%

        cpuVal = math.floor(totalUtilisation[cpuResourceKey])
        ramVal = math.floor(totalUtilisation[memResourceKey])
        labelRam = 'Всего памяти используется'
        labelCpu = 'Всего CPU используется'
        
        ramReport = f'{labelRam}: {ramVal}%'
        cpuReport = f'{labelCpu}: {cpuVal}%'
        return '\n'.join([ramReport, cpuReport])

    def createMostRamIntensiveProcReport():
        counter = mostRamIntensiveProc
        res = memResourceKey
        
        procName = counter[procNameKey][:20]
        resVal = counter[res]

        label = 'Больше всего памяти использует'
        report = f'{label}: {procName}, {res}: {resVal}'
        return report

    def createMostCpuIntensiveProcReport():
        counter = mostCpuIntensiveProc
        res = cpuResourceKey
        
        procName = counter[procNameKey][:20]
        resVal = counter[res]

        label = 'Больше всего CPU использует'
        report = f'{label}: {procName}, {res}: {resVal}'
        return report
  

    reports.append(reportHeader)
    reports.append(createUsersReport())
    reports.append(createProcessTotalCountReport())
    reports.append(createUserProceesReport())

    reports.append(createTotalResourceUtilisation())
    reports.append(createMostRamIntensiveProcReport())
    reports.append(createMostCpuIntensiveProcReport())
    
    return '\n'.join(reports)

    
    # Отчёт о состоянии системы:
# Пользователи системы: 'root', 'user1', ...
# Процессов запущено: 833
# Пользовательских процессов:
# root: 533
# user1: 231
# ...
# Всего памяти используется: 45.7%
# Всего CPU используется: 33.2%
# Больше всего памяти использует: (%имя процесса, первые 20 символов если оно длиннее)
# Больше всего CPU использует: (%имя процесса, первые 20 символов если оно длиннее)


def createReport():
    return formatReport(countStats(parseAux()))
    
print(createReport())
