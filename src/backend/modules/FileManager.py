import os
from modules import GlobalValues as GV
import pandas as pd
from datetime import datetime
import time
# generates an object for storing the results of the pings and
# for use in writing to the csv file when given an response object
def generateOutObject(response, host):
    # get current time
    succeeded = response.success
    currDate = datetime.now().date()
    currTime = datetime.now().time()
    dict = {
        "Day": [currDate],
        'TimeStamp': [currTime],
        'Host': [host],
        "responseTIme": [response],
        "Succeeded": [succeeded]
    }
    writableResponse = pd.DataFrame.from_dict(dict)
    return writableResponse


# generates an object for storing the results of the pings and
# for use in writing to the csv file when given an response object
def generateOutSpeedObject(st_obj):
    # get current time
    up_speed = st_obj.upload()
    down_speed = st_obj.download()
    # ping = st_obj.ping()
    currDate = datetime.now().date()
    currTime = datetime.now().time()
    dict = {'Day': [currDate], 'TimeStamp': [currTime], 'UploadSpeed': [str(up_speed) + " b/s"], 'DownloadSpeed': [str(down_speed) + " b/s"]}
    writableResponse = pd.DataFrame.from_dict(dict)
    return writableResponse


# Generate the main folder if it doesnt exist
def generateHomeFolder(desktop_dir):
    fullhomedir = desktop_dir + GV._DIRECTORYMAIN
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
