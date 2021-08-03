import sys,json
data = sys.stdin.readlines()
data = json.loads(data[0])
print(data[0]+10)
sys.stdout.flush()

def getRecentPings():
    pass


def parseInput():
    data = sys.stdin.readlines()
    functionCall = json.loads(data[0])
    functionArgs = json.loads(data[0])

