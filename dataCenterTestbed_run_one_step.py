#-*- coding: utf-8 -*-
import paramiko
import os
import time

def ssh(ip,username,passwd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        return ssh
    except :
        print '%s\tError\n'%(ip)


def run_one_step(timeout,run_time=600):
    host1_ip = '192.168.1.185'
    host2_ip = '192.168.1.186'
    username = 'gzq'
    passwd = 'tanklab'


    host1 = ssh(host1_ip,username,passwd)
    host2 = ssh(host2_ip,username,passwd)
    print 'ssh host1 and host2 success'

    print 'run dataCenterTestbed_init.sh'
    os.system('sh dataCenterTestbed_init.sh')

    #启动iperf
    print 'start iperf server'
    host1.exec_command('sh /home/gzq/iperf_stop.sh &')
    host1.exec_command('sh /home/gzq/iperf_server.sh &')
    print 'start iperf server success'

    print 'start iperf client'
    host1.exec_command('sh /home/gzq/iperf_stop.sh &')
    host2.exec_command('sh /home/gzq/iperf_client.sh &')
    print 'start iperf client success'


    #流表查询结果写入日志
    os.system('ps -ef| grep flowEntry_statistics_record2 |grep -v grep|cut -c 9-15|xargs kill -9')
    print 'start flowEntry_statistics_record2.py'
    os.system('flowEntry_statistics_record2.py &')
    print 'start flowEntry_statistics_record2.py success'

    #系统运行run_time
    print 'run system {} seconds'.format(run_time/2)
    time.sleep(run_time/2)

    print 're distribute flow, run system {} seconds'.format(run_time/2)
    os.system('sh flowEntry_del2.sh &')
    os.system('sh flowEntry_setup3.sh &')
	
    time.sleep(run_time/2)

    #关闭iperf
    print 'stop iperf client'
    host2.exec_command('sh /home/gzq/iperf_stop.sh &')
    print 'stop iperf client success'

    print 'stop iperf server'
    host1.exec_command('sh /home/gzq/iperf_stop.sh &')
    print 'stop iperf server success'

    print 'disconnect host1 and host2'
    host1.close()
    host2.close()
    print 'disconnect host1 and host2 success'

    #关闭写日志进程
    print 'stop flowEntry_statistics_record2.py'
    os.system('ps -ef|grep flowEntry_statistics_record2 |grep -v grep|cut -c 9-15|xargs kill -9')
    print 'stop flowEntry_statistics_record2.py success'

    #分析流表日志
    print 'analysis flowEntry_statistics_record.txt start'
    os.system('flowEntry_statistics_analysis2.py')
    print 'analysis flowEntry_statistics_record.txt over'

    os.system('mkdir data30/{}'.format(timeout))
    os.system('mv flowlet_log_s1.txt data30/{}/'.format(timeout))
    os.system('mv flowlet_log_s2.txt data30/{}/'.format(timeout))
    os.system('mv flowEntry_statistics_analysis.txt data30/{}/'.format(timeout))
    os.system('mv simple_flowEntry_statistics_analysis.txt data30/{}/'.format(timeout))

    print 'copy files success'

    print 'success'

if __name__ == '__main__':
    #timeout_values = [9000,15000]
    timeout_values = [2500]
    system_run_time = 60
    for index in range(len(timeout_values)):
        timeout_value = timeout_values[index]
        print 'set timeout to {}'.format(timeout_value)
        timeout_replace = 'sed -i \'1,150s/^uint64_t timeout =.*/uint64_t timeout = {0};/\' /home/tank/br4/openvswitch-2.7.0/ofproto/ofproto-dpif-xlate.c'
        timeout_replace = timeout_replace.format(timeout_value)
        print timeout_replace
        print 'replace timeout in ofproto-dpif-xlate.c'
        os.system(timeout_replace)
        print 'replace timeout in ofproto-dpif-xlate.c success'

        run_one_step(timeout_value,system_run_time)

