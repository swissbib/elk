#!/usr/bin/env bash

for host in sb-uvf21.swissbib.unibas.ch \
            sb-uvf22.swissbib.unibas.ch \
            sb-uvf23.swissbib.unibas.ch \
            sb-uvf25.swissbib.unibas.ch \
            sb-uvf29.swissbib.unibas.ch \
            sb-uvf30.swissbib.unibas.ch \
            sb-uvf31.swissbib.unibas.ch \
            sb-uvf35.swissbib.unibas.ch

do
    echo "stop / disable / enable filebeat on $host"
    #ssh root@${host} "systemctl stop filebeat_swissbib.service; systemctl disable filebeat_swissbib.service"

    ssh root@${host} "systemctl enable filebeat_swissbib.service"

done
