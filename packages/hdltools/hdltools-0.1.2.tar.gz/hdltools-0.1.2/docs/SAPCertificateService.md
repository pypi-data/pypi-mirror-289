# Using SAP Certificate Authority

For creating signed certificates you can use an SAP PKI service that you can setup in your sub-account. The certifcates subject includes an "OU" with the sub-account ID. 

## Setting up PKI-Service

![Create PKI-Service](../images/createPKIService.png)

In order to use the PKI-Service for creating certificfates you need to create a service-key binding and download it locally.

![Create PKI Service Key Binding](../imagages/../images/pki_servicekey.png)

## Creating a SAP-signed certificate process

1. Create a certificate subject using the subject pattern from the service-key file and your new "CN" \(optionally "Location"\)
2. Create a private key and a certificate request using the previously created subject 
3. Ask for a token to interact with the PKI Authorisation
4. Request the certificate

## Using Script "sapcert"

For convenience reasons I have created a commandline tool to create certificates using a PKI-service and a downloaded service-key binding.

```shell
% sapcert -h 
usage: Creates, show details and list certificates. [-h] [-s] [-L] [-p PKISERVICE_FILE] [-d CERT_DIR] [-v VALIDITY]
                                                    [-t {HOURS,DAYS,MONTHS,YEARS}] [-l LOCATION] [-P P12PWD]
                                                    {create,list,details} [CN]

positional arguments:
  {create,list,details}
                        Command details (action)
  CN                    Subject common name (= certificate name)

options:
  -h, --help            show this help message and exit
  -s, --subject         Subject of lowest certificate
  -L, --list            List certificates in certificates folder
  -p PKISERVICE_FILE, --pkiservice_file PKISERVICE_FILE
                        Service key file for PKI service
  -d CERT_DIR, --cert_dir CERT_DIR
                        Certificate directory
  -v VALIDITY, --validity VALIDITY
                        Number
  -t {HOURS,DAYS,MONTHS,YEARS}, --validity_type {HOURS,DAYS,MONTHS,YEARS}
                        Validity type
  -l LOCATION, --location LOCATION
                        Subject location
  -P P12PWD, --P12pwd P12PWD
                        Password for keystore that is created.

```

Relative to my working directory I have created a folder with my service keys: "./service_keys" and a certificates-folder that stores all created certificates. Having this I can easily create a new certificate for "hdlclient" with a validity of 60 days by

```shell
sapcert create hdlclient  -v 60 -t DAYS
```

![Result of command](../images/sapcerthdlclient.png)

### Further Examples

List all certificates in certificates folder:

```shell
sapcert list
```

Get details of a certificate (subject fields and validity):
```shell
sapcert details hdlclient
```




