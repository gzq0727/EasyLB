#ensure the ovsdb is connected
/sbin/modprobe openvswitch
export PATH=$PATH:/usr/local/share/openvswitch/scripts
ovsdb-server --remote=punix:/usr/local/var/run/openvswitch/db.sock \
    --remote=db:Open_vSwitch,Open_vSwitch,manager_options \
    --private-key=db:Open_vSwitch,SSL,private_key \
    --certificate=db:Open_vSwitch,SSL,certificate \
    --bootstrap-ca-cert=db:Open_vSwitch,SSL,ca_cert \
    --pidfile --detach --log-file
ovs-vsctl --no-wait init
ovs-vswitchd --pidfile --detach --log-file

#del qos and queue
ovs-vsctl clear port veth12 qos
ovs-vsctl clear port veth12 qos
ovs-vsctl clear port veth21 qos
ovs-vsctl clear port veth22 qos
ovs-vsctl clear port veth31 qos
ovs-vsctl clear port veth32 qos
ovs-vsctl clear port veth41 qos
ovs-vsctl clear port veth42 qos

sleep 10

ovs-vsctl --all destroy qos
ovs-vsctl --all destroy queue

ovs-vsctl del-br s1
ovs-vsctl del-br s2
ovs-vsctl del-br s3
ovs-vsctl del-br s4

ip link del veth11 type veth peer name veth12
ip link del veth21 type veth peer name veth22
ip link del veth31 type veth peer name veth32
ip link del veth41 type veth peer name veth42

ip link del br1_s1_1 type veth peer name br1_s1_2
ip link del br2_s2_1 type veth peer name br2_s2_2

