# Show&Tell Jan 2024

Presentation Flow

## Intro
### Slide Intro

## Certificate
### Slide: Certificate
### Terminal: Commands

1. ``sapcert list``
2. ``sapcert details dehcm``
3. ``sapcert create hdlmt4``

## HDLFS instance

### Slide HDLFS Instance

### Browser: BTP Subaccount: LoB DP HXM

1. Create on main page
2. Create via Hana Cloud App
3. Service Manager - running instance

### Terminal: Commands
1. ``hdlinst list``
2. ``hdlinst create xpm-hdl-mt4 -a hdlmt4 -u hdlmtcross``

### Browser: BTP Subaccount: LoB DP HXM
Verify creation

## HDLFSCLI

### Terminal: 
``hdlfscli -h``

### VSCode: Show .hdlfscli.config.json

## Create Data with Spark

### Terminal: 
``hdlinst add2config xpm-hdl-mt4 -a hdlmt4``

``hdlgenspark create xpm-hdl-mt4 -u hdlmt4 -y FR -p data -n 10``

``hdlfscli -config xpm-hdl-mt4 ls data/FR/persons``


## Shares

### Slide: Shares
### Terminal: Commands

``hdlshare -c xpm-hdl-mt4 list`` 

``hdlshare -c xpm-hdl-mt4 add hxm FR employees –p data/FR/persons``

``hdlshare -c xpm-hdl-mt4 add crm FR customer –p data/FR/persons``

``hdlshare -c xpm-hdl-mt4 add sbn FR supplier –p data/FR/persons``

## Policies

### Slide
### Terminal: Commands

``hdlpolicy -c xpm-hdl-mt1 list``

``hdlpolicy -c xpm-hdl-mt4 list``

``hdlpolicy -c xpm-hdl-mt4 add fradmin -p templates/fradmin.json``

``hdlpolicy -c xpm-hdl-mt4 token –s fradmin``

``hdlpolicy -c xpm-hdl-mt4 cert -s fradmin``

## Delta Sharing Client

## Terminal: Commands

``hdlclient fradmin.json list``

``hdlclient fradmin.json metadata hxm fr employees``

``hdlclient fradmin.json download hxm fr employees``

## Slide







