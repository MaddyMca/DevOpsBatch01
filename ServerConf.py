
import time

class environment:
    def __init__(self, name, configurations):
        self.name = name
        self.configurations = configurations 
        print("created Env")


class configuration:
    def __init__(self, config_name, config_value, version, timestamp):
        self.config_name = config_name
        self.config_value = config_value
        self.version = 0
        self.timestamp = timestamp
        versions_config = [self.config_value]

    def get_config_name(self): 
        return str(self.config_name) 
    
    def set_config_name(self, config_name):
        self.config_name = config_name
    
    def get_config_value(self): 
        return str(self.config_value) 
    
    def set_config_value(self, config_value): 
        versions_config.append(config_value)
        version = version+1
        self.config_value = config_value
    
    def rollBack(self, version_num):
        if 0 <= int(version_num) < len(versions_config):
            self.config_value = versions_config[int(version_num)]
        

    
class environmentManager:
        def __init__(self):
            self.environments = []
            print("environmentManager")

        def add(self, environmentObj):
            print("environmentManager add")
            self.environments.append(environmentObj)
            print("environmentManager added "+str(len(self.environments)))

        def delete(self, envName):
            for x in self.environments:
                if x.name == envName :
                    self.environments.remove(x)

        def listEnvironments(self):
            print("list "+str(len(self.environments)))
            for x in self.environments:
                print("Envirnmanent Name : "+x.name)
                print("configurations : \n")
                for conf in x.configurations:
                    print(str(conf.get_config_name())+" : "+str(conf.get_config_value()))


envMgr = environmentManager()
while (True):
    inp = int(input('enter the option \n 1. for adding an environment \n 2. for delete environment \n 3. for Listsing all environments \n 0. for exit \n'))
    if(inp == 1):
        envName = input("enter the name of Env\n")
        configurations = []
        while(True):
            addMore = input("Press 11 if all confs are added.\n")
            if addMore == "11":
                break
            confName = input("enter the conf Name\n")
            confValue = input("enter the conf Value\n")
            configurations.append(configuration(confName, confValue, 0, time.time()))
        envMgr.add(environment(envName, configurations))
    if(inp == 2):
        envName = input("enter the name of Env to delete\n")
        envMgr.delete(envName)
    if(inp == 3):
        envMgr.listEnvironments()
        print("list env")
    if(inp == 0):
        print("break")
        break

