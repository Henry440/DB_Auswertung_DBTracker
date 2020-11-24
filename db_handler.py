from statics import DATABASE, TABLE_NAME

import sqlite3

DUPPLE_IDENTIFIER = "rawId"
EINTRAG_ID = "eintragNr" #Eindeutige ID

class db_handler():

    def __init__(self):
        self.conn = sqlite3.connect(DATABASE)
        self.c = self.conn.cursor()
        self._remove_dupple_entrys()
        self.entryLen = 0
        tem = []
        for e in self.get_all_datas():
            tem.append(e)
        self.entryLen = len(tem)

    def _get_rawId(self):
        return self.c.execute(f"SELECT {EINTRAG_ID}, {DUPPLE_IDENTIFIER} FROM {TABLE_NAME}")

    def _delete_entry(self, eintragNummer):
        self.c.execute(f"DELETE FROM {TABLE_NAME} WHERE eintragNr = {eintragNummer}")
        self.conn.commit()

    def execute(self, execute):
        return self.sql_request(execute)

    def sql_request(self, request):
        return self.c.execute(request)

    def _remove_dupple_entrys(self):
        ids = []
        for id in self._get_rawId():
            ids.append(id)
        
        exist = []
        for pack in ids:
            id = pack[0]
            rawId = pack[1]
            if(rawId in exist):
                entrys = self.sql_request(f"SELECT {EINTRAG_ID} FROM {TABLE_NAME} WHERE {DUPPLE_IDENTIFIER} = '{rawId}'") 
                max = 0
                d1 = []
                d2 = []
                for gg in entrys:
                    d1.append(gg[0])
                    d2.append(gg[0])
                for gg in d1:
                    if(gg > max):
                        max = gg
                for gg in d2:
                    if(gg != max):
                        self._delete_entry(gg)
            else:
                exist.append(rawId)


    def get_all_datas(self):
        ret = self.c.execute(f"SELECT * FROM {TABLE_NAME}")
        return ret