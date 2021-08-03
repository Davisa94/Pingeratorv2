
class Ping:
    def __init__(self):
        self.host=""
        self.file=""
    
    def runLocal(self, db_interactor):
        responses = pinger(self.host)
        res = {}
        for response in responses:
            res = response
        wr = generateOutObject(res, self.host)
        printDataframeToFile(wr, self.file)
    
    def run(self, db_interactor):
        responses = pinger(self.host)
        res = {}
        for response in responses:
            res = response
        print(res)
        db_interactor.insertPing(res, self.host)

class PingGoogle(Ping):
    def __init__(self, desktop):
        self.host = _GOOGLEHOST
        self.file = desktop + _GOOGLEOUTFILE
        generateFile(self.file, _PINGDICT)



class PingOpenDNS(Ping):
    def __init__(self, desktop):
        self.host = _OPENDNSHOST
        self.file = desktop + _OPENDNSOUTFILE
        generateFile(self.file, _PINGDICT)

class PingCloudFlare(Ping):
    def __init__(self, desktop):
        self.host = _CLOUDFLAREHOST
        self.file = desktop + _CLOUDFLAREOUTFILE
        generateFile(self.file, _PINGDICT)