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


# generates an object for storing the results of the pings and
# for use in writing to the csv file when given an response object
def generateOutObject(response, host):
    # get current time
    succeeded = response.success
    currDate = datetime.now().date()
    print("CURRENTDATETIME: ", datetime.now())
    currTime = datetime.now().time()
    dict = {
        "Day": [currDate],
        'TimeStamp': [currTime],
        'Host': [host],
        "responseTime": [response],
        "Succeeded": [succeeded]
    }
    # responseToRawPing(str(response))
    writableResponse = pd.DataFrame.from_dict(dict)
    return writableResponse

def generateSpeedSQL(st_obj):
    # get current time
    up_speed = st_obj.upload()
    print("RAW UPSPEED" ,up_speed)
    down_speed = st_obj.download()
    # ping = st_obj.ping()
    currDateTime = datetime.now()
    # SQLTimestamp = currDateTime.strftime('%Y-%m-%d %H:%M:%S')
    # print("TIMESTAMPRAW", SQLTimestamp)
    sql = "INSERT INTO speed VALUES ('{}',{},{});".format(currDateTime, up_speed, down_speed)
    # dict = {'Day': [currDate], 'TimeStamp': [currTime], 'UploadSpeed': [str(up_speed) + " b/s"], 'DownloadSpeed': [str(down_speed) + " b/s"]}
    # writableResponse = pd.DataFrame.from_dict(dict)
    return sql

def storeSpeedToDB(sql, db_interactor):
    db_interactor.insertSpeed(sql)

# generates an object for storing the results of the pings and
# for use in writing to the csv file when given an response object
def generateOutSpeedObject(st_obj):
    # get current time
    up_speed = st_obj.upload()
    print("RAW UPSPEED" ,up_speed)
    down_speed = st_obj.download()
    # ping = st_obj.ping()
    # currDate = datetime.now().date()
    currDate = datetime.now()
    # SQLTimestamp = currDate.strftime('%Y-%m-%d %H:%M:%S')
    # print("TIMESTAMPRAW", SQLTimestamp)
    sql = 'INSERT INTO speed VALUES {},{},{}'.format(currDate, up_speed, down_speed)
    print("Converted SQL: ", sql)
    currTime = datetime.now().time()
    dict = {'Day': [currDate], 'TimeStamp': [currTime], 'UploadSpeed': [str(up_speed) + " b/s"], 'DownloadSpeed': [str(down_speed) + " b/s"]}
    writableResponse = pd.DataFrame.from_dict(dict)
    return writableResponse


# Generate the main folder if it doesnt exist
def generateHomeFolder(desktop_dir):
    fullhomedir = desktop_dir + _DIRECTORYMAIN
    if not os.path.isdir(fullhomedir):
        try:
            os.makedirs(fullhomedir, exist_ok= True)
        except OSError:
            print("#ERROR# Couldn't Create Home Directory on your Desktop")
        else:
            print(
                "Running for the first time, Creating a directory on your desktop to store the log files 'InternetTester'")
    return fullhomedir


def generateFile(filename, header):
    if not os.path.exists(filename):
        try:
            with open(filename, 'w') as file:
                file.close()
        except OSError:
            print("Couldnt create file:" + filename)
        else:
            print("Creating the file '{}' for storing info about internet outages".format(filename))
            #print file header if it is new:

            #convert header dict to dataframe:
            printable_header = pd.DataFrame.from_dict(header)
            printDataframeToFile(printable_header, filename)


def generateDesktopPath():

    desktop_dir = os.path.join(os.path.join((os.environ["USERPROFILE"]), "Desktop"))

    print("Found desktop at: {}".format(desktop_dir))
    return desktop_dir

def printDataframeHeaderToFile(writableResponses, file):
    writableResponses.to_csv(file, header=None, mode="a")

def printDataframeToFile(writableResponses, file):
    writableResponses.to_csv(file, header=None, mode="a")

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
