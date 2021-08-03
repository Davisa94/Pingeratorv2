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
        print(st.download())
        db_interactor.insertSpeed(st)