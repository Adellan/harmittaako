import subprocess
import platform
import os


def detectos():
    running = platform.system()
    if running == "Linux":
        return "linux"
    if running == "Windows":
        return "windows"


def sort():
    with open("data.dat", "r") as temp:
        templist = temp.read().splitlines()
    templist.sort()
    return templist


def showgraph():
    sadface = ':( '
    color = 'red'
    run = detectos()
    if run == "linux":
        subprocess.call(["termgraph", "data.dat", "--color", color, "--custom-tick", sadface, "--width", "30", "--title", "Mood entry history"])
    else:
        subprocess.run(["termgraph", "data.dat", "--color", color, "--custom-tick", sadface, "--width", "30", "--title", "Mood entry history"])


def showlatest():
    templist = sort()
    templist.reverse()
    minilist = open("tempdata.dat", "w")
    sadface = ':( '
    color = 'yellow'
    for i in range(5, -1, -1):
        minilist.write(templist[i]+"\n")
    minilist.close()
    run = detectos()
    if run == "linux":
        subprocess.call(["termgraph", "tempdata.dat", "--color", color, "--custom-tick", sadface, "--width", "20", "--title", "Latest moods"])
    else:
        subprocess.run(["termgraph", "tempdata.dat", "--color", color, "--custom-tick", sadface, "--width", "20", "--title", "Latest moods"])
