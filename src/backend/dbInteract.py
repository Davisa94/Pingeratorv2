################################################################
# A module for interacting with an existing MySQL Database
# Author: Austin Benitez
################################################################

import pymysql


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

    def insertSpeed(self, st_obj):
        # get current time
        up_speed = st_obj.upload()
        down_speed = st_obj.download()
        # ping = st_obj.ping()
        currDateTime = datetime.now()
        sql = "INSERT INTO speed VALUES ('{}',{},{});".format(currDateTime, up_speed, down_speed)
        self.DBO.execute(sql)