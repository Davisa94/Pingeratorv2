import time
import os
import pandas as pd
from pythonping import ping
from datetime import datetime

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
        pingC = PT.PingCloudFlare() 
        pingO = PT.PingOpenDNS()
        analyzer = DataAnalyzer()
        st = SpeedyTest.SpeedyTester()

        while True:
            time.sleep(8)
            pingG.run(db_interactor)
            pingC.run(db_interactor)
            pingO.run(db_interactor)
            st.run(db_interactor)
            # commit the changes to the database
            db_connection.commit()

        input("Press Enter To Continue")
        exit()
    # Close the connection
    except Exception as e:
        print("An unexpected error occurred: }".formt(e))
    finally:
        db_cursor.close()

    


if __name__ == '__main__':
    main()
