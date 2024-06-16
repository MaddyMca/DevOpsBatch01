class Server:

    def init(self, name, ip_address):

        self.name = name

        self.ip_address = ip_address

   

    def get_details(self):

        return  "Server Name: {self.name}, IP Address: {self.ip_address}"

# Creating instances for different server environments

production_server = Server("Production Server", "192.168.1.1")

test_server = Server("Test Server", "192.168.1.2")

development_server = Server("Development Server", "192.168.1.3")

# Accessing data within the Server class

print(production_server.get_details())

print(test_server.get_details())

print(development_server.get_details())