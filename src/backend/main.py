#!/usr/bin/env python3
import time
import os
import pandas as pd
from pythonping import ping
from datetime import datetime
import sys


from dbConnect import MyDb
from dbInteract import DBInteract
import re

from modules import GlobalValues
from modules import FileManager as FM
from modules import PingTest as PT
from modules import SpeedyTest

# Global Values
runningDir = os.path.dirname(__file__)


# TODO: Impliment data analysis 
class DataAnalyzer:
    def __init__(self):
        pass

    def analyze(self):
        place_holder_message = "Analyzing the data. Press any key to exit the application."
        print(place_holder_message)
        sys.stdout.flush()



def main():
    # Connect to the Database
    # create DB object
    db_obj = MyDb()
    # connect and get cursor
    db_connection = db_obj.connect()
    db_cursor = db_connection.cursor()
    db_interactor = DBInteract(db_cursor)
    try:
        pingG = PT.PingGoogle()
        print("init Google")
        pingC = PT.PingCloudFlare()
        print("init cf")
        pingO = PT.PingOpenDNS()
        print("init odns")
        analyzer = DataAnalyzer()
        st = SpeedyTest.SpeedyTester()
        print("init speed")

        while True:
            time.sleep(8)
            print("slept")
            pingG.run(db_interactor)
            print("pinging Google")
            pingC.run(db_interactor)
            print("pinging CF")
            pingO.run(db_interactor)
            print("pinging odns")
            st.run(db_interactor)
            print("testing speed")
            # commit the changes to the database
            db_connection.commit()

        input("Press Enter To Continue")
        exit()
    # Close the connection
    except Exception as e:
        print(e)
        print("An unexpected error occurred: ".format(e))
        sys.stdout.flush()
    finally:
        db_cursor.close()

    


if __name__ == '__main__':
    main()
