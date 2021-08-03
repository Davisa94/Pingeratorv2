################################################################
# A module for interacting with an existing MySQL Database
# Author: Austin Benitez
################################################################

import pymysql
from datetime import datetime
import re


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

    #Given an Ip address returns the id of that adress from the iplookup table 
    def getIPID(self, ip):
        sql = ("SELECT id FROM iplookup WHERE ipv4 = '{}'".format(ip))
        self.DBO.execute(sql)
        response_id = db_interactor.getIPID(_CLOUDFLAREHOST)
        ip_id = self.DBO.fetchall()
        return ip_id[0]

    def insertSpeed(self, st_obj):
        # get current time
        up_speed = st_obj.upload()
        down_speed = st_obj.download()
        # ping = st_obj.ping()
        curr_date_time = datetime.now()
        sql = "INSERT INTO speed VALUES ('{}',{},{});".format(curr_date_time, up_speed, down_speed)
        self.DBO.execute(sql)

    def responseToRawPing(response):
        raw_ping = re.findall('\d+(\.\d+)?ms',response)
        print("RAW PING: ", raw_ping)
        return raw_ping

    def insertPing(self, ping_response, host):
        # get current time
        succeeded = response.success
        curr_date_time = datetime.now()
        print("CURRENTDATETIME: ", datetime.now())
        currTime = datetime.now().time()
        self.responseToRawPing(response)
        dict = {
            "Day": [currDate],
            'TimeStamp': [currTime],
            'Host': [host],
            "responseTIme": [response],
            "Succeeded": [succeeded]
        }

        sql = "INSERT INTO ping VALUES ('{}', )"
        writableResponse = pd.DataFrame.from_dict(dict)
        return writableResponse