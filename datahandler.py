from db_handler import db_handler

class datahandler():

    def __init__(self, db):
        assert isinstance(db, db_handler)
        self.db = db
        self.entryLen = self.db.entryLen


    #Internal Operrations
    def _execute(self, cmd, lenArgs):
        ret = self.db.execute(cmd)
        return self._toArray(ret, lenArgs)

    def _buildRequest(self, request):
        ret = ""
        for i in range(len(request) -1):
            ret = ret + request[i] + ", "
        ret = ret + request[-1] + ""
        return ret

    def _toArray(self, data, argLen):
        ret = []
        for i in data:
            if(argLen == 1):
                ret.append(i[0])
            else:
                ret.append(i)
        return ret

    #External Operations
    def filter_array(self, data, position, value):
        ret = []
        for i in data:
            if(i[position] == value):
                ret.append(i)
        return ret


    #Database Operations
    def get(self, request, table):
        #SELECT request FROM table
        cmd = f"SELECT {self._buildRequest(request)} FROM {table}"
        if(len(request) == 1 and request[0] == "*"):
            return self._execute(cmd, 2)
        else:
            return self._execute(cmd, len(request))

    def get_ignore(self, request, table, filter, value):
        #SELECT request FROM table WHERE filter != value
        cmd = f"SELECT {self._buildRequest(request)} FROM {table} WHERE {filter} != '{value}'"
        if(len(request) == 1 and request[0] == "*"):
            return self._execute(cmd, 2)
        else:
            return self._execute(cmd, len(request))

    def get_filter(self, request, table, filter, value):
        #SELECT request FROM table WHERE filter = value
        cmd = f"SELECT {self._buildRequest(request)} FROM {table} WHERE {filter} == '{value}'"
        if(len(request) == 1 and request[0] == "*"):
            return self._execute(cmd, 2)
        else:
            return self._execute(cmd, len(request))
