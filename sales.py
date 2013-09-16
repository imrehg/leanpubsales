#!/usr/bin/env python2

import urllib2
try: 
    import simplejson as json
except ImportError: 
    import json

# Settings are stored here
import secrets

salesurl = "https://leanpub.com/%s/sales.json?api_key=%s" %(secrets.bookslug, secrets.apikey)

req = urllib2.Request(salesurl)
response = urllib2.urlopen(req)
salesdata = json.loads(response.read())

numsales = int(salesdata['num_happy_paid_purchases'])
nummoney = float(salesdata['total_book_royalties'])

try:
    with open('counts.txt') as countfile: 
        savedcounts = int(countfile.readline())
except IOError:
    savedcounts = 0
except ValueError:
    savedcounts = 0

if numsales != savedcounts:
    with open("counts.txt", "w") as text_file:
        text_file.write("%d" %numsales)
    print "Sales count: %d\nMonies: $%.2f" %(numsales, nummoney)

