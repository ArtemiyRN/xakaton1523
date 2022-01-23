import tkinter as tk
import matplotlib
import threading


stats = dict()
window = None
font = ("Arial Bold", 10)


def open_window(title = ""):
    global window
    global left_frame
    global right_frame
    global description

    window = tk.Tk()
    window.title = title

    stat_button = tk.Button(window, text="Click to show stats", font = font)
    stat_button.grid(row= 0, column= 0)

    left_frame = tk.Frame(window)
    right_frame = tk.Frame(window)
    left_frame.grid(column=0, row=1)
    right_frame.grid(column=1, row=1)

    description = tk.Label(right_frame, text="abcabc", font = font)
    description.grid(column=0,row=0)

    for hour in stats:
        text = stats[hour]
        add_hour(hour, text)

    window.geometry = "600x600"
    w = threading.Thread(target=window.mainloop())
    w.start()


def show_hour_stats(text= ""):
    description.text = text


def add_hour(hour, text):
    if window == None:
        return
    stats[hour] = text
    new_hour = tk.Button(left_frame, text=str(hour), command=lambda: show_hour_stats(stats[hour]), font= font)
    new_hour.grid(column = 0, row = hour)

