sh ovs_start.sh
sh dataCenterTopology_del.sh
echo "topo deleted!"

cd openvswitch-2.7.0
sh openvswitch-2.7.0/ovsinstall.sh

echo "ovs installed!"

cd ..
rm flowlet_log_s1.txt
rm flowlet_log_s2.txt

touch flowlet_log_s1.txt
touch flowlet_log_s2.txt


echo "file inited!"

sh dataCenterTopology_setup.sh

echo "topo setup!"

sh flowEntry_setup2.sh

echo "add flow!"

echo "data center testbed init ok!"
