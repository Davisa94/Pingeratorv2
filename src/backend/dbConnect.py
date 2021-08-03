################################################################
# A module for connecting to a mySQL database that already
# exists
# Author: Austin Benitez
################################################################

import pymysql
import json
import os

_CREDS_FILE = "dbcredentials.json"

class MyDb:

    def __init__(self):
        self.schema="pingerator"
        self.host="localhost"
        self.user=""
        self.password=""
        self.get_credentials()

    def get_credentials(self):
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        path_to_creds = os.path.join(curr_dir, _CREDS_FILE)
        with open(path_to_creds, 'r') as cred_file:
            creds = cred_file.read()
            # load str as json
            creds = json.loads(creds)
            self.user = creds["user"]
            self.password = creds["password"]

    def dbDebugDisplay(self, dbObject, statement):
        cursor = self.dbInteract(statement, dbObject)
        print(self.dbData2Array(cursor))

        
    def dbInteract(self, statment:str, dbConnection)->"Returns the cursor":
        #create cursor
        cursor = dbConnection.cursor()
        
        #execute the query
        cursor.execute(statment)
        return cursor

    def dbData2Array(self, cursor):
        tableData = cursor.fetchall()
        return tableData

    def connect(self) ->"dont forget to close the connection":
        mysql_connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.schema)
        cursorObj = mysql_connection.cursor()
        return cursorObj
    

# mydb = MyDb()
# connection = mydb.dbConnect()
# connection.fetchall()