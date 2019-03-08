class configure:
    def __init__(self,command):
        command_process_configure(command)
        
    def configure_init():
        m2_zone = False
        apikey_in = input("[api_key] :")
        secret_in = input("[secret key} :")
        zone_in = input("[data center] or type 'help' to check all aviliable zones :")
        while(zone_in == 'help' or zone_in not in ZONE):
            for name in ZONE:
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
    def configure_list():
        credit = open("credit.txt" , "r")
        print("API_KEY : ", credit.readilne())
        print("Secret Key : ", credit.readilne())
        print("Zone : ", credit.readline())
        print("response Type: ", credit.readline())
        return
    def command_process_configure(command):
        if command == "init":
            configure_init()
        elif command == "list":
            configure_list()
        else:
            print("no command matched")
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

