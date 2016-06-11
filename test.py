import os
import pprint

os.system("vnstat -d --dumpdb -i eth0 > /tmp/data.txt")

file = open('data.txt','r')

day = []
month = []
top = []

for line in file:
	explode = line.split('\n')[0]
	vstatdata = explode.strip().split(';')

	if(vstatdata[0] == 'd'):
		template = {}

		template['time'] = vstatdata[2]
		template['rx'] = int(vstatdata[3]) * 1024 + int(vstatdata[5])
		template['tx'] = int(vstatdata[4]) * 1024 + int(vstatdata[6])
		template['act'] = vstatdata[7]

		day.append(template)

	elif(vstatdata[0] == 'm'):
		 template = {}

		 template['time'] = vstatdata[2]
		 template['rx'] = int(vstatdata[3]) * 1024 + int(vstatdata[5])
		 template['tx'] = int(vstatdata[4]) * 1024 + int(vstatdata[6])
		 template['act'] = vstatdata[7]

		 month.append(template)

	elif(vstatdata[0] == 't'):
		 template = {}

		 template['time'] = vstatdata[2]
		 template['rx'] = int(vstatdata[3]) * 1024 + int(vstatdata[5])
		 template['tx'] = int(vstatdata[4]) * 1024 + int(vstatdata[6])
		 template['act'] = vstatdata[7]

		 top.append(template)

print "\nmonth:\n"
pprint.pprint(month)

print "\ndays:\n"
pprint.pprint(day)

print "\ntop:\n"
pprint.pprint(top)

os.remove('/tmp/data.txt')


