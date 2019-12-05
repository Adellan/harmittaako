import subprocess

def showgraph():
    sadface = ':( '
    color = 'red'
    subprocess.run(["termgraph", "data.dat", "--color", color, "--custom-tick", sadface, "--width", "20", "--title", "History of sad"])