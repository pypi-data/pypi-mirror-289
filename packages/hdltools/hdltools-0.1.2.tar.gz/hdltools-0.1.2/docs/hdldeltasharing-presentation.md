# Presentation HDL Delta Sharing from Scratch

## Intro
This presentation will lead you to setup a Delta Sharing scenario from scratch. Be noted that this was recorded end of 2023 and it uses what then was productively available. Be sure that a lot of features are in the making or have already been completed. So you should check out the git repositorys what additionally is ready. 

My name is Thorsten Hapke and I am product manager of the crossproduct frontrunner team. 

## Content

As promised I show each step from the very beginning:

- Create Certificates signed by SAP Certificate Authorization
- Deploy HDL Instances
- Generate Test Data – Delta Lake
- Use hdlfscli
- Add HDL Policies for HDLFS instance
- Build Shares
- Use Delta-Sharing Client

You find all of the coding and the documentation on our SAP github. 

## Create Certificates

First we need to create a certificates and because we need this very often it must be as convenient as possible.

What we have to do is:

- Setup PKI Service in BTP subaccount
- Create private key and public certificate
- Retrieve token from PKI Service
- Request for signing the certificate

So let's go first to our BTP subaccount and create a PKI service, create a serice key and download it. 

## DEMO PKI

## DEMO Create Certificate

I am using my commandline tool sapcert to create a certificate with a CommonName CN. All the other subject fields are adopted from the Certificate Service of SAP. For all my command lines I choose the lazy way, that means use as much as possible defaults and run the command in a prepared environment. I am here in the root folder of my local repository. 

With ``sapcert -h`` you see all the options and defaults

With ``sapcert create crmadmin -v 10 `` you create a new certificate

With ``sapcert details crmadmin`` you get again the details of the certificate

The filename of the certificate is the same as the CommonName, by the way. 

## Slide: Create HDFS Instance

There are 3 ways of creating HDLFS instances

1. Manually with BTP main view
2. SAP HANA Cloud Administration Tool  
3. Service Manager API 

We are going to use the Service Manager API with a commandline app. But before we can use the Service Manager API we need to start the service manager in our subaccount and create a service key. This is quite similiar to what we have done with the PKI service for requesting signed certificates. 

After we have done these pre-requisite steps we can start creating hdlfs-instances. Again I put the calls into a script ``hdlinst``. 

## DEMO Create Serice Key

First we have to 
1. setting up a **Service Manager** in your subaccount
2. creating a service key
3. downloading the service key

## DEMO Create HDLFS instance

First again the help of the command ``hdlinst -h``

Again you see a lot of defaults I am using, including the certificates path and the service-key file. 

I could first list the deployed hdl instances with ``hdlinst list`` and can have a look what users have access to an instance.

``hdlinst user xpm-hdl-mt1``.

Finally I can create a new instance. But before that let's have a look to the template that is used:

``cat configs/hdlfs_templates.json``. Here you see the 2 roles "admin' and 'user' and the pattern that will be replaced by the Common Names coming from the commandline options. There is also the root certificate of SAP that is the ultimated certificate authority. 

Finally let's create a new hdlf instance

``hdlinst create xpm-hdl-mt4 -a hdlmt4 -u hdlmtcross``. The admin and the user needs to have accessible certificates in the certificates folder.  

For interacting with an hdlfs-instance I am using a config-file that is also used by the official commandline tool ``hdlfscli``:  

``cat ~/.hdlfscli.config.json``. Here you see the endpoint and location of the key/certificate-files. 

To create a new entry for the newly created instance use: ``hdlinst add2config xpm-hdl-mt4 -a hdlmt4``

## Slide Generate Data

Now I must generate some data that I like to share via Delta Sharing. Currently the only way to generate Delta lake formatted files on HDLFS is by Spark and it is in general the mostly used way. 

``hdlgenspark create <hdl instances> -u <user> -y <country> -p <hldfs-path> -n 10``

## DEMO Generate Data

## Slide Create Delta Share

Now we need to create a share and add to the share a table with a schema. The shares are part of the catalog repository. It might be worth mentioning that delta sharing must be activated by operations. We still need a kind of control in this first phase. 

## DEMO Create Share

``hdlshare list``
``hdlshare add hxm US employees –p data/US/persons``
``hdlshare list -rm``

## Slide Policy

After we have created the share we need to define the recipients and the authorizations for a recipient. For this we use the central policy feature of Hana Datalake. With this policy app you can also define the accessibility of catalog tables and paths. In our case we are going to use this only for delta shares. 

Again I have put the API-calls into a commandline tool. 

Let's see how this looks like in action. 

## DEMO Policy

``hdlpolicy list``
``hdlpolicy add admin –p templates/dsadmin.json``
``hdlpolicy token –s dsadmin``
``hdlpolicy cert –s dsadhdmin``

## Slide Recap

Before we finally test our setup let's shortly recap what we have done so far:

1. We created certificates and then
2. deployed an HDLFS instance
3. Once we generated test data 
4. We defined shares and
5. created policies. 

Now we are ready to use a delta sharing client. Because we currently have only certificate authentication available we could not use a publicly available client. I therefore implemented the delta sharing protocol in a commandline tool: client. 