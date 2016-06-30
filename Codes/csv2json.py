"""
@author: Nicola Gujer

This script will put the stats and information from TwitterStats and the adjacency matrix from TwitterFriendship into a json file, with which you can make a visualiation.
"""

import csv
import json
import numpy as np
from io import BytesIO
import os.path

#Opens file will extracted information about Twitter users
binf = open('TwitterDetails.csv', 'rU')
c = binf.read().decode('utf-8').encode('utf-8')

#Creates the json file that will hold all of your information about the Twitter users and the friendship links.
jsonfile = open(os.path.abspath("twitter.json"),'w')

#Creates format the visualisation needs.
print >>jsonfile, 'graph("#graph", '
print >>jsonfile, '{'

#Creates the links.
print >>jsonfile, '"synapses": ['

#Opens the adjacency matrix that shows who follows who.
csvfile = np.genfromtxt('TwitterFriendship.csv', delimiter=',', dtype='int')

[i,j] = np.where(csvfile)
for k in range(len(i)):
    print >>jsonfile, '{"source":'+str(j[k])+', "target":'+str(i[k])+', "to":'+str(j[k])+', "from":'+str(i[k])+', "weight":2, "type":"S"},'  
print >>jsonfile, ']'

#Creates the nodes.
print >>jsonfile, ', "neurons": ['

for line in csv.DictReader(BytesIO(c)):
    json.dump(line, jsonfile, encoding='utf-8', ensure_ascii=False, indent=0, sort_keys = True)
    jsonfile.write('\n,')

print >>jsonfile, ']'
print >>jsonfile, '}, true)'
jsonfile.close()