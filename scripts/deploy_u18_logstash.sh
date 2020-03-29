#!/usr/bin/env bash

BASE_LOGSTASH_CONFDIR=/etc/logstash/
LOGSTASH_QUEUE=/swissbib_index/logstash/queue


#create data and log dirs
for host in sb-uelk1

do

    #hinweis geoip directory 1:1 per Hand von server to server kopiert

    echo "deploy all logstash configurations to $host"
    scp -r ../logstash/configuration/* root@${host}:${BASE_LOGSTASH_CONFDIR}

    #check logstash queue directory
    ssh root@${host} "[ ! -d ${LOGSTASH_QUEUE} ] &&   echo \"create ${LOGSTASH_QUEUE}\" && mkdir -p ${LOGSTASH_QUEUE} && chown -R logstash:logstash ${LOGSTASH_QUEUE}"

    #wenn alles vorbereitet
    ssh root@${host} "systemctl restart logstash.service"

done


