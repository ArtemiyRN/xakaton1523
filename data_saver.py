import json
import os


def new_data():
    with open("my.json", "w"):
        pass


def save_data(apps):
    if not "my.json" in os.listdir():
        os.mkdir("my.json")
    with open("my.json", "a") as file:
        json.dump(apps, file, indent=4)


