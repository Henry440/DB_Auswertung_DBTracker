from db_handler import db_handler

class datahandler():

    def __init__(self, db):
        assert isinstance(db, db_handler)
        self.db = db

    def execute(self, cmd):
        self.db.execute(cmd)

    def get(self, request, table):
        #SELECT request FROM table
        pass

    def get_ignore(self, request, table, filter, value):
        #SELECT request FROM table WHERE filter != value
        pass

    def get_filter(self, request, table, filter, value):
        #SELECT request FROM table WHERE filter = value
        pass
