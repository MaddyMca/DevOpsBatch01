class Server:
    def __init__(self, name, IPAddress):
        self.name = name
        self.IPAddress = IPAddress
        self.status = 'stopped'  # default status
    def printname(self):
        print(self.name, self.IPAddress)

class DataServer(Server):
    def __init__(self, name, IPAddress, userName, password):
        super.__init__(name, IPAddress)
        self.userName = userName
        self.password = password
    def connect(self):
        print("connected with "+self.userName)


class WebServer(Server):
    def __init__(self, name, IPAddress, url):
        super.__init__(name, IPAddress)
        self.url = url
    def connect(self):
        print("connected with "+self.url)

serverName = "xyz"
IPAddress ="1.1.1.127"
userName = "abc"
password = "pass"
DS = DataServer(serverName, IPAddress, userName, password)
DS.connect()








