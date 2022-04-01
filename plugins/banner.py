__Name__ = "Collector"
__Description__ = "Fetch all endpoints from a given domain"
__Author__ = "Md. Nur Habib"
__Version__ = "1.0.0"


reset='\033[0m'
bold='\033[01m'
disable='\033[02m'
underline='\033[04m'
reverse='\033[07m'
strikethrough='\033[09m'
invisible='\033[08m'
black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'



def Bannerfunction():
    print(f"""{bold}{yellow}

            _ _           _             
           | | |         | |            
   ___ ___ | | | ___  ___| |_ ___  _ __ 
  / __/ _ \| | |/ _ \/ __| __/ _ \| '__|
 | (_| (_) | | |  __/ (__| || (_) | |   
  \___\___/|_|_|\___|\___|\__\___/|_|{blue} {__Version__}
{red}
                          @thenurhabib {reset}
  
          """)
