import sys
import os

if sys.platform.lower() == "win32":
    os.system('color')
#Formatting
HEADER = lambda x: print('\033[94m' + str(x) + '\033[0m')
PASS = lambda x: print('\033[92m' + str(x) + '\033[0m')
WARNING = lambda x: print('\033[93m' + str(x) + '\033[0m')
FAIL = lambda x: print('\033[91m' + str(x) + '\033[0m')
TESTCASE = lambda x: print('\033[94m' + "\n=================================\n" + str(x) + "\n=================================" + '\033[0m')
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
NORMAL = '\033[0m'

print("hello")
HEADER("hello HEADER blue")
PASS("Hello PASS green")
WARNING("Hello WARNING yellow")
FAIL("Hello FAIL red")
TESTCASE("Hello TESTCASE black")
print(ENDC + "HELLO" + ENDC  )
print(BOLD + "HELLO BOLD" + BOLD  )
print(UNDERLINE + "HELLO UNDERLINE" + UNDERLINE  )
print(NORMAL + "HELLO back to normal" + NORMAL  )
