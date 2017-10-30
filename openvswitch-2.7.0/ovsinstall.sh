kill `cd /usr/local/var/run/openvswitch && cat ovsdb-server.pid ovs-vswitchd.pid` 
aptitude remove openvswitch-common openvswitch-datapath-dkms openvswitch-controller openvswitch-pki openvswitch-switch -y 

rm -r /usr/etc/openvswitch
rm -r /usr/local/etc/openvswitch
rm -r /usr/local/bin
rm -r /usr/local/include/openvswitch
rm -r /usr/local/share/openvswitch
rm -r /usr/local/var/run/openvswitch

#/sbin/rmmod openvswitch
modprobe -f openvswitch

./boot.sh
./configure --with-linux=/lib/modules/`uname -r`/build 2>/dev/null

make
make install
make modules_install

depmod -a

/sbin/modprobe openvswitch

export PATH=$PATH:/usr/local/share/openvswitch/scripts

mkdir -p /usr/local/etc/openvswitch
ovsdb-tool create /usr/local/etc/openvswitch/conf.db \
    vswitchd/vswitch.ovsschema

mkdir -p /usr/local/var/run/openvswitch
ovsdb-server --remote=punix:/usr/local/var/run/openvswitch/db.sock \
    --remote=db:Open_vSwitch,Open_vSwitch,manager_options \
    --private-key=db:Open_vSwitch,SSL,private_key \
    --certificate=db:Open_vSwitch,SSL,certificate \
    --bootstrap-ca-cert=db:Open_vSwitch,SSL,ca_cert \
    --pidfile --detach --log-file

ovs-vsctl --no-wait init
ovs-vswitchd --pidfile --detach --log-file
