import activity
from data_saver import save_data, new_data, read_data
import Input
import time
import threading
import ui
import db
import graph_builder


def main():
    new_data()
    user = db.new_user("Artemiy")
    day = db.add_day(user)
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
            db.add_hour(day, sum([Input.apps[app][2] for app in Input.apps]))
        for app in Input.apps:
            Input.apps[app][0] += 1


def add_app(app):
    activity.common_apps.append(app)


def del_app(app):
    activity.common_apps.remove(app)


def open_ui(title):
    ui.open_window(title)


def build_graph():
    hours = read_data
    graph_builder.get_stats(hours)
    graph_builder.show_graph()


def check_inputs():
    while True:
        i = input("Введите одну из доступных команд").strip()
        com = i.split()
        if len(com) not in (2,1):
            print("Директива отсутствует в списке команд")
            continue
        if not com[0] in commands.keys():
            print("Директива отсутствует в списке команд")
            continue

        if len(com) == 2:
            commands[com[0]](com[1])
        else:
            commands[com[0]]()


def get_command_list():
    print(list(commands.keys()))


current_time = int(time.ctime().split()[3].split(":")[0])
commands = {"add_app": lambda app: add_app(app), "del_app": lambda app: del_app(app), "open_ui": lambda title: open_ui(title),
            "build_graph": lambda: build_graph(), "get_command_list": lambda: get_command_list()}


input_checker = threading.Thread(target=check_inputs)
input_checker.start()

if __name__ == "__main__":
    main()
input_checker.join()