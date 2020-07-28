#Import modules 
import time 
from datetime import datetime as dt 
import json
import platform

#Looking for the host file
if platform.system()=='Windows':
    host_path_dns=r'C:\Windows\System32\drivers\etc\hosts'
elif platform.system()=='Linux':
    host_path_dns='/etc/hosts'

#Redirection path 
redirect='127.0.0.1'

#Blocked Sites 
website_list=[]
block_file=open('block_sites.txt','r').readlines()
for each in block_file:
    #Removing ascii chars at end
    if each[-1]=='\n':
        website_list.append(each[:-1])
    else:
        website_list.append(each)

#Delay time for running script 
delay=5

#Read working hours and free hours
time_dat=open('block_hours.txt','r').read()
time_dat=json.loads(time_dat)

work_hrs=time_dat['working']['hours']
work_mins=time_dat['working']['minutes']
work_secs=time_dat['working']['secs']
free_hrs=time_dat['free']['hours']
free_mins=time_dat['free']['minutes']
free_secs=time_dat['free']['secs']

#State change variable 
state=0

#Running script at regular intervals 
while (True):
    #Check if current time exits withing working hours 
    if dt(dt.now().year,dt.now().month,dt.now().day,work_hrs,work_mins,work_secs)<dt.now() and \
        dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,free_hrs,free_mins,free_secs):

        #Running 
        state=1

        with open(host_path_dns,'r+') as file:
            content=file.read()

            for website in website_list:
                #Website is already blocked
                if website in content:
                    pass
            
                #Block site (i.e. add to hosts file)
                else:
                    file.write(redirect+" "+website+"\n")
        print("Working hours")
    
    else:
        #Check if state was running and if so then unblock those sites
        if(state):
            with open(host_path_dns,'r+') as file:
                content=file.readlines()
                
                #Set pointer to starting 
                file.seek(0)

                #Check if no website exists in blocked file 
                #Then add that to file
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)

                file.truncate()

            #Set state to 0
            state=0
        else:
            pass
        print("Fun hours")  

    time.sleep(delay)
