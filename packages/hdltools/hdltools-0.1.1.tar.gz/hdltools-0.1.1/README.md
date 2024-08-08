# HDL Tools

This repository contains command line code for creating

1. SAP authorized certificates
2. HDL instances
3. test data (Delta lake) for one or many instances
   1. ``hdlgenspark``  - using a local spark installation (many instances)
   2.``hdlgen`` - WiP: using plain python with deltalake package and uploading result to 1 hdl instance
4. Policies for an HDL instances
5. Shares for Delta Sharing
6. Delta Sharing client that support certificate and token authentication

It uses the published APIs for HDLFS and Service Manager. 


Content

1. [sapcert - Support creating certificates and showing details of certificates](docs/SAPCertificateService.md)
2. [hdlinst - Creating hdl instances and providing information](docs/SetupHDLFS.md)
3. [hdlfscli - Comments to the official SAP HDL client tool](docs/hdlfscli.md)
4. [hdlshare - Create delta sharing entries in hdl-instance catalog](docs/hdlsharesetup.md)
5. [hdlpolicy - Manage hdl policies used by web-hdlfs, catalog and delta sharing](docs/hdlpolicysetup.md)
6. [hdlclient - Delta Sharing client](docs/hdldeltasharing.md)


## Installation of hdltools

1. clone the repostory
2. Run ``python -m build; pip install . ``

It is open if we should upload the code to **pypi.org**.

Then the installation would just be:
```shell
pip install hdltools
```

## URL Compositions

### Catalog API

<instance-uuid>.files.hdl.<hld-cluster-endpoint>/catalog/v2
<instance-uuid>.files.hdl.<hld-cluster-endpoint>/policies/v2


### Audience in JWT
<instance-uuid>.files.<hld-cluster-endpoint>

### Delta Sharing

- Token Access: <instance-uuid>.sharing.hdl.<hld-cluster-endpoint>/shares/v1/
- Cert Access: <instance-uuid>.files.hdl.<hld-cluster-endpoint>/shares/v1/






