def write(text="Script name: log.py\nFunction: write()\n", fname="log.log", rej="w", cod="utf8"):
    try:
        f = open(fname, rej, encoding=cod)
        f.write(text)
        f.close()
        return 1
    except Exception as e:
        return str(e)


def read(fname="log.log", rej="r", cod="utf8"):
    try:
        f = open(fname, rej)
        text = f.read()
        f.close()
        return text
    except:
        try:
            f = open(fname, rej, encoding=cod)
            text = f.read()
            f.close()
            return text
        except Exception as e:
            return str(e)


def CommandExecutionP(command=""):
    import os
    result = os.popen(command).read()
    return result


def CommandExecution(command=""):
    import os
    result = os.system(command)
    return result


def getDate():
    import datetime
    MyDate = datetime.date.today()
    return MyDate


def getTime():
    import datetime
    MyTime = datetime.datetime.today().strftime("%H:%M:%S")
    return MyTime