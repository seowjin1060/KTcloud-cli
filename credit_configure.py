

class configure:
    def __init__(self,input_command):
        self.command  = input_command
        self.commands = ["init","list"]
        self.ZONE= {"KOR-Central A":"1", "KOR-Central B":'2', "KOR-HA":'3', "KOR-Seoul M2":"4", "JPN":"5", "US-West":"6",}
        self.RESPONSE_TYPE=['json','xml']
    def configure_init(self):
        m2_zone = False
        apikey_in = input("[api_key] :")
        secret_in = input("[secret key} :")
        zone_in = input("[data center] or type 'help' to check all aviliable zones :")
        while(zone_in == 'help' or zone_in not in self.ZONE):
            for name in self.ZONE:
                print(name)
            zone_in = input("[data center] or type 'help' to check supported zones :")
    #    for i in ZONE:
    #        if(zone_in.lower() == i):
    #            zone_in=i
        response = input("[response type] or type help to check supported response :")
        if zone_in == "KOR-Seoul M2":
            m2_zone = True
        t = open("credit.txt","w")
        t.write(apikey_in+"\n")
        t.write(secret_in+"\n")
        t.write(zone_in+"\n")
        t.write(response+"\n")
        t.write(str(m2_zone)+ "\n")
        t.close()
        return

    def configure_list(self):
        credit = open("credit.txt" , "r")
        print("API_KEY : ", credit.readilne())
        print("Secret Key : ", credit.readilne())
        print("Zone : ", credit.readline())
        print("response Type: ", credit.readline())
        return
    
    def command_process_configure(self):
        command = self.command
        if command == "init":
            self.configure_init()
        elif command == "list":
            self.configure_list()
        elif command == "help":
            print("==========Supported configure commands==========")
            for i in self.commands:
                print("ucloudcli configure ",i)
        else:
            print("no command matched for "+"'ucloudcli configure"+command+"'"+ "\n" +"type 'ucloudcli configure help' to to view supported configure command'")
            exit(-1)

    ##def command_process_server(command):
    ##    if ctype == "List"
    ##        
    ##    elif ctype == "ListAvailableProductTypes":
    ##        ListAvailableProductTypes()
    ##    elif ctype == "deployVirtualMachnine":
    ##        deployVirtualMachine()
    ##    elif ctype == "startVirtualMachine" :
    ##        startVirutualMachine()
    ##    else:
    ##        print("no command matched")

