import make_signature_2
import requests
import json
class server:
    def __init__(self,input_command,parameters):
        self.credit = []
        try:
            file = open("credit.txt","r")
        except:
            print("no credit file detected \nplease type 'ucloud configure init' to create credit files")
            exit(-1)
        for line in file:
            line = line.replace("\n","")
            self.credit.append(line)
        self.command_list = {"help":[],"listAvailableProductTypes":[],"deployVirtualMachine":["serviceofferingid","templateid","diskofferingid","zoneid"],"destroyVirtualMachine":["id"],"startVirtualMachine":["id"]
                            ,"listVirtualMachines":["state"],"listVirtualMachineForCharge":[],"stopVirtualMachine":["id"],"changeServiceForVirtualMachine":["id","serviceofferingid"],
                             "checkVirtualMachineName":["display_name"],"changeServiceForVirtualMachineVerify":["id","serviceofferingid"],"restoreVirtualMachine":["virtualmachineid"],
                             "updateVirtualMachine":["id","displayname","haenable"],"updateVirtualMachineForCharge":["id,usageplantype"],
                             "createVolume":["name","diskofferingid","zoneid","usageplantype","account","domainid","size","snapshotid","virtualmachineid","productcode","iops"],
                             "attachVolume":["id","virtualmachineid"],"detatchVolume":["deviceid","id","virtualmachineid"],"deleteVolume":["id"],"listVolumes":[],
                             "resizeVolume":["id","vmid","size","isLinux"],"updateUsagePlanTypeForServer":["type","usagePlanType","id"],"associateIpAddress":["zoneid","usageplantype","account","domainid","networkid"], "disassociateIpAddress":["id"],"listPublicIpAddresses":["account"],
                             "updateIpAddress":["desc","id"],"upateUsagePlanTypeForServer":["type","usagePlanType","id"],
                             "createPortForwardingRule":["ipaddressid","privateport","protocol","publicport","virtualmachineid","cidrlist","openfirewall","privateendport","publicendport"],
                             "deletePortForwardingRule":["id"],"listPortForwardingRules":["account","domainid","id","ipaddressid","keyword","page","pagesize","isrecursive","listall"],
                             "createFirewallRule":["ipaddressid","protocol","cidrlist","startport","endport","icmpcode","icmptype","type"], "deleteFirewallRule":["id"], "listFirewallRules":["account","domainid","id","ipaddressid","keyword","page","pagesize","srecursive"],"listAccounts":["accounttype","domainid","id","iscleanuprequired","isrecursive","keyword","name","page","pagesize","state","listall"],
                             "queryAsyncjobResult":["jobid"],"listEvents":["account","domainid","duration","startdate","enddate","entrytime","id","keyword","page","pagesize","type","isrecursive","listall"],
                             "createSnapshot": ["volumeid","account","domainid","policyid"],"deleteSnapshot":["id"],"listSnapshots":["account","domainid","id","intervaltype","isrecursive","keyword","name","page","pagesize","snapshottype","volumeid","listall"],"listSnapshotSize":["id"],"createTemplate":["displaytext","name","ostypeid"],
                             "deleteTemplate":["id","zoneid"],"updateTemplate":["id","bootable","displaytext","format","name","ostypeid","zoneid","isgroup","passwordenable","sortkey"],"listTemplates":["templatefilter"],"copyTemplate":["id","sourcezoneid","destzoneid"],
                             "listNetworks":[], "listNetworkUsages":["startdate","enddate"],"createNetwork":["displaytext","zoneid","account","domainid","ipcount"],"deleteNetwork":["id"],
                             "interAzStatus":["destnetworkid","sourcenetworkid"],"listNetworkFlatRate":[],"networkFlatRate":["type"],"addNicToVirtualMachine":["networkid","virtualmachineid","eid"],"removeNicFromVirtualMachine":["nicid","virtualmachineid"],"requestForInterAz":["destnetworkid","sourcenetworkid","destzoneid","sourcezoneid"],
                             "listZones":[],
                             "createSSHKeyPair":["Name"],"deleteSSHKeyPair":["Name"],"listSSHKeyPairs":["Name"],
                             "enableStaticNat":["ipaddressid","virtualmachineid"],"disableStaticNat":["ipaddressid"],
                             "createTags":["resourceids","resoucretype","Tags"], "deleteTags":["resourceids","resourcetype"],"listTags":[]
                             }
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
                if(i == "createVolume"):
                    print("========== Volume commands==========")
                elif(i == "associateIpAddress"):
                    print("========== IP address commands=======")
                elif(i == "createPortForwardingRule"):
                    print("==========  port forward commands=======")
                elif(i =="createFirewallRule"):
                    print("==========  firewall commands=======")
                elif(i == "createSnapshot"):
                    print("==========  snapshot commands=======")
                elif( i == "createTemplate"):
                    print("==========  Template commands=======")
                elif( i == "listNetworks"):
                    print("==========  Networks commands=======")
                elif( i == "createSSHKeyPair"):
                    print("==========  SSHKeyPair commands=======")
                elif( i == "enableStaticNat"):
                    print("==========  StaticNat commands=======")
                elif( i == "createTags"):
                    print("==========  Tag commands=======")
                print("ucloud server ",i," ",end='')
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
                        
                
