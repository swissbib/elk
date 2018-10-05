# Elastic Kibana Logstash (ELK) Stack Configs

This repository contains all the configuration files for the ELK stack and file beat, 
which is used to process, store and analyze metrics from all
swissbib websites.


## FileBeat

To start FileBeat:

```
/usr/share/filebeat/bin/filebeat -c /etc/filebeat/filebeat.yml -path.home /usr/share/filebeat -path.config /etc/filebeat -path.data /var/lib/filebeat -path.logs /var/log/filebeat
```


## Logstash

Logstash uses various yml files to translate codes into human readable files. These should be updated regularly.

This is done via cron job (with swissbib user):

```
0 2 * * 0 /usr/bin/python3 /etc/logstash/presentation/dictionaries/update_logstash_dictionaries.py >> /etc/logstash/presentation/dictionaries/output.log 2>&1
```

Logstash saves persisted queues to:

```
/swissbib_index/logstash/queue
```

This ensures that no messages are lost as long as this queue exists.