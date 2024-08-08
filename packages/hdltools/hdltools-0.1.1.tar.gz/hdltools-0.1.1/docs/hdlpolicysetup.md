## HDL Policy

With policyies you can govern the access to 

1. Catalog entries
2. HDLFS paths
3. Delta Shares

 Currently only the delta sharing policies are fully implemented. 

 ### URLS

 - [Policy-swagger](https://github.wdf.sap.corp/DBaaS/hdl-files-service/blob/master/doc/api-spec/src/policies-swagger.yaml)
 - [Policy Documentation](https://github.wdf.sap.corp/DBaaS/Docs/blob/master/docs/designs/hanadatalake/hdlf/hdl-files-policies.md)

 ## Access 

 You can either add
 
 - user certificates to the HDLFS instance,
 - policies for user to the policy repository of each HDL instance or 
 - for Delta Sharing only a generated JWT.

Currently for Delta Sharing only a certificate-based authentication is available. 


## Commandline tool hdlpolicy

For ease of use I have written a commandline tool (currently no support):
```shell
pip install hdlshare
```

It is assumed that you have a ``.hdlfs.config.json`` file in your home directory and there is one config "default" with which you work primarly. Otherwise you need the option '--config <config name>

```shell
hdlpolicy -h
usage: Manage HDLFS share policies [-h] [-p POLICY] [-s SUBJECT] [-R RESOURCE] [-P PRIVILEGE] [-C CONSTRAINT] [-D DAYS] [-c CONFIG]
                                   {list,add,delete,copy,token,showtoken,cert_profile} [policy_names ...]

positional arguments:
  {list,add,delete,copy,token,showtoken,cert_profile}
                        Action
  policy_names          Policy name (for 'copy' arg 2 policies)

options:
  -h, --help            show this help message and exit
  -p POLICY, --policy POLICY
                        Policy content (json)
  -s SUBJECT, --subject SUBJECT
                        subject/user to add or delete from policy and for showing or generating tokens
  -R RESOURCE, --resource RESOURCE
                        Resource to add or delete from policy
  -P PRIVILEGE, --privilege PRIVILEGE
                        Privilege to add or delete from policy
  -C CONSTRAINT, --constraint CONSTRAINT
                        Constraint to add or delete from policy
  -D DAYS, --days DAYS  Days before expiring from now on.
  -c CONFIG, --config CONFIG
                        HDLFs config in '.hdlfscli.config.json'

```


### List policies

```shell
hdlpolicy list
```

or
```shell
hdlpolicy -c <config> list
```

### Managing policys

Adding new policy from file
```shell
 hdlpolicy add dehcm -p templates/dehcm.json 
```

Adding new policy from json-str
```shell
hdlpolicy add dehcm -p "{\"resources\": [\"share:hcm:schema:de:table:*\"],\"subjects\": [\"user:dehcm\"],\"privileges\": [\"browse\",\"open\"]}"
```

Copy policy
```shell
hdlpolicy copy dehcm ushcm
```

#### Modifying policies

Add user to a policy
```shell
hdlpolicy add dehcm -s user:frhcm
```

Delete user from a policy

```shell
hdlpolicy delete dehcm -s user:frhcm
```

### Create recipient profiles

#### Json Web Token
```shell
hdlpolicy token -s dehcm
```
![Token](../images/jwtgeneration.png)
 
with profile-file:
```json
{
    "shareCredentialsVersion": 1,
    "bearerToken": "eyJhbGciOiJS.....dyHavo_NEA",
    "endpoint": "https://96d268cd-fb4c-4f33-a212-7efd5a6b4dec.sharing.hdl.prod-us20.hanacloud.ondemand.com/shares/v1",
    "expirationTime": "2024-01-14T10:20:48",
    "sub": "dehcm"
}
```

#### Certificate/key

First create a new certificate, if not existing already
```shell
sapcert create dehcm
```

```shell
hdlpolicy cert dehcm
```
creates profile-file:

```json
{
    "shareCredentialsVersion": 1,
    "cert": "/Users/D051079/GitHub/delta_sharing_python_client/certificates/dehcm.pem",
    "key": "/Users/D051079/GitHub/delta_sharing_python_client/certificates/dehcm.key",
    "endpoint": "https://96d268cd-fb4c-4f33-a212-7efd5a6b4dec.files.hdl.prod-us20.hanacloud.ondemand.com/shares/v1",
    "notValidBefore": "2023-12-15T09:26:40",
    "notValidAfter": "2023-12-16T10:26:40",
    "subject": "CN=dehcm,L=Walldorf BW,OU=31b824eb-0ee3-4896-b769-d22957f91d2f,OU=SAP Cloud Platform Clients,O=SAP SE,C=DE"
}

```
