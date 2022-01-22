import os
from time import sleep, time
import log
import threading


def main():
    global Filename
    global List
    global BlackList
    global path
    global common_apps

    common_apps = ["EXCEL.EXE"]

    path = "H:\Documents\d"[:-1] # В переменной хранится путь, по которому будут сохраняться логи
    BlackList = log.read('blacklLst.conf').split(
        '\n')  # Считывается файл, со списком процессов ,которые мониторить не нужно из файла "blackList.conf"
    d = str(log.getDate())  # Получаем дату
    t = str(log.getTime())  # Получаем время
    d = d.split('-')  # Преобразуем вид даты (не обязательно, просто мне так уобнее)
    d = d[2] + '-' + d[1] + '-' + d[0]
    Filename = d.replace('-', '') + t.replace(':', '') + '.log'  # Формируем имя лог-файла
    List = list()
    _PID = log.CommandExecutionP('tasklist /FO CSV').split(
        '\n')  # первый раз получаем список запущенных процессов, но не сохраняем в файл
    PidSave(_PID, d, t, 'n')
    processor = threading.Thread(target=process)
    processor.start()


def process():
    while (True):
        print(List)
        sleep(
            1)  # Цикл выполняется через каждую секунду (время можно сократить, однако тогда возрастет нагрузка на систему)
        potok = threading.Thread(
            target=PidRead)  # Функция, считывающая список запущенных процессов, будет работать асинхронно
        potok.start()


def PidRead():
    # Функция получает список запущенных процессов и отправляет их в функции-проверки
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
                if line[0] in log.read('killProcessed.conf').split('\n'): # Если же имя процесса есть в списке завершаемых (в файле "killProcessed.conf")
                    log.CommandExecution('taskkill /PID ' + line[1]) # то завершаем этот процесс
    return List


def PidDel(_PID, d, t, wr='y'):
    # Функция проверяет каких процессов больше нет в получееном списке, если находит, то удаляет их из нашего локального списка и записыв
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
    return List


main()