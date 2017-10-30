ovs-ofctl -O openflow15 add-group s1 group_id=1,type=select,selection_method=hash,bucket=output:2,bucket=output:3
ovs-ofctl -O openflow15 add-group s2 group_id=1,type=select,selection_method=hash,bucket=output:1,bucket=output:3

#for arp h1--->h2
ovs-ofctl -O openflow15 add-flow s1 in_port=4,dl_type=0x0806,priority=10,idle_timeout=0,hard_timeout=0,actions=output:1
ovs-ofctl -O openflow15 add-flow s3 in_port=1,dl_type=0x0806,priority=10,idle_timeout=0,hard_timeout=0,actions=output:2
ovs-ofctl -O openflow15 add-flow s2 in_port=2,dl_type=0x0806,priority=10,idle_timeout=0,hard_timeout=0,actions=output:4
#for arp h2--->h1
ovs-ofctl -O openflow15 add-flow s2 in_port=4,dl_type=0x0806,priority=10,idle_timeout=0,hard_timeout=0,actions=output:1
ovs-ofctl -O openflow15 add-flow s4 in_port=1,dl_type=0x0806,priority=10,idle_timeout=0,hard_timeout=0,actions=output:2
ovs-ofctl -O openflow15 add-flow s1 in_port=2,dl_type=0x0806,priority=10,idle_timeout=0,hard_timeout=0,actions=output:4

#for tcp h1--->h2
ovs-ofctl -O openflow15 add-flow s1 in_port=4,dl_type=0x0800,nw_src=172.18.0.1,nw_dst=172.18.0.2,priority=10,idle_timeout=0,hard_timeout=0,actions=group:1,set_queue:0
ovs-ofctl -O openflow15 add-flow s4 in_port=2,dl_type=0x0800,nw_src=172.18.0.1,nw_dst=172.18.0.2,priority=10,idle_timeout=0,hard_timeout=0,actions=output:1,set_queue:0
ovs-ofctl -O openflow15 add-flow s5 in_port=1,dl_type=0x0800,nw_src=172.18.0.1,nw_dst=172.18.0.2,priority=10,idle_timeout=0,hard_timeout=0,actions=output:2,set_queue:0
ovs-ofctl -O openflow15 add-flow s2 in_port=1,dl_type=0x0800,nw_src=172.18.0.1,nw_dst=172.18.0.2,priority=10,idle_timeout=0,hard_timeout=0,actions=output:4
ovs-ofctl -O openflow15 add-flow s2 in_port=3,dl_type=0x0800,nw_src=172.18.0.1,nw_dst=172.18.0.2,priority=10,idle_timeout=0,hard_timeout=0,actions=output:4

#for tcp h2--->h1
ovs-ofctl -O openflow15 add-flow s2 in_port=4,dl_type=0x0800,nw_src=172.18.0.2,nw_dst=172.18.0.1,priority=10,idle_timeout=0,hard_timeout=0,actions=group:1,set_queue:0
ovs-ofctl -O openflow15 add-flow s3 cookie=3,in_port=2,dl_type=0x0800,nw_src=172.18.0.2,nw_dst=172.18.0.1,priority=10,idle_timeout=0,hard_timeout=0,actions=output:1,set_queue:0
ovs-ofctl -O openflow15 add-flow s4 cookie=4,in_port=1,dl_type=0x0800,nw_src=172.18.0.2,nw_dst=172.18.0.1,priority=10,idle_timeout=0,hard_timeout=0,actions=output:2,set_queue:0
ovs-ofctl -O openflow15 add-flow s5 cookie=5,in_port=2,dl_type=0x0800,nw_src=172.18.0.2,nw_dst=172.18.0.1,priority=10,idle_timeout=0,hard_timeout=0,actions=output:1,set_queue:0
ovs-ofctl -O openflow15 add-flow s1 in_port=2,dl_type=0x0800,nw_src=172.18.0.2,nw_dst=172.18.0.1,priority=10,idle_timeout=0,hard_timeout=0,actions=output:4
ovs-ofctl -O openflow15 add-flow s1 in_port=3,dl_type=0x0800,nw_src=172.18.0.2,nw_dst=172.18.0.1,priority=10,idle_timeout=0,hard_timeout=0,actions=output:4

#drop other packets
ovs-ofctl -O openflow15 add-flow s1 in_port=4,priority=9,idle_timeout=0,hard_timeout=0,actions=drop
ovs-ofctl -O openflow15 add-flow s2 in_port=4,priority=9,idle_timeout=0,hard_timeout=0,actions=drop
