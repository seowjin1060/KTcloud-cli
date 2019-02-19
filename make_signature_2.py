import sys
import string
import hashlib
import base64
import hmac
import urllib
from base64 import b64encode
api_key = "your api key"
secret = "your secrete key"
s_key = "keokzhd"
region = ""
command = "listAvailableProductTypes"

def make_digest(key,message) :
    
##    digester = hmac.new(key, message, hashlib.sha1)
##    #signature1 = digester.hexdigest()
##    signature1 = digester.digest()
##    #print(signature1)
##    #signature2 = base64.urlsafe_b64encode(bytes(signature1, 'UTF-8'))
##    signature2 = base64.urlsafe_b64encode(signature1)    
##    #print(signature2)
##    #return str(signature2, 'UTF-8')
    signature = b64encode(hmac.new(
            secret,
            msg=message.lower(),
            digestmod=hashlib.sha1
    ).digest())
    return signature

def url_encode(input_list):
    urllib.urlencode(input_list)
    
def sign_request_url(input_url,s_key):
    args = {}
    args['command']  = command
    args['response'] = "json"
    args['apiKey']   = api_key
        
        # For safty reason, force Quote some character.
    for i in args.keys():
        args[i] = args[i].replace("%", "%26")
        args[i] = args[i].replace("/", "%2f")
        
    query = '&'.join(
        '='.join([k, urllib.quote(args[k])]) for k in sorted(args.keys(), key=str.lower))
    
    signature = make_digest(secret,query.lower())
    signature = urllib.quote(signature)
    print(query)
    print(signature)
    listAvailableProductTypes(signature,query)
    return signature

def listAvailableProductTypes(signature,query):
    request = "https://api.ucloudbiz.olleh.com/server/v1/client/api?" +"command="+command+"&response=json"+"&apiKey="+api_key+"&signature="+signature
    print(request)

    
def main():
    command_list = []
    
    input_url ="command=listVirtualMachines&name=VM_33111&state=Running&response=xml&apiKey=miVr6X" #"command=listVirtualMachines&apiKey="+api_key
    sign = sign_request_url(input_url,s_key)
 #   sign = urllib.parse.quote(sign.encode('utf-8'))
        
    #print(sign)
   
    
#    print()
main()
