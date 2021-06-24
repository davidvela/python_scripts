from datetime import date

def examples():
    d0 = date(2014, 1, 1)
    d1 = date(2020, 8, 25)
    delta = d1 - d0 
    print(delta.days + 1)
    
def calculate_days(idate):
    #print(date)
    # print( "{} - {} - {} ".format(idate[0:4], idate[4:6], idate[6:8])  ) 
    
    f_date = date(2014, 1, 1)
    l_date1 = date(int(idate[0:4]), int(idate[4:6]), int(idate[6:8]))
    delta = l_date1 - f_date
    print(idate + " = " + str(delta.days + 1))

def print_timestamp():
    timestamp = 1613520000
    date_time = date.fromtimestamp(timestamp)
    # print("Date time object:", date_time.strftime("%d/%m/%Y"))
    # print(date_time)
    # print(date_time.strftime("%d/%m/%Y"))
    print(date_time.strftime("%Y%m%d"))


def main():
    print("Hello, World!")
    calculate_days("20140102")
    calculate_days("20200101")
    calculate_days("20210101")
    calculate_days("20210224")
    calculate_days(date.today().strftime('%Y%m%d'))



if __name__== "__main__" :
    main()