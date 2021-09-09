#!/usr/bin/python

import dns.resolver
myquery = dns.resolver.Resolver()
domain = "megacorpone.com"
host = "www"
target = host + "." + domain


def func_a(_target):
    question = myquery.query(_target, 'A')

    for _a in question:
        print(_a)

func_a(target)

