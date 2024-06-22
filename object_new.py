class Server:
<<<<<<< HEAD

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
=======
    def __init__(self, name, ip_address, environment):
        self.name = name
        self.ip_address = ip_address
        self.environment = environment
        self.status = 'stopped'  # default status

    def start(self):
        if self.status == 'stopped':
            self.status = 'running'
            print(f"{self.environment} server {self.name} started.")
        else:
            print(f"{self.environment} server {self.name} is already running.")

    def stop(self):
        self.status = 'stopped'
        print(f"{self.environment} server {self.name} stopped.")
       

    def restart(self):
        print(f"Restarting {self.environment} server {self.name}...")
        self.stop()
        self.start()

    def get_status(self):
        return f"{self.environment} server {self.name} is currently {self.status}."


class ProductionServer(Server):
    def __init__(self, name, ip_address):
        super().__init__(name, ip_address, 'Production')
        # Add any additional attributes or methods specific to ProductionServer

    # Example of an additional method
    def deploy(self):
        print(f"Deploying new release to production server {self.name}...")
z