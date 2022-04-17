import subprocess

def getProcessesList():
    auxOutput, auxErr = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).communicate()

    if auxErr != None:
        print('internal ps aux err')
        return []

    processesListWithHeaderStr = str(auxOutput, 'utf-8').split('\n')

    return processesListWithHeaderStr

def getProcessesListWithHeaders():
    processesListWithHeader = getProcessesList()
    
    headers = processesListWithHeader[0].split()
    processes = processesListWithHeader[1:]
    # remove last empty string
    processes.pop()

    return headers, processes
