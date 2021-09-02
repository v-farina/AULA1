#!/usr/bin/python

import dns.query
import dns.zone
import dns.resolver

myquery = dns.resolver.Resolver()

domain = 'megacorpone.com'
mytimeout = 15.0


def dns_tf(_target,_domain):
    try:
        transfzone = dns.zone.from_xfr(dns.query.xfr(_target, _domain))

        for _machines in transfzone:
            print('[+] -', str(_machines) + '.' + domain)

    except:
        print('[!] - Falha na transferencia de zona de dominio:', _domain, 'NS: ', _target)

def dns_ns(_domain):
    queryns = myquery.query(_domain, 'NS')

    for _hostns in queryns:
        print('Servidor DNS alvo:', _hostns)
        dns_tf(str(_hostns),_domain)

dns_ns(domain)


