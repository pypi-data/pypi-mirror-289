# Setup HDL Delta Sharing

## Activation

In order to use Delta Sharing with an HDL Files instance you need first submitting a request to activate  Delta Sharing for a BTP subaccount. This you do by opening a jira ticket in the project **HC01 - HANA Cloud Incident Management (HC01)** and add the following information:

1. Project Name: xPM Data Platform Deployment Template
2. Project Sponsor:
3. Project Summary:
4. Business Unit:
5. DL for communication, or preferred commmuniation method:
6. Hyperscaler/Regions in which you would like this feature support:
7. BTP Global/Sub accounts (IDs) that will be consuming the feature:

[Example Ticket](https://jira.tools.sap/browse/HC01-170224)

Currently Delta Sharing is only available for Azure!


## Share Management

For exposing a Delta Sharing API you need to 

1. Create share(s) entry in the catalog API
2. Add access policies to the shares that includes adding recipients
3. Distribute the 'profile'-file to the recipients and the certificates/key-pair

[Repo - Documentation](https://github.wdf.sap.corp/DBaaS/Docs/blob/master/docs/designs/hanadatalake/hdlf/hdl-files-delta-sharing.md#jwts-and-transport)

There are Rest-APIs provided to interact with the catalog-api:
[swagger](https://github.wdf.sap.corp/DBaaS/hdl-files-service/blob/master/doc/api-spec/src/catalog-swagger.yaml)

## hdlshare - Commandline

For demonstrating purpose I have implemented the RestAPI with a commandline tool: hdlshare. 

```shell
hdlshare -h                
usage: Manage HDLFS shares [-h] [-r] [-m] [-C] [-p PATH] [-c CONFIG] [-d] {list,add,delete,get} [target ...]

positional arguments:
  {list,add,delete,get}
                        Command for 'target'-argument
  target                share schema table (optional)

options:
  -h, --help            show this help message and exit
  -r, --recursive       List recursively
  -m, --metadata        Show metadata of table (action=list)
  -C, --cascade         Drop cascade when deleting share (action=delete)
  -p PATH, --path PATH  HDLFS data folder
  -c CONFIG, --config CONFIG
                        HDLFs config in '.hdlfscli.config.json'
  -d, --disable_cdf     Enable CDF

```

### Examples

List all shares and tables 
```shell
% hdlshare list -r

shares
├── sbm
├── hxm
└── crm
    └── us
        └── customer

```

Add new table to share
```shell
% hdlshare add hxm us employees --path data/deltalake/persons
Table successfully added: hxm: us.employees
% hdlshare list -r
shares
├── sbm
├── hxm
│   └── us
│       └── employees
└── crm
    └── us
        └── customer
```

Details of Share:schema:table:
```shell
% hdlshare list -rm
shares
├── sbm
├── hxm
│   └── us
│       └── employees
│           ├── data/deltalake/persons
│           ├── DELTA
│           └── cdf: True
└── crm
    └── us
        └── customer
            ├── data/deltalake/US/customer
            ├── DELTA
            └── cdf: True
```
