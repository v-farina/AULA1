#!/usr/bin/python

import shodan
shodan_mykey='ZYiFaQVLSm6TNU4cKZI6T0NtxVKG5hFa'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_item = 'Microsoft-ISS/8.0'
shodan_result = shodan_api.search(shodan_item)


def shodan_search():
    print('Buscar por:', shodan_item)
    print('Numero de ocorrencias:', shodan_result['total'])

    print('.....:: TOP 100 ::.....')
    
    count = 1


    for _result in shodan_result['matches']:
        print('[+] - Possivel Alvo',count, 'IP',_result['ip strg'])
        count = count + 1

shodan_search()

