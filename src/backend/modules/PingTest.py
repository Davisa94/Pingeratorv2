from modules import GlobalValues
from pythonping import ping
class Pinger:
    def pinger(host):
        responses = ping(host, count=1)
        return responses

# TODO: Comment me
class Ping(Pinger):
    def __init__(self):
        self.host=""
    
    def run(self, db_interactor):
        responses = pinger(self.host)
        res = {}
        for response in responses:
            res = response
        print(res)
        db_interactor.insertPing(res, self.host)

class PingGoogle(Ping):
    def __init__(self):
        self.host = _GOOGLEHOST

class PingOpenDNS(Ping):
    def __init__(self):
        self.host = _OPENDNSHOST

class PingCloudFlare(Ping):
    def __init__(self):
        self.host = _CLOUDFLAREHOST