from time import sleep, time
import log
import threading
import Input


def main():
    global Filename
    global List
    global BlackList
    global path
    global common_apps

    common_apps = ["EXCEL.EXE"]

    path = "H:\Documents\d"[:-1]
    BlackList = log.read('blacklLst.conf').split(
        '\n')
    d = str(log.getDate())
    t = str(log.getTime())
    d = d.split('-')
    d = d[2] + '-' + d[1] + '-' + d[0]
    Filename = d.replace('-', '')  # Формируем имя лог-файла
    List = list()
    _PID = log.CommandExecutionP('tasklist /FO CSV').split(
        '\n')
    PidSave(_PID, d, t, 'n')


def process():
    sleep(
        1)
    potok = threading.Thread(
        target=PidRead)
    potok.start()


def PidRead():
    _PID = log.CommandExecutionP('tasklist /FO CSV').split('\n')
    d = str(log.getDate())
    t = str(log.getTime())
    PidSave(_PID, d, t)
    PidDel(_PID, d, t)


def PidSave(_PID="", d="", t="", wr='y'):
    for line in _PID:
        line = line.replace('"','').split(',')
        if len(line) > 1:
            if not line[0] + ' ' + line[1] in List and not line[0] in BlackList:
                List.append(line[0] + ' ' + line[1])
                if wr == 'y' and line[3] != '0' and not line[0] in BlackList:
                    log.write('+ \t' + line[0] + '\t' + line[1] + '\t' + line[4][:len(line[4])-2].replace('я',' ') + 'Кб' + '\t' + t + '\t' + d.replace('-', '.') + '\n', path + Filename, 'a') # то ДОзаписываем информацию информацию об этом в лог-файл
                    if line[0] in common_apps:
                        Input.start(line[0])
                if line[0] in log.read('killProcessed.conf').split('\n'):
                    log.CommandExecution('taskkill /PID ' + line[1])
    return List


def PidDel(_PID, d, t, wr='y'):
    newlist = []
    for line in _PID:
        line = line.replace('"', '').split(',')
        if len(line) > 1:
            newlist.append(line[0] + ' ' + line[1])
    for line in List:
        if not line in newlist:
            List.remove(line)
            if wr == 'y':
                log.write('- \t' + line + 'Кб' + '\t' + t + '\t' + d.replace('-', '.') + '\n', path + Filename, 'a')
                if line[0] in common_apps:
                    Input.stop(line[0])
    return List


main()
