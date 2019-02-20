import make_signature_2
import requests
import json
class server:
    def __init__(self,input_command,parameters):
        self.credit = []
        file = open("credit.txt","r")
        for line in file:
            line = line.replace("\n","")
            self.credit.append(line)
        self.command_list = {"help":[],"listAvailableProductTypes":[],"delpoyVirtualMachine":["productcode","zoneid"],"startVirtualMachine":["id"]
                            ,"listVirtualMachines":["state"],"listVirtualMachineForCharge":[]}
        self.command = input_command
        #print(self.credit)
        self.apikey = self.credit[0]
        self.secret = self.credit[1] 
        self.Zone = self.credit[2]
        self.response = self.credit[3]
        self.parameters = parameters
        self.url = "https://api.ucloudbiz.olleh.com/server/v1/client/api?"
        if(self.Zone == "KOR-Seoul M2"):
            self.url= "https://api.ucloudbiz.olleh.com/server/v2/client/api?"
    
    def execute(self):
        state = 0
        p_types = []
        p_dict = {}
        if self.command == "help":
            print("==========Supported server commands==========")
            for i in self.command_list:
                print("ucloudcli server ",i)
        else:               
            for i in self.command_list:
                if(i == self.command):
                    state = 1
                    p_types = self.command_list[i]
                    break
                    
            if(state == 0):
                print("unsupported command\n type 'ucloudcli server help' to view supported server command ")        
                exit(-1)
            if(len(self.parameters) < len(self.command_list[self.command])):
                print("less parameter given",len(self.parameters)," expected",len(self.command_list[self.command]))
                exit(-1)
            elif(len(self.parameters) > len(self.command_list[self.command])):
                print("too many parameter given",len(self.parameters)," expected",len(self.command_list[self.command]))
                exit(-1)
            cnt = 0
            
            for i in p_types:
                par = self.parameters[cnt]
                p_dict[i] = par                                          
                cnt+=1
                
            sig = make_signature_2.sign_request_url(self.apikey,self.secret,self.command,self.response,p_dict)
            query = self.url+"command="+self.command
            for i in p_dict:
                query = query + "&"+i+"="+p_dict[i]
            query +="&response="+self.response+"&apiKey="+self.apikey+"&signature="+sig
            print("res_url:",query)
            response = requests.get(query)
            res = response.json()
            if response.status_code != "200":
                print(response.text)
            else:
                key = ""
                for line in res[self.command.lower()+"response"]:
                    key = line
                    break
                print(str(key))
                for line in res[self.command.lower()+"response"][key]:
                    print(line)

                
