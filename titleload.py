import csv

ifile = open('template.csv', 'r')
reader = csv.reader(ifile,delimiter='\t')
ofile = open('output.csv', 'w')
writer = csv.writer(ofile, delimiter='\t')




findlist = ['XefzX','XshpX']
replacelist = ['test','secondtest']

s = ifile.read()
for item, replacement in zip(findlist, replacelist):
    s = s.replace(item, replacement)
ofile.write(s)

ifile.close()
ofile.close() 
