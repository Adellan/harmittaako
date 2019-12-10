import subprocess
import platform
import os


def detectos():
    return platform.system().lower()


def showgraph():
    sadface = ':( '
    color = 'red'
    run = detectos()
    command = ["termgraph", "data.dat", "--color", color, "--custom-tick", sadface, "--width", "30", "--title", "Mood entry history"]
    if run == "linux":
        subprocess.call(command)
    else:
    #assumes Windows
        subprocess.run(command)


def showlatest():
    with open("data.dat", "r") as temp:
        templist = temp.read().splitlines()
    templist.sort()
    minilist = open("tempdata.dat", "w")
    sadface = ':( '
    color = 'yellow'

    #latest 5 dates, newest on the bottom
    for i in range(len(templist) -5, len(templist), 1):
        minilist.write(templist[i]+"\n")
    minilist.close()
    run = detectos()
    command = ["termgraph", "tempdata.dat", "--color", color, "--custom-tick", sadface, "--width", "20", "--title", "Latest moods"]
    if run == "linux":
        subprocess.call(command) 
    else:
    #assumes Windows
        subprocess.run(command)
