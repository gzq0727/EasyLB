#coding=utf-8
import os
import time

if __name__ == '__main__':
    with open('/home/tank/br4/flow_record.txt','w') as fr:
	while(True):
        	result = os.popen('ovs-ofctl -O openflow15 dump-flows s3')
		fr.write('ovs-ofctl -O openflow15 dump-flows s3'+'\n')
        	res = result.read()
        	for line in res.splitlines():
            		fr.write(line+'\n')

        	result = os.popen('ovs-ofctl -O openflow15 dump-flows s4')
		fr.write('ovs-ofctl -O openflow15 dump-flows s4'+'\n')
        	res = result.read()
        	for line in res.splitlines():
            		fr.write(line+'\n')
        	result = os.popen('ovs-ofctl -O openflow15 dump-flows s5')
		fr.write('ovs-ofctl -O openflow15 dump-flows s5'+'\n')
        	res = result.read()
        	for line in res.splitlines():
            		fr.write(line+'\n')
		fr.write('\n')
        	fr.flush()
        	time.sleep(0.6)
