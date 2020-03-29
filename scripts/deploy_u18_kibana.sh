#!/usr/bin/env bash

BASE_KIBANA_DIR=/etc/kibana


#create data and log dirs
#sollte nach sb-uelk1 da dort nur logstash -> Paul sagen
#for host in sb-uelk1
for host in sb-uelk2 sb-uelk3 sb-uelk4

do

    echo "deploy specific kibana.yml"
    scp ../kibana/configs/$host/kibana.yml root@${host}:${BASE_KIBANA_DIR}
    #ssh root@${host} "ufw allow 5601"
    ssh root@${host} "systemctl restart kibana.service"

done


