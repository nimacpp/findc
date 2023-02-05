#! /etc/lib/python3
import os
import sys
import requests
v = "1.0.0"
a = os.environ['PATH'].split(';')
listapp = []
for i in a:
    try:
        for j in os.listdir(i):
            listapp.append(j)
    except:
        pass
        #print("list is emty")
#print(listapp)
try:
    tr = sys.argv[1].lower()
except:
    print("error: no operation specified (use -h for help)")
    exit()
if tr == "-h":
    print('''usage: findc <operation> [...]
operations:
    findc {-h help}
    findc {-v version}
    findc {-u check update}
use 'findc {-h --help}' with an operation for available options
''')
elif tr == "-v":
    print(f'''
███████╗██╗███╗   ██╗██████╗  ██████╗   - findc - {v} 
██╔════╝██║████╗  ██║██╔══██╗██╔════╝   - python - {'.'.join(str(e) for e in sys.version_info[0:3])}
█████╗  ██║██╔██╗ ██║██║  ██║██║        - github.com/nimacpp/findc.git
██╔══╝  ██║██║╚██╗██║██║  ██║██║        - t.me/nimacpp
██║     ██║██║ ╚████║██████╔╝╚██████╗
╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝
''')
elif tr == "-u":
    req = requests.get("https://raw.githubusercontent.com/nimacpp/findc/main/.version")
    if req.text != v+"\n":
        print("your app need update")
    else:
        print("you use least version")
else:
    for k in listapp:
        if tr in k.lower():
            if k.endswith('.exe') == True:
                print(f"do you mean : {k}")
            else:
                pass
