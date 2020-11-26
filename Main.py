import time
from db_handler import db_handler
from datahandler import datahandler

def init():
    ts_start = time.time()
    db = db_handler()
    ts_end = time.time()
    data = datahandler(db)
    print(f"Database Inizialised in {round(ts_end - ts_start)} Sekunden")
    print(f"{data.entryLen} Einträge geladen")
    return db, data

database, data = init()