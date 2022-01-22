import activity
from data_saver import save_data
import Input
import time


current_time = int(time.ctime().split()[3].split(":")[0])


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




main()
