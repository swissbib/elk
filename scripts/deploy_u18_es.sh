#!/usr/bin/env bash

BASE_ES_DIR=/swissbib_index/es
DATA_DIR=$BASE_ES_DIR/data
LOG_DIR=$BASE_ES_DIR/logs
INIT_D=/etc/init.d/
ES_CONFIG_DIR=/etc/elasticsearch


#create data and log dirs
for host in sb-uelk2 sb-uelk3 sb-uelk4

do

    ssh root@${host} "[ ! -d ${DATA_DIR} ] &&   echo \"create ${DATA_DIR}\" && mkdir -p ${DATA_DIR} && chown -R elasticsearch:elasticsearch ${BASE_ES_DIR} "
    ssh root@${host} "[ ! -d ${LOG_DIR} ] &&   echo \"create ${LOG_DIR}\" && mkdir -p ${LOG_DIR} && chown -R elasticsearch:elasticsearch ${BASE_ES_DIR} "

    scp ../elasticsearch/init.d/elasticsearch root@${host}:${INIT_D}

    scp ../elasticsearch/config/$host/elasticsearch.yml root@${host}:${ES_CONFIG_DIR}

    ssh root@${host} "systemctl restart elasticsearch.service"

done


