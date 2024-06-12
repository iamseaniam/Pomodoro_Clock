#!/usr/bin/env python3
import pygame
import time
import datetime
from win10toast import ToastNotifier
import subprocess

pygame.mixer.init()


def Pomodoro_Clock(work_minutes, break_minutes):
    """Sets a timer that notifies you"""

    # Setting math to know how long minutes are.
    work_seconds = work_minutes * 60
    break_seconds = break_minutes * 60

    # Counts down work minutes till its zero.
    while work_seconds > 0:
        timer = datetime.timedelta(seconds=work_seconds)
        print(timer, end="\r")
        time.sleep(1)
        work_seconds -= 1
    print("Work time is up!")

    # Plays a bloop sound when work_seconds is over.
    pygame.mixer.music.load("Bloop.mp3") # Can change sound to whatever .mp3 file you have
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    # Sends a pop up notication to computer.
    n = ToastNotifier()
    n.show_toast("Pomodoro Timer", "Your work time has gone off!", duration=15, icon_path="MacAttack.ico") # Can change the .ico file if you have a differnt one

    # Calls subprocess to send a messege through slack.
    subprocess.run(["python", "slack2.py"])

    # Counts down beak minutes till its zero.
    while break_seconds > 0:
        timer = datetime.timedelta(seconds=break_seconds)
        print(timer, end="\r")
        time.sleep(1)
        break_seconds -= 1
    print("Break time is up!")

    # plays sound after break is time is up
    pygame.mixer.music.load("Bloop.mp3") # Can change sound to whatever .mp3 file you have
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

    # sends a pop up notifacation to computer
    n = ToastNotifier()
    n.show_toast("Pomodoro Timer", "Your break time has gone off!", duration=10, icon_path="MacAttack.ico")  # Can change the .ico file if you have a differnt one

    # Calls subprocess to send message through slack
    subprocess.run(["python", "slack.py"])

# asking for how many minutes you want for work time and break time.
work_minutes = int(input("Enter the work time in minutes: "))
break_minutes = int(input("Enter the break time in minutes: "))

Pomodoro_Clock(work_minutes, break_minutes)
