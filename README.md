# Elastic Kibana Logstash (ELK) Stack Configs

This repository contains all the configuration files for the ELK stack and file beat, 
which is used to process, store and anaylize metrics from all
swissbib websites.



### Logstash

Logstash needs some additional plugins which are not installed by default:

- logstash-filter-geoip
- logstash-filter-translate

To install them use:

```
sudo su -c "/usr/share/logstash/bin/logstash-plugin remove logstash-filter-translate" -s /bin/sh logstash
sudo su -c "/usr/share/logstash/bin/logstash-plugin install logstash-filter-translate" -s /bin/sh logstash
sudo su -c "/usr/share/logstash/bin/logstash-plugin install logstash-filter-geoip" -s /bin/sh logstash
```

**Important**: When updating Logstash, the plugins have to be updated manually.

To list all available plugins:
```
sudo su -c "/usr/share/logstash/bin/logstash-plugin list" -s /bin/sh logstash
```


## FileBeat

To start FileBeat:

```
/usr/share/filebeat/bin/filebeat -c /etc/filebeat/filebeat.yml -path.home /usr/share/filebeat -path.config /etc/filebeat -path.data /var/lib/filebeat -path.logs /var/log/filebeat
```
