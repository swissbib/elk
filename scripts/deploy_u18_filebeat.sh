#!/usr/bin/env bash

BASE_FILEBEAT_SWISSBIB_DIR=/etc/filebeat/swissbib



for host in sb-uvf21 sb-uvf23 sb-uvf23
do
    echo "copy /filebeat/presentation/green/filebeat.yml to $host"
    scp ../filebeat/presentation/green/filebeat.yml root@${host}:${BASE_FILEBEAT_SWISSBIB_DIR}

    #erst restart wenn wirklich alles vorbereitet ist
    #ssh root@${host} "systemctl restart filebeat_swissbib.service"
done

for host in sb-uvf25
do
    echo "copy /filebeat/presentation/jus/filebeat.yml to $host"
    scp ../filebeat/presentation/jus/filebeat.yml root@${host}:${BASE_FILEBEAT_SWISSBIB_DIR}

    #erst restart wenn wirklich alles vorbereitet ist
    #ssh root@${host} "systemctl restart filebeat_swissbib.service"
done

for host in sb-uvf29 sb-uvf30 sb-uvf31
do
    echo "copy /filebeat/presentation/bb/filebeat.yml to $host"
    scp ../filebeat/presentation/bb/filebeat.yml root@${host}:${BASE_FILEBEAT_SWISSBIB_DIR}

    #erst restart wenn wirklich alles vorbereitet ist
    #ssh root@${host} "systemctl restart filebeat_swissbib.service"
done

for host in sb-uvf35
do
    echo "copy /filebeat/sru/filebeat.yml to $host"
    scp ../filebeat/sru/filebeat.yml root@${host}:${BASE_FILEBEAT_SWISSBIB_DIR}

    #erst restart wenn wirklich alles vorbereitet ist
    #ssh root@${host} "systemctl restart filebeat_swissbib.service"
done


