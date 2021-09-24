import time  
import os
#!/usr/bin/python
import sys
import configparser

path = "../../../__data/"
config_file = "../../_config.ini"

# config = configparser.ConfigParser()
# config.read(path + config_file)
# print( config["topsecret.server.com"]['Port'])

def showKPIs():
    print("KPIs:\n")



var_i = ""
g_seconds = 5 #300

def main():
    global var_i 
    var_i = "test"
    # print("Hello, World!")
    #loop:
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("loop:{}seconds\n".format(g_seconds))
    i = 0
    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        i = i + 1
        print('i=' + str(i))
        showKPIs()
        time.sleep(g_seconds)


##########################################################################
##########################################################################
# $ python _moni.py arg1 arg2 arg3
if __name__== "__main__" :
    print( 'Number of arguments:' + str(len(sys.argv)) + ' arguments.' )
    print ( 'Argument List:' + str(sys.argv) ) 
    if len(sys.argv) > 1:
        g_seconds = int(sys.argv[1])
    else: 
        g_seconds = 5    
    main()
