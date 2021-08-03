import speedtest
################################################################
# A class that encapsulates the speedtest library and gives
# Useful methods for simplifying the process of managing 
# returned data
# Author: Austin Benitez
################################################################

class SpeedyTester:
    def __init__(self, desktop):
        self.file = desktop + _SPEEDSOUTFILE
        generateFile(self.file, _SPEEDDICT)

    def runLocal(self):
        print("The full path to my log files is at: {} ".format(self.file))
        st = speedtest.Speedtest()
        # print("Success" if res.success else " Failed")
        print("Speeds: ", st)
        wr = FM.generateOutSpeedObject(st)
        FM.printDataframeToFile(wr, self.file)

    def run(self, db_interactor):
        st = speedtest.Speedtest()
        print(st.download())
        db_interactor.insertSpeed(st)