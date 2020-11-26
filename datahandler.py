from db_handler import db_handler

class datahandler():

    def __init__(self, db):
        assert isinstance(db, db_handler)
        self.db = db

    def _execute(self, cmd):
        return self.db.execute(cmd)

    def _buildRequest(self, request):
        ret = ""
        for i in range(len(request) -1):
            ret = ret + request[i] + ", "
        ret = ret + request[-1] + ""
        return ret

    def get(self, request, table):
        #SELECT request FROM table
        cmd = f"SELECT {self._buildRequest(request)} FROM {table}"
        return self._execute(cmd)

    def get_ignore(self, request, table, filter, value):
        #SELECT request FROM table WHERE filter != value
        cmd = f"SELECT {self._buildRequest(request)} FROM {table} WHERE {filter} != '{value}''"
        return self._execute(cmd)

    def get_filter(self, request, table, filter, value):
        #SELECT request FROM table WHERE filter = value
        cmd = f"SELECT {self._buildRequest(request)} FROM {table} WHERE {filter} == '{value}''"
        return self._execute(cmd)
