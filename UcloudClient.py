import sys
import make_signature

UCLOUD_API_URLS={
    'server' : 'https://api.ucloudbiz.olleh.com/server/v1/client/api',
    'lb'     : 'https://api.ucloudbiz.olleh.com/loadbalancer/v1/client/api',
    'waf'    : 'https://api.ucloudbiz.olleh.com/waf/v1/client/api',
    'watch'  : 'https://api.ucloudbiz.olleh.com/watch/v1/client/api',
    'package': 'https://api.ucloudbiz.olleh.com/packaging/v1/client/api',
    'as'     : 'https://api.ucloudbiz.olleh.com/autoscaling/v1/client/api',
    'cdn'    : 'https://api.ucloudbiz.olleh.com/cdn/v1/client/api',
    'msg'    : 'https://api.ucloudbiz.olleh.com/messaging/v1/client/api',
    'nas'    : 'https://api.ucloudbiz.olleh.com/nas/v1/client/api',
    'db'     : 'https://api.ucloudbiz.olleh.com/db/v1/client/api',
}
ZONE= {1:"KOR-Central A", 2:"KOR-Central B", 3:"KOR-HA", 4:"KOR Seoul-M", 5:"JPN", 6:"US-West",7:"KOR-Seoul M2"}
RESPONSE_TYPE=['json','xml']    
Command_List = ["configure","ListAvailableProductTypes","delpoyVirtualMachine","startVirtualMachine","listVirtualMachines","listVirtualMachineForCharge"]


def main():
    cnt = 0
    m2_zone = False
    if len(sys.argv) != 1:
        print ("usage: ucloudbiz [commnand] [parameters] \n or type ucloudbiz help")
        exit(-1)
    else:
        for c in Command_List:
            if (c == argv[1]):
                command = c
                cnt+=1
                break
        if(cnt == 0):
            print("unable to process command type 'ucloudcli help' to verify commands  ")
            exit(-1)
        command_process(command)
        
    command = sys.argv[1]
    client = Client()
    result = client.request(command)

def configure():
    apikey_in = input("[api_key] :")
    secret_in = input("[secret key} :")
    zone_in = input("[data center] or type 'help' to check all aviliable zones :")
    while(zone_in == 'help'):
        for index,name in ZONE:
            print(name)
        zone_in = input("[data center] or type 'help' to check all aviliable zones :")

    for i in ZONE:
        if(zone_in.lower() == i):
            zone_in=i
            
    response = input("[response type] :")
    
    sig = make_signature()
    if zone_in == "KOR-Seoul M2":
        m2_zone = True
    signature - sig.sign_request_url()

def command_process(command):
    if command == "configure":
        configure()
    elif command == "ListAvailableProductTypes":
        ListAvailableProductTypes()
    elif command == "deployVirtualMachnine":
        deployVirtualMachine()
    elif command == "startVirtualMachine" :
        startVirutualMachine()
        
    else:
        print("no command matched")
    return                
                
##def ListAvailableProductTypes():
##    return
