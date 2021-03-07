#!/usr/bin/python
import sys

import configparser

path = "../../../__data/"
config_file = "_config.ini"

# config = configparser.ConfigParser()
# config.read(path + config_file)
# print( config["topsecret.server.com"]['Port'])
var_i = ""
def main():
    global var_i 
    var_i = "test"
    print("Hello, World!")

##########################################################################
##########################################################################
# $ python test.py arg1 arg2 arg3
# if __name__== "__main__" :
    main()
    # print( 'Number of arguments:' + str(len(sys.argv)) + ' arguments.' )
    # print ( 'Argument List:' + str(sys.argv) )