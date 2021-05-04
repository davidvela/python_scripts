import pandas as pd
import configparser
import sys

exports = "../../../../__exports/"
path = "../../../../__data/"
config_file = "_config.ini"

config = configparser.ConfigParser()
config.read(path + config_file)

fname = 'entries_zalando'
folder = 'JSON/'

# read csv: 
# ds = pd.read_csv(path + 'xx.csv')

# parse JSON to excel
def convert_json_2_xlsx():
    df_json = pd.read_json(path + folder+ fname+'.json')
    df_json.to_excel(path + folder+ fname+'c.xlsx',index=False)
    
# parse excel to json
def convert_xlsx_2_json():
    df_xlsx = pd.read_excel(path + folder+ fname+'.xlsx', index=False,sheet_name=0)
    df_xlsx.to_json(path + folder+ fname+'c.json', orient = "records")
    
# parse to js - object


df_json = pd.read_json(path + folder+ fname+'.json')
# print(df_json.head(5))
print(df_json.info)

# iterate DS: 


def main():
    print("main")
     #test pandas
     #convert_json_2_xlsx()

######################################################################################################
######################################################################################################
# $ python test.py arg1 arg2 arg3
if __name__== "__main__" :
    print( 'Number of arguments:' + str(len(sys.argv)) + ' arguments.' )
    print ( 'Argument List:' + str(sys.argv) )
    i = 0
    if len(sys.argv) > 0:
        for a in sys.argv:
            # 0 = filename
            if i == 1: fname =  a; print(a)
            if i == 2: print("second" + str(a))
            else: print("others:" + str(a))
            i = i+1
    main()
    