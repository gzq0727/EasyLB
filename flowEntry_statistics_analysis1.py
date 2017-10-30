#coding=utf-8
def flow_analysis():
    with open('flowEntry_statistics_record.txt','r') as fa:
        with open('s1_flowEntry_statistics_analysis.txt', 'w') as fr1:
            with open('s2_flowEntry_statistics_analysis.txt', 'w') as fr2:
                lines = fa.readlines()
                time = 1
                start = 0
                end = 0
		ratio_count = 0
		total_ratio = 0.0
 	
		s1_port1_packets = 0
                s1_port1_bytes = 0
                s1_port2_packets = 0
                s1_port2_bytes = 0

                s1_port1_packets_last = 0
                s1_port1_bytes_last = 0
                s1_port2_packets_last = 0
                s1_port2_bytes_last = 0

                s2_port1_packets = 0
                s2_port1_bytes = 0
                s2_port2_packets = 0
                s2_port2_bytes = 0

                s2_port1_packets_last = 0
                s2_port1_bytes_last = 0
                s2_port2_packets_last = 0
                s2_port2_bytes_last = 0

                s1_packet_ratio = 0.0
                s1_byte_ratio = 0.0
                s1_avg_flowlet_size1 = 0.0
                s1_avg_flowlet_size2 = 0.0

                s2_packet_ratio = 0.0
                s2_byte_ratio = 0.0
                s2_avg_flowlet_size1 = 0.0
                s2_avg_flowlet_size2 = 0.0

                for index in range(len(lines)):
                    if lines[index] == '\n':
                        end = index - 1
                        for line in range(start,end):
                            if 'ip,in_port=1,nw_src=172.18.0.1,nw_dst=172.18.0.2 actions=output:2' in lines[line]:
                                splits = lines[line].split(',')
                                s1_port1_packets = int(splits[3].split('=')[-1])
                                s1_port1_bytes = int(splits[4].split('=')[-1])
                            elif 'ip,in_port=2,nw_src=172.18.0.1,nw_dst=172.18.0.2 actions=output:1' in lines[line]:
                                splits = lines[line].split(',')
                                s1_port2_packets = int(splits[3].split('=')[-1])
                                s1_port2_bytes = int(splits[4].split('=')[-1])
                            elif 'ip,in_port=2,nw_src=172.18.0.2,nw_dst=172.18.0.1 actions=output:1' in lines[line]:
                                splits = lines[line].split(',')
                                s2_port1_packets = int(splits[3].split('=')[-1])
                                s2_port1_bytes = int(splits[4].split('=')[-1])
                            elif 'in_port=1,nw_src=172.18.0.2,nw_dst=172.18.0.1 actions=output:2' in lines[line]:
                                splits = lines[line].split(',')
                                s2_port2_packets = int(splits[3].split('=')[-1])
                                s2_port2_bytes = int(splits[4].split('=')[-1])

                        s1_inter_port1_packets = s1_port1_packets - s1_port1_packets_last
                        s1_inter_port1_bytes = s1_port1_bytes - s1_port1_bytes_last
                        s1_inter_port2_packets = s1_port2_packets - s1_port2_packets_last
                        s1_inter_port2_bytes = s1_port2_bytes - s1_port2_bytes_last

                        s2_inter_port1_packets = s2_port1_packets - s2_port1_packets_last
                        s2_inter_port1_bytes = s2_port1_bytes - s2_port1_bytes_last
                        s2_inter_port2_packets = s2_port2_packets - s2_port2_packets_last
                        s2_inter_port2_bytes = s2_port2_bytes - s2_port2_bytes_last

                        analysis = ''
                        if float(s1_inter_port2_packets):
                            s1_packet_ratio = float(s1_inter_port1_packets) / float(s1_inter_port2_packets)
                        else:
                            s1_packet_ratio = 'inf'
                        if  float(s1_inter_port2_bytes):
                            s1_byte_ratio = float(s1_inter_port1_bytes) / float(s1_inter_port2_bytes)
                        else:
                            s1_byte_ratio = 'inf'
                        if float(s1_inter_port1_packets):
                            s1_avg_flowlet_size1 = float(s1_inter_port1_bytes) / float(s1_inter_port1_packets)
                        else:
                            s1_avg_flowlet_size1 = 'inf'
                        if float(s1_inter_port2_packets):
                            s1_avg_flowlet_size2 = float(s1_inter_port2_bytes) / float(s1_inter_port2_packets)
                        else:
                            s1_avg_flowlet_size2 = 'inf'

			
			analysis += str(s1_byte_ratio)+'\n'                        
			'''
			analysis += 'time:' + str(time) + ' '+'p1_packets:' + str(s1_inter_port1_packets) + ' ' + 'p1_bytes:' + str(s1_inter_port1_bytes)\
                                    + ' ' + \
                                'p2_packets:' + str(s1_inter_port2_packets) + ' ' + 'p2_bytes:' + str(s1_inter_port1_bytes) + ' '\
                                'p1_avg_fl_size:' + str(s1_avg_flowlet_size1) + ' ' + 'p2_avg_fl_size:'+ str(s1_avg_flowlet_size2) + ' ' + \
                                'packet_ratio:' + str(s1_packet_ratio) + ' ' + 'byte_ratio:' + str(s1_byte_ratio)+'\n'
			'''

                        fr1.write(analysis)
                        fr1.flush()

                        analysis = ''
                        if float(s2_inter_port2_packets):
                            s2_packet_ratio = float(s2_inter_port1_packets) / float(s2_inter_port2_packets)
                        else:
                            s2_packet_ratio = 'inf'
                        if float(s2_inter_port2_bytes):
                            s2_byte_ratio = float(s2_inter_port1_bytes) / float(s2_inter_port2_bytes)
                        else:
                            s2_byte_ratio = 'inf'
                        if float(s2_inter_port1_packets):
                            s2_avg_flowlet_size1 = float(s2_inter_port1_bytes) / float(s2_inter_port1_packets)
                        else:
                            s2_avg_flowlet_size1 = 'inf'
                        if float(s2_inter_port2_packets):
                            s2_avg_flowlet_size2 = float(s2_inter_port2_bytes) / float(s2_inter_port2_packets)
                        else:
                            s2_avg_flowlet_size2 = 'inf'
			
			analysis += str(s2_byte_ratio)+'\n'

			if s2_byte_ratio != 'inf':
				ratio_count += 1
				total_ratio += s2_byte_ratio
				
			'''
                        analysis += 'time:' + str(time) + ' ' + 'p1_packets:' + str(
                            s2_inter_port1_packets) + ' ' + 'p1_bytes:' + str(s2_inter_port1_bytes) \
                                    + ' ' + \
                                    'p2_packets:' + str(s2_inter_port2_packets) + ' ' + 'p2_bytes:' + str(
                            s2_inter_port2_bytes) + ' ' \
                                                    'p1_avg_fl_size:' + str(
                            s2_avg_flowlet_size1) + ' ' + 'p2_avg_fl_size:' + str(s2_avg_flowlet_size2) + ' ' + \
                                    'packet_ratio:' + str(s2_packet_ratio) + ' ' + 'byte_ratio:' + str(
                            s2_byte_ratio) + '\n'
			'''

                        fr2.write(analysis)
                        fr2.flush()

                        time = time + 1
                        start = end + 2

                        s1_port1_packets_last = s1_port1_packets
                        s1_port1_bytes_last = s1_port1_bytes
                        s1_port2_packets_last = s1_port2_packets
                        s1_port2_bytes_last = s1_port2_bytes

                        s2_port1_packets_last = s2_port1_packets
                        s2_port1_bytes_last = s2_port1_bytes
                        s2_port2_packets_last = s2_port2_packets
                        s2_port2_bytes_last = s2_port2_bytes

	
    with open('ratio_count.txt','a') as final_f:
	final_f.write(str(total_ratio/ratio_count)+'\n')
	final_f.flush()
if __name__ == '__main__':
    flow_analysis()

