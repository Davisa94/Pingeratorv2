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
        print("Download: {}b/s".format(st.download()))
        sys.stdout.flush()
        print("Upload: {}b/s".format(st.upload()))
        sys.stdout.flush()
        db_interactor.insertSpeed(st)