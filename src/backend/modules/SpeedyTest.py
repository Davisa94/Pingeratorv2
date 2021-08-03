import sys
import speedtest
################################################################
# A class that encapsulates the speedtest library and gives
# Useful methods for simplifying the process of managing 
# returned data
# Author: Austin Benitez
################################################################

class SpeedyTester:

    def run(self, db_interactor):
        st = speedtest.Speedtest()
        dl = st.download()
        dl = dl/1000000
        ul = st.upload()
        ul = ul/1000000
        print("Download: {} mb/s".format(dl))
        sys.stdout.flush()
        print("Upload: {} mb/s".format(ul))
        sys.stdout.flush()
        db_interactor.insertSpeed(st)