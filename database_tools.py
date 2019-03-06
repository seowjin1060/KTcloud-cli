import make_signature_2
import requests
import json


class database:
    def __init__(self,input_command,parameters):
        self.credit = []
        self.command_list = {"createInstance":[] , "listInstances":["instanceids"],"updateInstancePerfClass":["instanceid","perfclass"],
        "updateInstanceStorageSize":["instanceid","storagesize","usageplantype"],"updateInstanceBackup":["instanceid","backupretention","backupstarthour","backupstartmin","backupduration"],
        "updateInstanceMaintenance":["instanceid","maintenanceweekday","maintenancestarthour","maintenancestartmin","maintenanceduration"],"updateInstanceParameterGroup":["instanceid","parametergroupid"],"updateInstancePassword":["instanceid","dbmasterpassword"],
        "updateInstanceAccessControlGroup":["instanceid","accesscontrolgroupids"],"startInstance":["instanceid"],"restartInstance":["instanceid"],"deleteInstance":["instanceid"],"createParameterGroup":["sourceparametergroupid","parametergroupname","parameters.name","parameters.value"],
        "listParameterGroupEntries":["parametergroupid"],"listParameterGroups":["parametergroupids"],"deleteParameterGroup":["parametergroupids"]}
        try:
            file = open("credit.txt","r")
        except:
            print("no credit file detected \nplease type 'ucloud configure init' to create credit files")
            exit(-1)
        for line in file:
            line = line.replace("\n","")
            self.credit.append(line)
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

    def execute():
        state = 0
        p_types = []
        p_dict = {}
        if self.command == "help":
            print("==========Supported Database commands==========")
            for i in self.command_list:
                if(i == "createInstance"):
                    print("========== Instance ==========")
                elif(i == "ceateParameterGroup"):
                    print("========== Parameter group =======")
                elif(i == "listEvents"):
                    print("==========  Event =======")
                elif(i =="recoverFromBackup"):
                    print("========== Backup =======")
                elif(i == "createReplicationGroup"):
                    print("==========  Replication group =======")
                elif( i == "createTemplate"):
                    print("==========  HA group =======")
                elif( i == "createAccessControlGroup"):
                    print("==========  Access Control Group =======")
                elif( i == "queryAsncJobResult"):
                    print("==========  Asnchronous job =======")

                for i in self.command_list[i]:
                    print('[',i,']',' ',end='')
                print("")
            print("=============================================")
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
 #           print("res_url:",query)
            response = requests.get(query)
            res = response.json()
            if response.status_code != 200:
                 print(response.status_code)
                 print(response.text)
                 print("what")
            else:
                key = ""
                for line in res[self.command.lower()+"response"]:
                    if(line == "count"):
                        continue
                    else :
                        key = line
                    print(key)
                    #break
                for line in res[self.command.lower()+"response"][key]:
                    #a = line["producttypes"]
                    print("====================================================")
                    for l in line:
                        print(l,":",line[l])
                    print("=====================================================")
                        #print(l)
                        #print("")
                    #break
                   # for a in res[self.command.lower()+"response"][key][line]:
