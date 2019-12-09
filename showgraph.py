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
    command = ["termgraph", "data.dat", "--color", color, "--custom-tick", sadface, "--width", "30", "--title", "Mood entry history"]
    if run == "linux":
        subprocess.call(command)
    else:
    #assumes Windows
        subprocess.run(command)


def showlatest():
    templist = sort()

    #newest entries to top
    templist.reverse()
    minilist = open("tempdata.dat", "w")
    sadface = ':( '
    color = 'yellow'

    #reversing list and reading from end index to beginning so the graph has latest entry on the bottom
    for i in range(5, -1, -1):
        minilist.write(templist[i]+"\n")
    minilist.close()
    run = detectos()
    command = ["termgraph", "tempdata.dat", "--color", color, "--custom-tick", sadface, "--width", "20", "--title", "Latest moods"]
    if run == "linux":
        subprocess.call(command)
    #assumes Windows
    else:
        subprocess.run(command)
