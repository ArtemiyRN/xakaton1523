from pynput import keyboard
from pynput import mouse
import threading


apps = dict()
in_process = []


def on_press(key):
    action(1)


def listen_kb():
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()


def on_click(x, y, button, pressed):
    action(1)


def listen_ms():
    with mouse.Listener(
            on_click=on_click) as listener:
        listener.join()


def start(app):
    if app not in apps:
        apps[app] = [0, 0, 0]
    if app not in in_process:
        in_process.append(app)


def stop(app):
    if app in in_process:
        in_process.remove(app)


def action(value):
    for i in in_process:
        apps[i][1] += value / len(in_process)
        apps[i][2] = apps[i][1] / apps[i][0]


kb = threading.Thread(target = listen_ms)
ms = threading.Thread(target=listen_ms)

kb.start()
ms.start()


