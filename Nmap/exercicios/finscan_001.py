#!/usr/bin/python

import nmap3
from datetime import datetime
from termcolor import colored

msg1 = colored('+', 'blue', attrs=['blink'])
msg2 = colored('+', 'red', attrs=['blink'])

nmap_start = datetime.now()

target = '11.11.11.171'

pynmap = nmap3.NmapScanTechniques()
finscan = pynmap.nmap_fin_scan(target)

print('Porta...:', finscan['ports']['portid'])     
print('Protocolo...:', finscan['ports']['protocol'])     
print('Servico...:', finscan['ports']['name'])     
print('Estado...:', finscan['ports']['state'])     


nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print('[' + msg1 + ']' , 'Tempo de execucao', nmap_time)



