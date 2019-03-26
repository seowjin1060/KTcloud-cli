import make_signature_2
import requests
import json
import urllib.request

class stotageV2:
    def __init__(self,input_command,parameters):
        self.credit = []
        self.command_list = {"auth":["host", "Content-Type", "domain", "auth","name","user","password","identity","methods","scope"]}
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
        self.url = "https://ssproxy.ucloudbiz.olleh.com/auth/v1.0"
        if(self.Zone == "KOR-Seoul M2"):
            self.url= "https://api.ucloudbiz.olleh.com/server/v2/client/api?"

    def execute(self):
        state = 0
        p_types = []
        p_dict = {}
        if self.command == "help":
            print("==========Supported storage 2.0 commands==========")
            for i in self.command_list:
                if(i == ""):
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
                
           # query = self.url+"command="+self.command
            for i in p_dict:
                query = query + "&"+i+"="+p_dict[i]
            #HttpGet httpget = new HttpGet("https://ssproxy.ucloudbiz.olleh.com/auth/v1.0");
		    #httpget.setHeader("X-Auth-Token" :"MTQzODE2MjE1MDE0MzgxNTYyOTU2NjYw")
		   # HttpResponse response = null;
		   # HttpEntity entity = null;
		    #StatusLine res_sl = null;
		    #Header[] res_header = null;
		    #BufferedReader in = null;
            requests.get("https://ssproxy.ucloudbiz.olleh.com/auth/v1.0", headers={"X-Auth-Token" :"MTQzODE2MjE1MDE0MzgxNTYyOTU2NjYw"})

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
