import make_signature_2
import requests
import json
class server:
    def __init__(self,input_command):
        self.credit = []
        file = open("credit.txt","r")
        for line in file:
            line = line.replace("\n","")
            self.credit.append(line)
        self.command_list = ["help","listAvailableProductTypes","delpoyVirtualMachine","startVirtualMachine","listVirtualMachines","listVirtualMachineForCharge"]
        self.command = input_command
        print(self.credit)
        self.apikey = self.credit[0]
        self.secret = self.credit[1] 
        self.Zone = self.credit[2]
        self.response = self.credit[3]
        self.url = "https://api.ucloudbiz.olleh.com/server/v1/client/api?"
        if(self.Zone == "KOR-Seoul M2"):
            self.url= "https://api.ucloudbiz.olleh.com/server/v2/client/api?"
        
    def execute(self):
        state = 0
        if self.command == "help":
            print("==========Supported server commands==========")
            for i in self.command_list:
                print("ucloudcli configure ",i)
        else:               
            for i in self.command_list:
                if(i == self.command):
                    state = 1
                    break
                    
            if(state == 0):
                print("unsupported command\n type 'ucloudcli server help' to view supported server command ")        
                exit(-1)
            
            sig = make_signature_2.sign_request_url(self.apikey,self.secret,self.command,self.response)
            query = self.url+"command="+self.command+"&response="+self.response+"&apiKey="+self.apikey+"&signature="+sig
            response = requests.get(query)
            res = response.json()
            print(res)
            for line in res[self.command.lower()+"response"]["producttypes"]:
                print(line)

              
