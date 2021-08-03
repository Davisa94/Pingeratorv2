_DIRECTORYMAIN = '\\InternetTester\\responses'
# The interval between rounds of testing
_TESTINTERVAL = 8
_GOOGLEOUTFILE = '\\googleResponses.csv'
_CLOUDFLAREOUTFILE = "\\cloudFlareResponses.csv"
_OPENDNSOUTFILE = "\\openDns.csv"
_SPEEDSOUTFILE = "\\speeds.csv"
_CLOUDFLAREHOST = "1.1.1.1"
_GOOGLEHOST = "8.8.8.8"
_OPENDNSHOST = "208.67.222.222"
_PINGDICT = {
    'Day': ['Day'],
    'TimeStamp': ['TimeStamp'],
    'Host': ['Host'],
    'responseTIme': ['ResponseTime'],
    'Succeeded': ['Succeeded']
}
_SPEEDDICT = {
    'Day': ['Day'],
    'TimeStamp': ['TimeStamp'],
    'UploadSpeed': ['UploadSpeed'],
    'DownloadSpeed': ['DownloadSpeed'],
    'FullResponse': ['FullResponse']
}