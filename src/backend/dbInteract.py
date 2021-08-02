################################################################
# A module for interacting with an existing MySQL Database
# Author: Austin Benitez
################################################################

from name import Name
from location import Location
from sectionDataClass import CourseSectionData
import pymysql


class DBInteract:
    def __init__(self, dbObject=""):
        self.DBO = dbObject


    def getAllSpeeds(self):
        sql = ("SELECT * FROM speeds")
        self.DBO.cursor.execute(sql)
        return dbObject

    def getSomeSpeeds(self, start, end):
        sql = ("SELECT * FROM speeds WHERE (course_code = %s and course_prefix = %s)")
        self.DBO.cursor.execute(sql, (course_code, course_prefix))
        return dbObject
