import subprocess
import platform

def detectsmiley():
    running = platform.system()
    running.lower()
    if running == "linux":
        return '☹'
    else:
        return ':( '


def sort():
    with open("data.dat", "r") as temp:
        templist = temp.read().splitlines()
    templist.sort()
    return templist


def showgraph():
    sadface = detectsmiley()
    color = 'red'
    subprocess.run(["termgraph", "data.dat", "--color", color, "--custom-tick", sadface, "--width", "30", "--title", "Mood entry history"])


def showlatest():
    templist = sort()
    templist.reverse()
    minilist = open("tempdata.dat", "w")
    sadface = detectsmiley()
    color = 'yellow'
    for i in range(5, -1, -1):
        minilist.write(templist[i]+"\n")
    minilist.close()
    subprocess.run(["termgraph", "tempdata.dat", "--color", color, "--custom-tick", sadface, "--width", "20", "--title", "Latest moods"])