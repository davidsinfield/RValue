import urllib.request
import time
import socket
from datetime import datetime

def gettimestr():
    return str(datetime.now())


sites=["www.google.com","bt.com"]

print (gettimestr())
print (sites[0])
print (sites[1])
b=0

def doload(site):
    #print("doing site:"+'https://'+site)
    global b
    try:
        with urllib.request.urlopen('https://'+site) as response:
            html=response.read()
            if len(html)<100:
                print (gettimestr()+html)
            else:
                #print (gettimestr()+' Site '+ site + '  loaded')
                b=b+1
                if b % 50==0:
                    print (str(b)+" Successful downloads")
                
    except socket.gaierror as e:
        print (gettimestr()+"gaierror")
    except urllib.error.HTTPError as e:
        print (gettimestr()+site+" Exception:HTTPError ")
        print ("Successful downloads since last error: "+str(b))
        b=0
    except  urllib.error.URLError as e:
        print (gettimestr()+site +" Exception:URLError ")
        print ("Successful downloads since last error: "+str(b))
        b=0
while (1):
    for site in sites:
        doload(site)
    time.sleep(5)
    
