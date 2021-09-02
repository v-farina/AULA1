#!/usr/bin/python

import dns.resolver
myquery = dns.resolver.Resolver()
target = "megacorpone.com"

def func_ns(_target):
    question = myquery.query(_target, 'NS')

    for _ns in question:
        print(_ns)


def func_mx(_target):
    question = myquery.query(_target, 'MX')

    for _mx in question:
        print(_mx)


def func_txt(_target):
    question = myquery.query(_target, 'TXT')

    for _txt in question:
        print(_txt)



print("#" * 60)
print("Consultas classica de DNS - NS, MX, TXT")

def func_dnsenum(target):
    print("Lista de servidores DNS do dominio")
    func_ns(target)
    print()
    print("Lista de servidores MX")
    func_mx(target)
    print()
    print("Informacoes do registro TXT do dominio")
    print()
    func_txt(target)


func_dnsenum(target)

