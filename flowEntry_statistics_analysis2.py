#coding=utf-8
def flow_analysis():
    with open('flowEntry_statistics_record.txt','r') as fa:
        with open('flowEntry_statistics_analysis.txt', 'w') as fr1:
            with open('simple_flowEntry_statistics_analysis.txt', 'w') as fr2:
                lines = fa.readlines()
                time = 1
                start = 0
                end = 0

                p1_bytes = 0
                p1_packets = 0
                p1_bytes_last = 0
                p1_packets_last = 0

                p2_bytes = 0
                p2_packets = 0
                p2_bytes_last = 0
                p2_packets_last = 0

                p3_bytes = 0
                p3_packets = 0
                p3_bytes_last = 0
                p3_packets_last = 0

                packet_ratio = 0.0
                byte_ratio = 0.0

                p1_avg_flowlet_size = 0.0
                p2_avg_flowlet_size = 0.0
                p3_avg_flowlet_size = 0.0

                for index in range(len(lines)):
                    if lines[index] == '\n':
                        end = index -1
                        for line in range(start,end+1):
                            if 'cookie=0x3' in lines[line]:
                                splits = lines[line].split(',')
                                p1_packets = int(splits[3].split('=')[-1])
                                p1_bytes = int(splits[4].split('=')[-1])
                            elif 'cookie=0x5' in lines[line]:
                                splits = lines[line].split(',')
                                p3_packets = int(splits[3].split('=')[-1])
                                p3_bytes = int(splits[4].split('=')[-1])
                            elif 'cookie=0x4' in lines[line]:
                                splits = lines[line].split(',')
                                p2_packets = int(splits[3].split('=')[-1])
                                p2_bytes = int(splits[4].split('=')[-1])

                        p1_inter_packets = p1_packets - p1_packets_last
                        p1_inter_bytes = p1_bytes - p1_bytes_last
                        p2_inter_packets = p2_packets - p2_packets_last
                        p2_inter_bytes = p2_bytes - p2_bytes_last
                        p3_inter_packets = p3_packets - p3_packets_last
                        p3_inter_bytes = p3_bytes - p3_bytes_last

                        analysis = ''
                        if float(p1_inter_packets+p3_inter_packets):
                            packet_ratio = float(p2_inter_packets) / float(p1_inter_packets + p2_inter_packets + p3_inter_packets)
                        else:
                            packet_ratio = 'inf'
                        if  float(p1_inter_bytes + p3_inter_bytes):
                            byte_ratio = float(p2_inter_bytes) / float(p1_inter_bytes + p2_inter_bytes + p3_inter_bytes)
                        else:
                            byte_ratio = 'inf'

                        analysis += 'time:' + str(time) + ' '+'p1_packets:' + str(p1_inter_packets) + ' ' + 'p1_bytes:' + str(p1_inter_bytes)\
                                    + ' ' + \
                                'p2_packets:' + str(p2_inter_packets) + ' ' + 'p2_bytes:' + str(p2_inter_bytes) + ' '+\
                                'p3_packets:'+str(p3_inter_packets)+' '+'p3_bytes:'+str(p3_inter_bytes)+' '+\
                                'packet_ratio:' + str(packet_ratio) + ' ' + 'byte_ratio:' + str(byte_ratio)+'\n'

                        fr1.write(analysis)
                        fr1.flush()

                        analysis = ''
                        analysis += str(byte_ratio*100) + '\n'

                        fr2.write(analysis)
                        fr2.flush()


                        p1_packets_last = p1_packets
                        p1_bytes_last = p1_bytes
                        p2_packets_last = p2_packets
                        p2_bytes_last = p2_bytes
                        p3_packets_last = p3_packets
                        p3_bytes_last = p3_bytes

                        time = time + 1
                        start = end + 2




if __name__ == '__main__':
    flow_analysis()
