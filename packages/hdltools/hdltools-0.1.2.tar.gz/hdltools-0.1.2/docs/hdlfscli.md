# Command Tool for interacting with HDL Files

- [SAP Help](https://help.sap.com/docs/hana-cloud-data-lake/user-guide-for-data-lake-files/hdlfscli-data-lake-files-utility)
- [Git Repository](https://github.wdf.sap.corp/bigdataservices/hdlfs-cli) with latest binaries


To ease the access to HDLFS you can create a config-file in you home-directory by:

```shell
hdlfscli \
   -cert client.crt \
   -key client.key \
   -s  <endpoint> \
   -config default \
   -dump-config \
   ls
```

The option "-dump-config" stores the config data to the file ".hdlfscli.config.json" in your homedirectory. 

```
{
  "configs": {
    "default": {
        "timeout": 3000000000,
        "cert": "/Users/D051079/certificates/hdlmt1.pem",
        "key": "/Users/D051079/certificates/hdlmt1.key",
        "user": "",
        "role": "",
        "endpoint": "hdlfs://xxxxxxxxxxx.files.hdl.prod-us20.hanacloud.ondemand.com",
        "parallel": 10,
        "format": "TEXT"
        }
    }
}
```

To use a specific config you call hdlfscli with the option `-c`:
```hdlfscli -c <config> ls data```


This configuration file is been used for all the commandline tools introduced in this repo:

- hdlinst
- hdlshare
- hdlpolicy


