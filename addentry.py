def addentry():
    entrydate = input("Give a date (YYYY-MM-DD) ")
    if entrydate and len(entrydate) != 10:
        return print("Invalid date")

    entrymood = input("How's your mood on scale 1-10? ")
    if entrymood and entrymood.isnumeric():
        if int(entrymood) >= 1 and int(entrymood) <= 10:
            moods = open('data.dat', 'a')
            moods.write("\n%s %s" % (entrydate, entrymood))
            moods.close()
            return
        else:
            print("Invalid range")
    else:
        return print("Invalid mood input")