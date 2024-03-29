# Author: Waqar Ali Abbas
# yellowpages.ca Data scraper Tool
import requests
import time
from bs4 import BeautifulSoup
from colorama import Fore,Back,Style
import os
os.system("clear")
print(f"{Fore.CYAN}\n\n----> DEVELOPER WAQAR ALI ABBAS")
print(f"{Fore.GREEN}----> YELLOW PAGES DATA SCRAPER TOOL")
print(f"{Fore.RED}----> PHANTOM LEGEND")
print(f'''{Fore.YELLOW}
██╗    ██╗ █████╗  ██████╗  █████╗ ██████╗ 
██║    ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗
██║ █╗ ██║███████║██║   ██║███████║██████╔╝
██║███╗██║██╔══██║██║▄▄ ██║██╔══██║██╔══██╗
╚███╔███╔╝██║  ██║╚██████╔╝██║  ██║██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝╚═╝  ╚═╝                     
''')
print(f'''{Fore.YELLOW}
 Fight With Bugs-               |     |
                                \\_W_//
                                \/=|=\/
                                 [=v=]
                               __\___/_____
                              /..[  _____  ]
                             /_  [ [  W /] ]
                            /../.[ [ A /@] ]
                           <-->[_[ [Q /@/] ]
        KING IS HERE      /../ [.[ [ /@/ ] ]
     _________________]\ /__/  [_[ [/@/ A] ]
    <_________________>>0---]  [=\ \@/ R / /
       ___      ___   ]/000o   /__\ \ / / /
          \    /              /....\ \_/ /
       ....\||/....           [___/=\___/
      .    .  .    .          [...] [...]
     .      ..      .         [___/ \___]
     .    0 .. 0    .         <---> <--->
  /\/\.    .  .    ./\/\      [..]   [..]
 / / / .../|  |\... \ \ \    _[__]   [__]_
/ / /       \/       \ \ \  [____>   <____]
''')
print(f"{Fore.RED}           ------------------------------------")
print(f"{Fore.WHITE}          CERTIFIED INFORMATION SYSTEM SECURITY \n              PROFESSIONAL WAQAR ALI ABBAS")
print(Style.RESET_ALL)
# -------- URL Pagination 
for page in range(0,60+1):
    url=f"https://www.yellowpages.ca/search/si/{page}/Grocery+Stores/Toronto+ON"
    get=requests.get(url)
    soup=BeautifulSoup(get.content,"html.parser")
    numbers=soup.find_all("li","mlr__submenu__item")
    for i in numbers:
        var=i.next_element.string
        with open("number.txt","a",encoding="UTF-8") as f:
            f.write(f"{var}\n")
    spans=soup.find_all("span","jsMapBubbleAddress")
    list_=["Address","City","State","Postal-Code"]
    index_list=0
    for text in spans:
        if index_list==0:
            var2=f"{list_[index_list]}: {text.string}"
            print(f"{Fore.GREEN}DATA HAVE BEEN STORED IN  Address.txt FILE...")
            time.sleep(0.2)
            with open("Address.txt","a",encoding="UTF-8") as f:
                f.write(f"{var2}\n")
        if index_list==1:
            var3=f"{list_[index_list]}: {text.string}"
            print(f"{Fore.GREEN}DATA HAVE BEEN STORED IN  City.txt FILE...")
            time.sleep(0.2)
            with open("City.txt","a",encoding="UTF-8") as f:
                f.write(f"{var3}\n")
        if index_list==2:
            var4=f"{list_[index_list]}: {text.string}"
            print(f"{Fore.GREEN}DATA HAVE BEEN STORED IN  State.txt FILE...")
            time.sleep(0.2)
            with open("State.txt","a",encoding="UTF-8") as f:
                f.write(f"{var4}\n")
        if index_list==3:
            var5=f"{list_[index_list]}: {text.string}"
            print(f"{Fore.GREEN}DATA HAVE BEEN STORED IN  Postal.txt FILE...")
            time.sleep(0.2)
            with open("Postal.txt","a",encoding="UTF-8") as f:
                f.write(f"{var5}\n")
        index_list+=1
        if index_list==4:
            index_list=0
    print(f"{Fore.CYAN}\nPROCESSING PLEASE WAIT...")
    print(Style.RESET_ALL)
