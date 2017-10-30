#coding=utf-8

def flowlet_analysis():
    with open('flowlet_log.txt','r') as fl:
        with open('s1_flowlet_analysis.txt', 'w') as fr1:
            with open('s2_flowlet_analysis.txt', 'w') as fr2:
                #flowlet trigger times
                flowlet_number = {}
                flowlet_number['s1'] = 0
                flowlet_number['s2'] = 0

                #flowlet trigger times for every flow
                flow_flowlet_number = {}
                flow_flowlet_number['s1'] = {}
                flow_flowlet_number['s2'] = {}

                #the number of flows in each paths
                s1_to_s2_flows_in_path = {}
                s1_to_s2_flows_in_path['p1'] = set()
                s1_to_s2_flows_in_path['p2'] = set()
                s2_to_s1_flows_in_path = {}
                s2_to_s1_flows_in_path['p1'] = set()
                s2_to_s1_flows_in_path['p2'] = set()


                s1_packet_number = 0
                s2_packet_number = 0
                total_flowlet_number = 0
                start = 0
                end = 0
                lines = fl.readlines()
		time = 0
                for index in range(len(lines)):
		    if time > 20000:
			break
                    if lines[index] == '\n':
			time += 1
                        end = index - 1
                        datapath = ''
                        for line in range(start,end+1):
                            if 'datapath:s1' in lines[line]:
                                datapath = 's1'
                                s1_packet_number += 1
                            elif 'datapath:s2' in lines[line]:
                                datapath = 's2'
                                s2_packet_number += 1
                            if 'hash code' in lines[line]:
				if datapath == '':
					start = end + 2
					break
                                hashcode = int(lines[line].split(':')[-1].strip(' '))
				print line
                                if hashcode not in flow_flowlet_number[datapath].keys():
                                    flow_flowlet_number[datapath][hashcode] = 0
                            if 'timeout! trigger a new flowlet' in lines[line]:
				if datapath == '':
					start = end +2
					break
                                if hashcode not in flow_flowlet_number[datapath].keys():
					start = end +2
					break		
                                flow_flowlet_number[datapath][hashcode] = flow_flowlet_number[datapath][hashcode] + 1
                                flowlet_number[datapath] = flowlet_number[datapath] + 1
                            if 'output port:' in lines[line]:
                                output_port = int(lines[line].split(':')[-1].strip(' ').strip('\n'))
                                if output_port == 1:
                                    if datapath == 's1':
                                        s1_to_s2_flows_in_path['p1'].add(hashcode)
                                        if hashcode in s1_to_s2_flows_in_path['p2']:
                                            s1_to_s2_flows_in_path['p2'].remove(hashcode)
                                    elif datapath == 's2':
                                        s2_to_s1_flows_in_path['p2'].add(hashcode)
                                        if hashcode in s2_to_s1_flows_in_path['p1']:
                                            s2_to_s1_flows_in_path['p1'].remove(hashcode)
                                elif output_port == 2:
                                    if datapath == 's1':
                                        s1_to_s2_flows_in_path['p2'].add(hashcode)
                                        if hashcode in s1_to_s2_flows_in_path['p1']:
                                            s1_to_s2_flows_in_path['p1'].remove(hashcode)
                                    elif datapath == 's2':
                                        s2_to_s1_flows_in_path['p1'].add(hashcode)
                                        if hashcode in s2_to_s1_flows_in_path['p2']:
                                            s2_to_s1_flows_in_path['p2'].remove(hashcode)

                        #function one
                        total_flowlet_number = flowlet_number['s1'] + flowlet_number['s2']

                        #function three
                        if len(s1_to_s2_flows_in_path['p2']) != 0:
                            s1_to_s2_flow_num_ratio = float(len(s1_to_s2_flows_in_path['p1'])) / float(len(s1_to_s2_flows_in_path['p2']))
                        else:
                            s1_to_s2_flow_num_ratio = 'inf'

                        if len(s2_to_s1_flows_in_path['p2']) != 0:
                            s2_to_s1_flow_num_ratio = float(len(s2_to_s1_flows_in_path['p1'])) / float(len(s2_to_s1_flows_in_path['p2']))
                        else:
                            s2_to_s1_flow_num_ratio = 'inf'

                        #function two
                        pass
			
			'''	
                        fr1.write('pk_num:'+str(s1_packet_number)+' fl_num:'+str(flowlet_number['s1'])+' total_fl_num:'\
                        +str(total_flowlet_number)+' fw_num_p1:'+str(len(s1_to_s2_flows_in_path['p1']))+' fw_num_p2:'+str(len(s1_to_s2_flows_in_path['p2']))
                        +' fw_ratio:'+str(s1_to_s2_flow_num_ratio )+'\n')
			'''
			
			fr1.write(str(s1_to_s2_flow_num_ratio)+'\n')
			fr1.flush()
			
			'''
                        fr2.write('pk_num:' + str(s2_packet_number) + ' fl_num:' + str(
                            flowlet_number['s2']) + ' total_fl_num:' \
                                  + str(total_flowlet_number) + ' fw_num_p1:' + str(
                            len(s2_to_s1_flows_in_path['p1'])) + ' fw_num_p2:' + str(len(s2_to_s1_flows_in_path['p2']))
                                  + ' fw_ratio:' + str(s2_to_s1_flow_num_ratio) + '\n')
			'''
			
			fr2.write(str(s2_to_s1_flow_num_ratio)+'\n')
			fr2.flush()
                        start = end + 2
		fl.close()
		fr1.close()
		fr2.close()

if __name__ == '__main__':
    flowlet_analysis()
