ovs-vsctl add-br s1
ovs-vsctl add-br s2
ovs-vsctl add-br s3
ovs-vsctl add-br s4
ovs-vsctl add-br s5
ovs-vsctl set bridge s1 protocol=OpenFlow15
ovs-vsctl set bridge s2 protocol=OpenFlow15
ovs-vsctl set bridge s3 protocol=OpenFlow15
ovs-vsctl set bridge s4 protocol=OpenFlow15
ovs-vsctl set bridge s5 protocol=OpenFlow15


ip link add veth11 type veth peer name veth12
ip link add veth21 type veth peer name veth22
ip link add veth31 type veth peer name veth32
ip link add veth41 type veth peer name veth42
ip link add veth51 type veth peer name veth52
ip link add veth61 type veth peer name veth62

ovs-vsctl add-port s1 veth11
ovs-vsctl add-port s3 veth12

ovs-vsctl add-port s2 veth21
ovs-vsctl add-port s4 veth22

ovs-vsctl add-port s2 veth31
ovs-vsctl add-port s3 veth32

ovs-vsctl add-port s1 veth41
ovs-vsctl add-port s4 veth42

ovs-vsctl add-port s1 veth51
ovs-vsctl add-port s5 veth52

ovs-vsctl add-port s2 veth61
ovs-vsctl add-port s5 veth62
#add linux bridge connecting host and ovs switch
brctl addbr br1
brctl addbr br2

#add one link between br1 and s1
ip  link add br1_s1_1 type veth peer name br1_s1_2
brctl addif br1 br1_s1_1
ovs-vsctl add-port s1 br1_s1_2

#add one link between br2 and s2
ip link add br2_s2_1 type veth peer name br2_s2_2
brctl addif br2 br2_s2_1
ovs-vsctl add-port s2 br2_s2_2

#change virtual network device states to up
ifconfig veth11 up
ifconfig veth12 up
ifconfig veth21 up
ifconfig veth22 up
ifconfig veth31 up
ifconfig veth32 up
ifconfig veth41 up
ifconfig veth42 up
ifconfig veth51 up
ifconfig veth52 up
ifconfig veth61 up
ifconfig veth62 up
ifconfig br1 up
ifconfig br2 up
ifconfig br1_s1_1 up
ifconfig br1_s1_2 up
ifconfig br2_s2_1 up
ifconfig br2_s2_2 up

#set link speed
#link s1<---->s3<----->s2
ovs-vsctl set port veth11 qos=@newqos1 --  \
--id=@newqos1 create qos type=linux-htb queues=0=@q0 -- \
--id=@q0 create queue other-config:max-rate=60000000

ovs-vsctl set port veth12 qos=@newqos2 --  \
--id=@newqos2 create qos type=linux-htb queues=0=@q0 -- \
--id=@q0 create queue other-config:max-rate=60000000

ovs-vsctl set port veth31 qos=@newqos3 --  \
--id=@newqos3 create qos type=linux-htb queues=0=@q0 -- \
--id=@q0 create queue other-config:max-rate=60000000

ovs-vsctl set port veth32 qos=@newqos4 --  \
--id=@newqos4 create qos type=linux-htb queues=0=@q0 -- \
--id=@q0 create queue other-config:max-rate=60000000


#link s1<---->s5<------>s2
ovs-vsctl set port veth51 qos=@newqos5 --  \
--id=@newqos5 create qos type=linux-htb queues=0=@q0 -- \
--id=@q0 create queue other-config:max-rate=180000000

ovs-vsctl set port veth52 qos=@newqos6 --  \
--id=@newqos6 create qos type=linux-htb queues=0=@q0 -- \
--id=@q0 create queue other-config:max-rate=180000000

ovs-vsctl set port veth61 qos=@newqos7 --  \
--id=@newqos7 create qos type=linux-htb queues=0=@q0 -- \
--id=@q0 create queue other-config:max-rate=180000000

ovs-vsctl set port veth62 qos=@newqos8 --  \
--id=@newqos8 create qos type=linux-htb queues=0=@q0 -- \
--id=@q0 create queue other-config:max-rate=180000000

#link s1<----->s4<------->s2
ovs-vsctl set port veth41 qos=@newqos9 --  \
--id=@newqos9 create qos type=linux-htb queues=0=@q0 --  \
--id=@q0 create queue other-config:max-rate=60000000

ovs-vsctl set port veth42 qos=@newqos10 --  \
--id=@newqos10 create qos type=linux-htb queues=0=@q0 --  \
--id=@q0 create queue other-config:max-rate=60000000

ovs-vsctl set port veth21 qos=@newqos11 --  \
--id=@newqos11 create qos type=linux-htb queues=0=@q0 --  \
--id=@q0 create queue other-config:max-rate=60000000

ovs-vsctl set port veth22 qos=@newqos12 --  \
--id=@newqos12 create qos type=linux-htb queues=0=@q0 -- \
--id=@q0 create queue other-config:max-rate=60000000

