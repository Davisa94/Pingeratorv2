################################################################
# A module for interacting with an existing MySQL Database
# Author: Austin Benitez
################################################################

import pymysql
from datetime import datetime


class DBInteract:
    def __init__(self, dbObject=""):
        self.DBO = dbObject
        print("RAW DATABASE OBJECT: ", self.DBO)


    def getAllSpeeds(self):
        sql = ("SELECT * FROM speeds")
        self.DBO.cursor.execute(sql)
        return dbObject

    def getSomeSpeeds(self, start, end):
        sql = ("SELECT * FROM speeds WHERE (course_code = %s and course_prefix = %s)")
        self.DBO.cursor.execute(sql, (course_code, course_prefix))
        return dbObject
    def stripGarbage(self, response):
        stripped = response.strip("(),")
    def getIPID(self, ip):
        sql = ("SELECT id FROM iplookup WHERE ipv4 = '{}'".format(ip))
        self.DBO.execute(sql)
        return self.DBO

    def insertSpeed(self, st_obj):
        # get current time
        up_speed = st_obj.upload()
        down_speed = st_obj.download()
        # ping = st_obj.ping()
        curr_date_time = datetime.now()
        sql = "INSERT INTO speed VALUES ('{}',{},{});".format(curr_date_time, up_speed, down_speed)
        self.DBO.execute(sql)

    def insertPing(self, ping_response, host):
        # get current time
        succeeded = response.success
        curr_date_time = datetime.now()
        print("CURRENTDATETIME: ", datetime.now())
        currTime = datetime.now().time()
        dict = {
            "Day": [currDate],
            'TimeStamp': [currTime],
            'Host': [host],
            "responseTIme": [response],
            "Succeeded": [succeeded]
        }
        sql = "INSERT INTO pings VALUES ('{}', )"
        writableResponse = pd.DataFrame.from_dict(dict)
        return writableResponse