#!/usr/bin/python

import nmap3
from datetime import datetime
from termcolor import colored

msg1 = colored('+', 'blue', attrs=['blink'])
nmap_start = datetime.now()

target = '11.11.11.171'

pynmap = nmap3.NmapScanTechniques()
vanilla = pynmap.nmap_tcp_scan(target)

for _info in vanilla[target]:
    print('[' + msg1 + ']', _info['portid'], _info['protocol'], _info['state'], _info['reason'])

nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print('[' + msg1 + ']' , 'Tempo de execucao', nmap_time)


