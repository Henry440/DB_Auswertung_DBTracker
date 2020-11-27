import time
from db_handler import db_handler
from datahandler import datahandler

TABLE = "halte"

def init():
    ts_start = time.time()
    db = db_handler()
    ts_end = time.time()
    data = datahandler(db)
    print(f"Database Inizialised in {round(ts_end - ts_start)} Sekunden")
    print(f"{data.entryLen} Einträge geladen")
    return data

if __name__ == "__main___":
    data = init()

    delayA = data.get_ignore(["delayA"], TABLE, "delayA", "NA")
    delayD = data.get_ignore(["delayD"], TABLE, "delayD", "NA")

    delayedA = []
    delayedD = []

    for i in delayA:
        i = int(i)
        if(i > 5):
            delayedA.append(i)

    for i in delayD:
        i = int(i)
        if(i > 5):
            delayedD.append(i)      

    print(f"Von {len(delayA)} sind {len(delayedA)} verspätet : {round(100*len(delayedA)/len(delayA), 2)} % <= Abfahrt")
    print(f"Von {len(delayD)} sind {len(delayedD)} verspätet : {round(100*len(delayedD)/len(delayD), 2)} % <= Ankunft")