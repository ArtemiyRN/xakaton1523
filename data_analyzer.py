import json
import log


average_intensivity = 1400
average_time = 3000


def analyze_data(json_file):
    hour_count = 1
    work_list = dict()
    with open(json_file, "r") as file:
        f = json.read(file)
        for hour in f:
            work_list[hour] = [dict()]
            hour_count += 1
            for app in hour.keys():
                work_list[hour][app] = dict()
                work_list[hour][app]["intensivity"] = hour[app][2] + f"average: {average_intensivity}"
                work_list[hour][app]["time"] = hour[app][0] + f"average: {average_time}"
    return work_list


def analyze_log():
    d = str(log.getDate())
    d = d.split('-')
    d = d[2] + '-' + d[1] + '-' + d[0]
    Filename = d.replace('-', '')
    path = "H:\Documents\d"[:-1]
    myfile = log.read(path+Filename, "r").split("\n")
    used_apps = set()
    apps_opened = 0
    for line in myfile:
        com = line.split()
        if com == []:
            break
        if com[0] == "+":
            used_apps.add(com[1])
            apps_opened += 1
    return {"used_apps": used_apps, "apps_opened": apps_opened}


print(analyze_log())