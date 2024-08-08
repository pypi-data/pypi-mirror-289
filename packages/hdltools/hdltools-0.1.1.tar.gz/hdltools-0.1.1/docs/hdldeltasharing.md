# HDL Delta Sharing Client

HDL Delta Sharing server is compliant to the Delta Sharing protocol.

Because currently only certificate/key authorization is supported for delta-sharing standard Delta-Sharing client need not to be working yet. 

For testing Delta Sharing I have developed a client supporting certificate/key authorization.


## hdlclient - Delta Sharing Client

Installation: `pip install hdltools`


```shell
hdlclient -h
usage: hdlclient [-h] [-r] [-d DIRECTORY] [-m] [-v VERSION] [-e END_VERSION] [-c CONFIG]
                 profile {list,download,changes,metadata} [target ...]

positional arguments:
  profile               Profile of delta sharing
  {list,download,download_changes,metadata}
                        Action
  target                (optional) Target: <share> [<schema>] [<table>]].

options:
  -h, --help            show this help message and exit
  -r, --recursive       Sync files with hana
  -d DIRECTORY, --directory DIRECTORY
                        Directory to store data.
  -m, --meta            Download metadata as csn-file to edit before starting the replication.
  -v VERSION, --version VERSION
                        Start version
  -e END_VERSION, --end_version END_VERSION
                        Version end
  -c CONFIG, --config CONFIG
                        Config-file for HANA access (yaml with url, user, pwd, port)

```

### Examples

List avaliable shares for user/profile crossadmin: `hdlclient crossadmin list -r`

[share tree](../images/sharetree.png)

`hdlclient dehcm list hcm de`

[share tree](../images/treesharehcmus.png)

Currently the list function is working counter-intuitively. If a user has not the authorisation to view all members of a level, then nothing is listed, even when there is a branch for which an authorization is available.

View metadata of a table: ``hdlclient crossadmin metadata hcm us employees``

Download data without versions: ``hdlclient crossadmin download hcm us employees -d tmp``

Download data with versions: ``hdlclient crossadmin download hcm us employees -d tmp`

Download data changes: ``hdlclient crossadmin changes hcm us employees -d tmp -v 2``

