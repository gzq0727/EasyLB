sh testbedTopology_del.sh
echo "topo deleted!"

cd openvswitch-2.7.0
sh ovsinstall.sh

echo "ovs installed!"

cd ..
rm flowlet_log_s1.txt
rm flowlet_log_s2.txt

touch flowlet_log_s1.txt
touch flowlet_log_s2.txt

echo "file inited!"

sh testbedTopology_setup.sh

echo "topo setup!"

sh flowEntry_setup1.sh

echo "add flow!"

echo "testbed init ok!"
