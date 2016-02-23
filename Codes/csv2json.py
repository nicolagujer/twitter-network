import csv
import json
import numpy as np
from io import BytesIO
import os.path

binf = open('twitterFinal.csv', 'rU')
c = binf.read().decode('utf-8').encode('utf-8')
#jsonfile = open('twitter.json', 'w')
jsonfile = open(os.path.abspath("../HTML/twitter-network/twitter.json"),'w')
print >>jsonfile, 'graph("#graph", '
print >>jsonfile, '{'

print >>jsonfile, '"synapses": ['


csvfile = np.genfromtxt('FinalTwitterMatrix.csv', delimiter=',', dtype='int')


[i,j] = np.where(csvfile)
for k in range(len(i)):
    print >>jsonfile, '{"source":'+str(j[k])+', "target":'+str(i[k])+', "to":'+str(j[k])+', "from":'+str(i[k])+', "weight":2, "type":"S"},'  

print >>jsonfile, ']'
print >>jsonfile, ', "neurons": ['

for line in csv.DictReader(BytesIO(c)):
    json.dump(line, jsonfile, encoding='utf-8', ensure_ascii=False, indent=0, sort_keys = True)
    jsonfile.write('\n,')

print >>jsonfile, ']'
print >>jsonfile, '}, true)'
jsonfile.close()