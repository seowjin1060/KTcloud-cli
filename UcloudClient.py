import sys
import make_signature_2 
import urllib.parse
import credit_configure
UCLOUD_API_URLS={
    'server' : 'https://api.ucloudbiz.olleh.com/server/v1/client/api',
    'loadbalancer'     : 'https://api.ucloudbiz.olleh.com/loadbalancer/v1/client/api',
    'waf'    : 'https://api.ucloudbiz.olleh.com/waf/v1/client/api',
    'watch'  : 'https://api.ucloudbiz.olleh.com/watch/v1/client/api',
    'package': 'https://api.ucloudbiz.olleh.com/packaging/v1/client/api',
    'autoscaling'     : 'https://api.ucloudbiz.olleh.com/autoscaling/v1/client/api',
    'cdn'    : 'https://api.ucloudbiz.olleh.com/cdn/v1/client/api',
    'msg'    : 'https://api.ucloudbiz.olleh.com/messaging/v1/client/api',
    'nas'    : 'https://api.ucloudbiz.olleh.com/nas/v1/client/api',
    'db'     : 'https://api.ucloudbiz.olleh.com/db/v1/client/api',
}

#Command_List = ["configure","ListAvailableProductTypes","delpoyVirtualMachine","startVirtualMachine","listVirtualMachines","listVirtualMachineForCharge"]
Ctype_List = ["configure","server"]

ctype = ""
command = ""
def main():
    cnt = 0
   
    if len(sys.argv) < 3:
##        if(sys.argv[1] == Command_List[0]):
##            configure()
##            ctype = sys.argv[1]
##        elif(sys.argv[1] == Command_List[1]):
##            ListAvailableProductTypes()
##        else:
        print ("usage: ucloudbiz [type] [command] [parameters] \n or type ucloudbiz help")
        exit(-1)
    else:
        ctype = sys.argv[1]
        command = sys.argv[2]
        for c in Ctype_List:
            if (c == sys.argv[1]):
                ctype = c
                cnt+=1
                break
        if(cnt == 0):
            print("unable to process command type 'ucloudcli help' to verify commands  ")
            exit(-1)
        ctype_process(ctype,command)      


    #signature = sig.sign_request_url(ZONE)

def ctype_process(ctype,command):
    print(command)
    if ctype == "configure":
        c = credit_configure.configure(command)
        c.command_process_configure()
    #elif ctype == "server":
        
    return



#def ListAvailableProductTypes():
    
main()
##def ListAvailableProductTypes():
##    return
