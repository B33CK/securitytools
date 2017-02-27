#coding: utf-8

print("""


██████╗ ██████╗ ██████╗  ██████╗██╗  ██╗
██╔══██╗╚════██╗╚════██╗██╔════╝██║ ██╔╝
██████╔╝ █████╔╝ █████╔╝██║     █████╔╝ 
██╔══██╗ ╚═══██╗ ╚═══██╗██║     ██╔═██╗ 
██████╔╝██████╔╝██████╔╝╚██████╗██║  ██╗
╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
                                        
PortScan (TCP) 

[*] Coder: B33CK
[*] 1 TOOL
""")

import socket,sys

start = int(raw_input('[*] DIGITE [1] PARA PROSSEGUIR COM O SCAN, DIGITE [2] PARA SAIR DO PORTSCAN: '))

while start > 2:
    start = int(raw_input('[*] DIGITE [1] PARA PROSSEGUIR COM O SCAN, DIGITE [2] PARA SAIR DO PORTSCAN: '))

if start == 1:
        target = raw_input('[*] TARGET ADDRESS: ')
        rangemin = raw_input('[*] RANGE MIN: ')
        rangemax = raw_input('[*] RANGE MAX: ')
        if int(rangemax) > 65535:
            rangemax = 65535
        timeout = float(raw_input('[*] TIMEOUT SCAN: '))
        targethost = socket.gethostbyname(target)
        print '[*] STARTING SCAN ON HOST: %s\n' %targethost
        for i in range(int(rangemin), int(rangemax)):
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(float(timeout))
            code = client.connect_ex((targethost, i))
            if code == 0:
                print '\n[*] OPEN => %d\n' %(i,)

if start == 2:
    sys.exit()


    