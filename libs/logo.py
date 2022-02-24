# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = ''' \033[0;96m __  __        __  ______  ____
 \033[0;96m________________   ________________________________________________
____  _/_  ____/   ___  __ \__  ____/__  __ \_  __ \__  __ \__  __/
 __  / _  / __     __  /_/ /_  __/  __  /_/ /  / / /_  /_/ /_  /  ® \033[0m|| Created By Im Boot 
__/ /  / /_/ /     _  _, _/_  /___  _  ____// /_/ /_  _, _/_  /    
/___/  \____/      /_/ |_| /_____/  /_/     \____/ /_/ |_| /_/     
                                                         '''



def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.YELLOW + "      TheDbSearcher Project: https://discord.gg/JCsHZ43"+ Style.RESET_ALL + Style.BRIGHT)
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
