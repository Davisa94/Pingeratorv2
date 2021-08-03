import time
import os
import pandas as pd
from pythonping import ping
from datetime import datetime
import speedtest
from dbConnect import MyDb
from dbInteract import DBInteract
import re

from modules import GlobalValues
from modules import FileManager as FM
from modules import PythonPing as PP

# Global Values
runningDir = os.path.dirname(__file__)

class SpeedyTester:
    def __init__(self, desktop):
        self.file = desktop + _SPEEDSOUTFILE
        generateFile(self.file, _SPEEDDICT)


    def upload_test(self):
        pass
    def run(self, db_interactor):
        print("The full path to my log files is at: {} ".format(self.file))
        st = speedtest.Speedtest()
        # print("Success" if res.success else " Failed")
        print(st.download())
        # sql = generateSpeedSQL(st)
        # storeSpeedToDB(sql, db_interactor)
        db_interactor.insertSpeed(st)

        # printDataframeToFile(wr, self.file)

    

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

        desktop_dir = generateDesktopPath()
        home_dir = generateHomeFolder(desktop_dir)
        #check if files exist, if they do move along, if not, generate them with appropriate headers

        print("The detected desktop directory is {} and will be used for storing the data folder".format(home_dir))
        pingG = PingGoogle(home_dir)
        pingC = PingCloudFlare(home_dir) 
        pingO = PingOpenDNS(home_dir)
        analyzer = DataAnalyzer()
        st = SpeedyTester(home_dir)

        while True:
            time.sleep(8)
            pingG.run(db_interactor)
            pingC.run()
            pingO.run(db_interactor)
            st.run(db_interactor)
            # commit the changes to the database
            db_connection.commit()

        input("Press Enter To Continue")
        exit()
    # Close the connection
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))
    finally:
        db_cursor.close()

    


if __name__ == '__main__':
    main()
