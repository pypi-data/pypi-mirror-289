# Create HDLFS Instance

There are 3 ways of creating HDLFS instances

1. Manually with BTP main view
2. SAP HANA Cloud Administration Tool  
3. Service Manager API 

## Manually with BTP Main View

![BTP UI creating HDLFS instance](../images/BTPHDLFSinstance.png)


## SAP HANA Cloud Administration Tool  

![BTP Cloud admin tool](../images/MenuHanaTool.png)

![Tool create instance](../images/toolcreateinstance.png)

## Service Manager API

In case you create many HDLFS instances and prefer a commandline interaction you can use scripts and the service manager API. 

For using the [Service Manager API](https://service-manager.cfapps.eu10.hana.ondemand.com/api/#/Service%20Instances/getAllServiceInstances) you need first 

- setting up a **Service Manager** in your subaccount
- create a service key
- download the service key

![Service Key Manager](../images/skmanager.png)

 For a convenient usage I have developed commandline **hdlinst**.

 # hdlinst-script

```shell
hdlinst -h
usage: hdlinst [-h] [-a ADMIN] [-u USER] [-H HANASERVICENAME] [-s SERVICE_PLAN] [-t TEMPLATE] [-r CA_CERTIFICATE] [-S SERVICE_KEY]
               [-d DIR_CERTIFICATES]
               {list,details,user,create,delete,add2config} [name]

Utility to create a manage HDL instances via Service Manager API.

positional arguments:
  {list,details,user,create,delete,add2config}
                        Action
  name                  HDLFS instance name (required for creating instance)

options:
  -h, --help            show this help message and exit
  -a ADMIN, --admin ADMIN
                        User with ADMIN role (required for creating instance) and adding entry to config.
  -u USER, --user USER  User with USER role (required for creating instance).
  -H HANASERVICENAME, --HanaServicename HANASERVICENAME
                        SAP BTP HANA Service Name
  -s SERVICE_PLAN, --service_plan SERVICE_PLAN
                        SAP BTP service plan
  -t TEMPLATE, --template TEMPLATE
                        File-Template to configure HDLFS instance
  -r CA_CERTIFICATE, --ca_certificate CA_CERTIFICATE
                        Trusted CA certificate file
  -S SERVICE_KEY, --service_key SERVICE_KEY
                        Service Manager key file
  -d DIR_CERTIFICATES, --dir_certificates DIR_CERTIFICATES
                        Directory of certificates

```


For creating and managing HDL instances I have developed a commandline tool **hldinst**.

Folder structure to use default commandline attributes:
- ./certificates: for the certificates relative to current working directory
- ./service_keys/sm-sk.txt: service-key 


## List Instances
```shell
hdlinst  list
```

## Access Parameter
```shell
hdlinst user <hdl-instance>
```

## Instance Details
```shell
hdlinst details xpm-mt1
```

Currently the hdlfs-endpoint is not provided by the hdl-instance details but must be build by

<service id>.files.hdl.<regional hana cloud domain>, e.g. 

40e60329-e854-46e2-89d4-728093fb7576.files.hdl.prod-us30.hanacloud.ondemand.com

The following command adds a config section to the configuration file: $HOME/.hdlfscli.config.json

```shell
hdlinst add2config xpm-mt1 -C hdlmt1
```

To create a new hdl-instance
```shell
hdlinst create <hld instance name>  -a <admin> -u <user>
```
This uses a template file in folder *'./configs/hdlfs_template.json'*. The admin and the user needs to have accessible certificates in the certificates folder.  


## Additional Requirements for HDL Instance management

1. Adding API for deleting an HDLFS instance

