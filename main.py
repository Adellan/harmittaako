from showgraph import showgraph
from addentry import addentry

print("Welcome to mood tracker!")


def start():
    print("")
    print("[s]how graph")
    print("[a]dd entry")
    print("[e]xit")
    print("")
    command = input("What would you like to do? ")
    return command


while True:
    keys = start().lower()
    if keys == "e":
        print("Bye bye!")
        break;
    if keys == "s":
        showgraph()
    if keys == "a":
        addentry()
