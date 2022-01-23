import activity
from data_saver import save_data
import Input
import time
import threading


def main():
    next_hour = 1
    while True:
        time.sleep(1)
        activity.process()
        cur_hour = int(time.ctime().split()[3].split(":")[0])
        if cur_hour > 17 or cur_hour < 8:
            quit(main)
        if cur_hour >= next_hour + current_time:
            next_hour += 1
            save_data(Input.apps)
            for app in Input.apps:
                Input.apps[app][0] = 0
        for app in Input.apps:
            Input.apps[app][0] += 1


def add_app(app):
    activity.common_apps.append(app)


def del_app(app):
    activity.common_apps.remove(app)


def check_inputs():
    while True:
        i = input("Введите одну из доступных команд")
        com = i.split()
        if not com[0] in commands or len(commands) != 2:
            print("Директива отсутствует в списке команд")
            continue
        commands[com[0]](com[1])



current_time = int(time.ctime().split()[3].split(":")[0])
commands = {"add_app": lambda app: add_app(app), "del_app": lambda app: del_app(app)}

input_checker = threading.Thread(target=check_inputs)
input_checker.start()


main()