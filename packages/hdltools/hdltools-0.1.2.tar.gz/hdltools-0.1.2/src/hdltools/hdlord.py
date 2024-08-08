import json
from pathlib import Path
import argparse
from datetime import datetime
import re
from rich import print as rprint

try:
    import termprint as tp
    import hdlshare
    import hdlpolicy
    print("Import: *")
except (ModuleNotFoundError, ImportError):
    from hdltools import  hdlshare
    import hdltools.termprint as tp
    from hdltools import hdlpolicy
    print("Import: hdltools.*")

HDLFSCONFIGFILE = ".hdlfscli.config.json"

# Standard Defaults
ORD_VERSION="1.8"
SECURITY_LEVEL="sap:core:v1"
SAP_VENDOR="sap:vendor:SAP:"


def generate_api_resource(provider: str, data_product: str, share: str, recipients: set,
                     endpoint: str) -> dict:
    
    consumption_bundels = [{"ordId": f"sap.xref:consumptionBundle:{r}:v1"} for r in recipients]
    return  {
        "ordId": f"sap.{provider}:apiResource:{share}:v1",
        "title": share,
        "shortDescription": share,
        "description": share,
        "version": "1.0.0",
        "lastUpdate": datetime.now().isoformat(),
        "releaseStatus": "active",
        "apiProtocol": "delta-sharing",
        "visibility": "internal",
        "partOfPackage": f"sap.xref:package:{data_product}:v1",
        "partOfConsumptionBundles": consumption_bundels,
        "entryPoints": [ endpoint+"/shares/"+share],
        "apiResouceDefinition": [
            {
                "type": "csn",
                "mediaTyoe": "application/json",
                "url": endpoint+"/shares/"+share
            }
        ]
      }

def generate_consumption_bundels(api_resources: list, authentication='certificate') -> dict:
    cbs = list()
    for ar in api_resources:
        for pcb in ar["partOfConsumptionBundles"]:
            rmatch = re.match(r"sap.xref:consumptionBundle:(\w+):v.+",pcb["ordId"])
            if rmatch:
                recipient = rmatch.group(1)
            else:
                tp.error(f"Format pattern not matching for recipient: {pcb['ordId']}")
                recipient = "unknown"
            vmatch = re.match(r"sap.xref:consumptionBundle:\w+:v(\d+)",pcb["ordId"])
            if vmatch:
                version = vmatch.group(1)
            else:
                tp.error(f"Format pattern not matching for version: {pcb['ordId']}")
                version = "0"
            if authentication == 'certificate':
                ces =  {"type": "custom","customType": "sap:certificate:v1",
                                "customDescription": "Certificate authentication"}
            else :
                ces =  {"type": "custom","customType": "sap:bearertoken:v1",
                                "customDescription": "BearerToken authentication"}
            cbs.append( {
                    "ordId": pcb["ordId"],
                    "title": f"Delta Sharing Share {ar['title']} for {recipient}",
                    "credentialExchangeStrategies": [ ces ]
                  })
    return cbs

def generate_data_product(packageId: str, product: str, provider:str, visibility:str, 
                          release_status='active', dataproduct_type='base',
                          category='analytical') -> dict:
    return {
        "ordId": f"sap:dataProduct:{product}:v1",
        "title": product,
        "partOfPackage": packageId,
        "version": "1.0.0",
        "lastUpdate": datetime.now().isoformat(),
        "visibility": visibility,
        "releaseStatus": release_status,
        "type": dataproduct_type,
        "category": category,
        "responsible": f"SAP:provider:{provider}",
        "outputPorts": [
            "sap.{provider}:apiResouce:{product}:v1"
        ]
    }

def generate_product(product: str, provider: str) -> dict:
    return {
        "ordId": f"sap:product:{product}:v1",
        "title": product,
        "shortDescription": f"Data product \"{product}\" from \"{provider}\"",
        "vendor": SAP_VENDOR
    }

def generate_package(productId: str,product: str, provider: str) -> dict:
    return {
        "ordId": f"sap.xref:package:product:v1",
        "title": product,
        "shortDescription": f"Package of data product \"{product}\" provided by \"{provider}\"",
        "description": f"Package of data product \"{product}\" provided by \"{provider}\"",
        "version": "1.0.0",
        "partOfProducts": [productId],
        "vendor": SAP_VENDOR
    }

def main():
    parser = argparse.ArgumentParser("Generate ORD document")
    parser.add_argument("-o", "--out", help=f"output file", default ='ord.json')
    parser.add_argument("-c", "--config", help=f"HDLFs config in \'{HDLFSCONFIGFILE}\'", default ='default')
    parser.add_argument("-p", "--provider", help=f"Data product provider", required=True)
    parser.add_argument("-d", "--data_product", help=f"Data product", required=True)
    parser.add_argument("-C", "--category", choices=['business-object', 'analytical', 'other'], help=f"category (default=analytical)", default='analytical')
    parser.add_argument("-v", "--visibility", choices=['public', 'internal', 'private'], help=f"Visibility of data product (default=internal)", default='internal')
    parser.add_argument("-a", "--authentication", choices=['certificate','token'],help=f"Authentication (default=certificate)", default='certificate')
    args = parser.parse_args()

    product = args.data_product
    provider = args.provider
    authentication = args.authentication
    category = args.category
    visibility = args.visibility


    product_dict = generate_product(product,provider)
    package_dict = generate_package(product_dict['ordId'],product,provider)
    data_product_dict = generate_data_product(packageId=package_dict['ordId'], product=product,provider=provider,
                                             visibility=visibility,category=category)

    ord = {
        "openResourceDiscovery": ORD_VERSION,
        "policyLevel": SECURITY_LEVEL,
        "products": [product_dict] ,
        "packages":[package_dict],
        "dataProducts": [data_product_dict]
    }

    with open(Path.home() / HDLFSCONFIGFILE  ) as fp:
        hdlfs_params = json.load(fp)["configs"][args.config]

    endpoint = hdlfs_params['endpoint'].replace('hdlfs://', 'https://') + "/shares/v1"
    provider = args.provider
    data_product = args.data_product

    all_shares = hdlshare.list_shares(hdlfs_params)
    shares =  {share: set() for share in all_shares}

    policies = hdlpolicy.list_policies(hdlfs_params)
    for p in policies:
        user = list()
        for u in p["subjects"]:
            g = re.match(r"user:(\w+)",u)
            if g:
                user.append(g.group(1))
        for r in p["resources"]:
            g = re.match(r"share:(\w+)[:$\s+]",r)
            if g:
                share =  g.group(1)
                if share not in shares:
                    tp.error(f"Share in policy not setup: {share}")
                else: 
                    print(f"All Shares: {shares}")
                    print(f"Share {share}: {shares[share]}")
                    shares[share].update(user)
                    print(f"Share {share}: {shares[share]}")
                    print(f"All Shares: {shares}")
            if "share:*" in r:
                for rr in shares.keys():
                    shares[rr].update(user)

    ord['apiResources'] = [generate_api_resource(provider=provider, data_product=data_product, 
                                  share=s, recipients=u, endpoint=endpoint)
                     for s,u in shares.items()]
    ord['consumptionBundels'] = generate_consumption_bundels(ord['apiResources'],authentication=authentication)

    rprint(ord)

    with open(args.out,"w") as fp:
        json.dump(ord, fp, indent=4)


if __name__ == '__main__':
    main()