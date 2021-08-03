from modules import GlobalValues as GV
from pythonping import ping
import sys


class Pinger:
    def pinger(self, host):
        responses = ping(host, count=1)
        return responses

# TODO: Comment me
class Ping(Pinger):
    def __init__(self):
        self.host=""
    
    def run(self, db_interactor):
        responses = self.pinger(self.host)
        res = {}
        for response in responses:
            res = response
        print(res)
        sys.stdout.flush()
        db_interactor.insertPing(res, self.host)

class PingGoogle(Ping):
    def __init__(self):
        self.host = GV._GOOGLEHOST

class PingOpenDNS(Ping):
    def __init__(self):
        self.host = GV._OPENDNSHOST

class PingCloudFlare(Ping):
    def __init__(self):
        self.host = GV._CLOUDFLAREHOST