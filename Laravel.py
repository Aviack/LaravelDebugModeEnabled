import   sys , argparse , os  , json , time 
# need to learn aboyt argparse , validators , tldextract and figlet
from colorama import Fore ,Style , init
import requests,re
import time
from shodan import Shodan
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from pyfiglet import Figlet
#All is well buddy 
# Displaying the banner - starting
custom_fig = Figlet(font='slant')
print(Fore.BLUE + Style.BRIGHT + custom_fig.renderText('-------------') + Style.RESET_ALL)
print(Fore.BLUE + Style.BRIGHT + custom_fig.renderText('Laravel-Debug-ModeEnabled') + Style.RESET_ALL)
print(Fore.GREEN + Style.BRIGHT + "____________________ Avadh Dobariya --> Aviack ____________________\n")
print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "-----> Twitter   : https://twitter.com/AviackOG\n")
print(Fore.MAGENTA + Style.BRIGHT + "-----> GitHub    : https://github.com/Aviack\n")
print(Fore.MAGENTA + Style.BRIGHT + "-----> LinkedIn  : https://www.linkedin.com/in/avadh-dobariya-a27342156/\n")
print(Fore.BLUE + Style.BRIGHT + custom_fig.renderText('-------------') + Style.RESET_ALL)
# Displaying the banner ending the

#Now it;s time to handle the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d" , "--domainList" , type=str, help="provide the path list of domain")
parser.add_argument("-s" , "--shodanKey" , type=str, help="provide the shodan key")
args = parser.parse_args()
#Handling of arguments ends


class Arguments():
    def __init__(self,wordlist,shodanKey):
        self.wordlist=wordlist
        self.shodanKey=shodanKey
        self.ListOfDomains = []
        #self.checkWordListFormat() #Word list should be in format domain.com and not www.domain.com and if in case it is in that format make it like domain.com
        #self.strip
        
    def PathDoesExistOrNot(self): #Return True or False for the path
        if  os.path.exists(self.wordlist):
             return True
        else:
            return False
    def returnShodanKey(self): # return type string
        return self.shodanKey
    def getThePath(self): 
        return self.wordlist
    def returnWordList(self): # return type list
        listOfDomain =  open(self.wordlist)
        for word in listOfDomain:
            self.ListOfDomains.append(word.rstrip("\n"))
        return self.ListOfDomains
        







class LaravelDebugMOdeList:
    def __init__(self,domainList,Shodankey):
        self.domainList=domainList # returnWordList --> argument.returnWordList()
        self.Shodankey=Shodankey # returnShodanKey  -->argument.returnShodanKey()
                    

        self.laravel_debug_list = [] # list to store laravel_debug_list # this What I return
        self.domainIp = {} # to understand Which IP belongs to which Domain
    def return_domain_List(self):
        return self.domainIp

    def LaravelList(self): # returns the list
        
        fileName = "domainIpFile.txt"
        path = os.path.join(os.getcwd(),fileName)

        domainIpFile = open(path, "w")
        api = Shodan(self.Shodankey)
        for word in self.domainList:
            query = "html:'URLconf defined' ssl:" + word.strip('\n') # construct the shodan query with the help of wordlist 
            try:
                results =  api.search(query)
                time.sleep(1)
                print("Result found:{}".format(str(results['total'])) + "  for:{}".format(word))
                for result in results['matches']:
                    self.domainIp[result['ip_str']] = word.rstrip("\n")
                    port = result['port']
                    if port in [80 , 443]:
                        if port ==  443:
                            ip = "https://"+result['ip_str']
                        else:
                            ip = "https://"+result['ip_str']
                    else:
                        ip = "https://"+result['ip_str']+":"+str(port)
                    self.laravel_debug_list.append(ip)
                    

            except Exception as e:
               print(e)
        domainIpFile.write(json.dumps(self.domainIp))
        return self.laravel_debug_list 
    
    
         
class AutomationAndReporting():
    def __init__(self):
        self.listContainingDJango=[]
        self.IpFinalList = []
    def IpChecking(self,laravel_debug_list): # this list is ==> LaravelList.LaravelList() 
        regex = r"(?:mongodb|redis):\/\/"

        for ip in laravel_debug_list:
            ipaddress = ip[8:len(ip)]
            try:
                response = requests.post(url=ip.rstrip("\n")+"/admin", data = {} , verify=False)
                finalDecodedResponse= response.content.decode("utf-8") ##Solves the cannot use string pattern on byte like object || byte object is not callable for respose.content() 
                if re.search(regex,finalDecodedResponse):
                    self.listContainingDJango.append(ipaddress)
        
            except Exception as e:
                print(e) 
        return self.listContainingDJango
    
    def reportMaking(self,domainAndIp): #domainAndIp -->.return_domain_List()
        fileName = "FinalResponse.txt"
        path = os.path.join(os.getcwd(),fileName)
        FinalResponse =  open(path, "w") 

        IpAddressDummmy = self.IpChecking(LaravelList.LaravelList())
        for ip in IpAddressDummmy:
            string1 = "https://"
            finalString = string1+ip
            self.IpFinalList.append(finalString)
        for list in self.IpFinalList:
            ips = list[8:].rstrip("\n")
            try:
                response = requests.post(url=list.rstrip("\n")+"/admin", data = {} , verify=False)
                finalDecodedResponse= response.content.decode('utf-8')
                FinalResponse.write(str(list)+"\n")
                FinalResponse.write(str(domainAndIp[ips])+"\n"*3)
                FinalResponse.write(finalDecodedResponse+"\n"*5)
                FinalResponse.write("__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________\n")




            except Exception as e:
                print("There is something wrong in the code ")
                print(ip)

    




        



argument = Arguments(args.domainList , args.shodanKey)
LaravelList = LaravelDebugMOdeList(argument.returnWordList(),argument.returnShodanKey())
automatinoOne = AutomationAndReporting()
#all=automatinoOne.IpChecking(LaravelList.LaravelList())
reportMakingOne = automatinoOne.reportMaking(LaravelList.return_domain_List())
print(all)

#print(p)


