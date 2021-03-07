#!/usr/bin/python
import sys
import configparser

# import http.client
import requests
import json
import xml.etree.ElementTree as ET
import time
import re
from datetime import datetime
import pandas as pd

# from getpass import getpass
# >>> requests.get('https://api.github.com/user', auth=('username', getpass()))
from requests.auth import HTTPBasicAuth

path = "../../../__data/"
config_file = "_config.ini"

# config = configparser.ConfigParser()
# config.read(path + config_file)
# print( config["topsecret.server.com"]['Port'])

l_url = 'Northwind'
l_url = 'https://services.odata.org/V2/Northwind/Northwind.svc/'

params = [{ "h": l_url , "u" : "user",   "p":"***" , "e": "", "f" : "" , "es":""   },
          { "h": l_url , "u" : "user",   "p":"***" , "e": "/Products", "f": "?$format=json", "es": "x" },
          { "h": l_url , "u" : "user",   "p":"***" , "e": "/Products(1)", "f": "?$format=json", "es": "" },
          {}]

######################################################################################################
def WS_CALL( par ): 
    querystring = '' #param
    url = par["h"] +  par["e"] +  par["f"] 

    print(url)
    #print(param)
    payload = ''    
    headers = { 'Content-Type': "application/json", 'cache-control': "no-cache"    }
    response = requests.request("GET", url , data=payload, params=querystring , headers=headers,  
                                        #auth=HTTPBasicAuth( par["u"] ,par["p"]  ) , 
                                        verify=False)
    
    if(response.status_code == 200): 
        print("success")
        #print(response.text)
        #print(len(response.text) )
        #return response.text
        try:
            jj = json.loads(response.text)
        except: 
            return response.text
        
        if( par["es"] == "x"):
            print( "count: {}".format(len( jj["d"]["results"]   )))
        else: 
            print( "count: 1")       
        return jj
    
    
    else: 
        print( "error: " + str(response.text) )
        return ''
######################################################################################################
# g_fields   = ""
# g_columns  = []
# g_pages    = ""

def odatacProduct( par ): 
#     global g_fields   
#     global g_columns  
#     global g_pages    
#     global g_count    
#     global g_bm    
#     g_fields   = ""
#     g_columns  = []
#     g_pages    = ""
    
    data = WS_CALL( par )
    
#     if type(json_o) == str: 
#         return data
    
    p_id   =  data["d"]["ProductID"]  
    p_pn   =  data["d"]["ProductName"] 
    p_us   =  data["d"]["UnitsInStock"]  
    p_rl   =  data["d"]["ReorderLevel"]  
    d:ReorderLevel
    #print("pages={0:,}, total={0:,}; block_size={0:,}".format(g_pages,g_count, g_bm  ))
    #print("pages={}, total={}; block_size={}".format(g_pages,g_count, g_bm  ))
    print("p_id={0:,}, {3}. UnitsInStock={1:,}; ReorderLevel={2:,}".format(int(p_id),int(p_us),int(p_rl),p_pn  ))

    
    try:
        g_fields = json.loads(g_fields)
    except: 
        return data
    
    #data["d"]["FIELDS"] = ""
    #print(data["d"])
    #return data
    
#     for col in range(len(g_fields["fields"])): 
#         g_columns.append(g_fields["fields"][col]["N"]) 
#     print("number of columns = " + str(len(g_columns)))
    return data
    
def odatacProducts( par ): 
    data =  WS_CALL( par )
    l_i = len(data["d"]["results"]) 
    a_lines = []
           
#     try:
    if  l_i > 0 : 
        #for i in range(2):
        for i in range(l_i):
            #print(data["d"]["results"][i]["TBLOUT_STR"])
            line = data["d"]["results"][i]["ProductID"]#.split('|;|')
            a_lines.append(line) 
            #print(len(line))
            #print(line)
        #print(a_lines)
        #dft = pd.DataFrame(a_lines, columns=g_columns)
        #df.append(dft)
        #df = df.append(dft, ignore_index = True) 
#     except: 
#         print('error happened in dataframe construction')
#         return data

    print(a_lines)
    return a_lines   

def main():
    print("main")
    start_time = time.time()
    # json_o = ''

    # json_o = WS_CALL( params[1] ) 
    a_lines = odatacProducts( params[1] ) 
    # json_o = odatacProduct( params[2] ) 

    # df = pd.DataFrame( columns=g_columns)

    end_time = time.time()
    l_time = end_time-start_time
    print("Execution time: {} seconds".format(l_time))
    print("Execution time: {} minutes".format(l_time/60))

    #print json 
    # print(json_o)
    # SaveJSON(json_o,  "new")

######################################################################################################
######################################################################################################
# $ python test.py arg1 arg2 arg3
if __name__== "__main__" :
    main()
    # print( 'Number of arguments:' + str(len(sys.argv)) + ' arguments.' )
    # print ( 'Argument List:' + str(sys.argv) )