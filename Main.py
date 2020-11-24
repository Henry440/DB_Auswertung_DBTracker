
from db_handler import db_handler

db = db_handler()

def getDelay(datas):
    min = 0
    max = 0
    maxID = 0
    minID = 0
    fahrten = 0
    delayed = 0
    reg = 5
    for i in datas:
        data = int(i[0])
        fahrten += 1
        if(data > reg):
            delayed += 1
        
        if(data > max):
            max = data
            maxID = i[1]
        
        if(data < min):
            min = data
            minID = i[1]

    print(f"Maximal : {max} Minimal : {min} Prozent : {round(100*delayed/fahrten, 2)} unpünktlich")
    print(f"ID Minimal : {minID} ID Maximal : {maxID} | eintragNr der Züge")
    print(f"Fahrten : {fahrten} davon Verspätet : {delayed} mit mehr als {reg} Minuten")
    '''
    for x in db.execute(f"SELECT * FROM halte WHERE eintragNr = {minID}"):
        print(f"MIN {x}")
    for x in db.execute(f"SELECT * FROM halte WHERE eintragNr = {maxID}"):
        print(f"MAX {x}")
    '''

def gw():
    not_relevant = ["3", "3a", "4", "5", "6", "7", "8", "8a"]
    r1 = ["1", "2"]
    r2 = ["9", "10"]
    for x in db.execute("SELECT platformD, scheduledPlatformD, station FROM halte WHERE platformD != 'NA' AND platformD != scheduledPlatformD AND station = 'Erfurt Hbf'"):
        if (not(x[1] in not_relevant or x[0] in not_relevant)):
            if((x[0] in r1 and x[1] in r2) or (x[0] in r2 and x[1] in r1)):
                print(x)

print("Ankunft")
getDelay(db.execute("SELECT delayA, eintragNr FROM halte WHERE delayA != 'NA'"))
print("Abfahrt")
getDelay(db.execute("SELECT delayD, eintragNr FROM halte WHERE delayD != 'NA'"))
gw()
