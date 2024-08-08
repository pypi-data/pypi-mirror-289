import requests
import argparse
from datetime import datetime
import json
import re
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from rich import print as rprint
from rich.pretty import pprint 
from rich.table import Table
from rich.tree import Tree as rTree

from hdlfs.hdlfs import HDLFSConnect
import hdlpolicy
import termprint as tp

# from . import termprint as tp

# try:
#     import termprint as tp
# except (ModuleNotFoundError, ImportError):
#     import hdltools.termprint as tp

HDLFSCONFIGFILE = ".hdlfscli.config.json"


def list_shares(params, verbose=False) -> list:
    endpoint = params['endpoint']
    certificate = params['cert']
    key = params['key']
    container = re.match(r".+\/\/([^.]+)", endpoint).group(1)
    url = endpoint.replace('hdlfs://', 'https://') + "/catalog/v2/shares"
    headers = {'x-sap-filecontainer': container}
    r = requests.get(url, cert=(certificate, key), headers=headers)
    if verbose:
        tp.print_request_info("GET", endpoint.replace('hdlfs://', 'https://'), "/catalog/v2/shares", headers, params)

    if r.status_code not in [200, 201]: 
        raise ValueError(f"Unsuccessful API-call - Status code: {r.status_code} - {r.text}")
    return [s['name'] for s in json.loads(r.text)['shares']]

def share_exist(params, share, verbose=False) -> bool:
    shares = list_shares(params,verbose=verbose)
    if share in shares:
        return True
    else:
        return False


def list_schemas(share: str, params, verbose=False) -> dict:
    endpoint = params['endpoint']
    certificate = params['cert']
    key = params['key']
    container = re.match(r".+\/\/([^.]+)", endpoint).group(1)
    url = endpoint.replace('hdlfs://', 'https://') + f"/catalog/v2/shares/{share}/schemas"
    headers = {'x-sap-filecontainer': container}
    r = requests.get(url, cert=(certificate, key), headers=headers)
    if verbose:
        tp.print_request_info("GET", endpoint.replace('hdlfs://', 'https://'), f"/catalog/v2/shares/{share}/schemas", headers, params)
        

    if r.status_code not in [200, 201]: 
        raise ValueError(f"Unsuccessful API-call - Status code: {r.status_code} - {r.text}")
    return [s['name'] for s in json.loads(r.text)['schemas']]

def list_tables(share: str, schema: str, params, verbose=False) -> list:
    endpoint = params['endpoint']
    certificate = params['cert']
    key = params['key']
    container = re.match(r".+\/\/([^.]+)", endpoint).group(1)
    url = endpoint.replace('hdlfs://', 'https://') + f"/catalog/v2/shares/{share}/schemas/{schema}/tables"
    headers = {'x-sap-filecontainer': container}
    r = requests.get(url, cert=(certificate, key), headers=headers)
    if verbose:
        tp.print_request_info("GET", endpoint.replace('hdlfs://', 'https://'), f"/catalog/v2/shares/{share}/schemas/{schema}/tables", headers,params)

    if r.status_code not in [200, 201]: 
        raise ValueError(f"Unsuccessful API-call - Status code: {r.status_code} - {r.text}")
    return [t['name'] for t in json.loads(r.text)['tables']]

def add_share(share: str, params, verbose=False) -> None:
    endpoint = params['endpoint']
    certificate = params['cert']
    key = params['key']
    container = re.match(r".+\/\/([^.]+)", endpoint).group(1)
    url = endpoint.replace('hdlfs://', 'https://') + f"/catalog/v2/shares/{share}"
    headers = {'x-sap-filecontainer': container}
    r = requests.put(url, cert=(certificate, key), headers=headers)
    if verbose:
        tp.print_request_info("PUT", endpoint.replace('hdlfs://', 'https://'), f"/catalog/v2/shares/{share}", headers,params)

    if r.status_code not in [200, 201]:
        raise ValueError(f"Unsuccessful API-call - Status code: {r.status_code} - {r.text}")
    tp.info("Share successfully created", share)


def add_table(share: str, schema: str, table: str, hdl_path: str, cdf: bool, params, verbose=False) -> None:
    endpoint = params['endpoint']
    certificate = params['cert']
    key = params['key']
    container = re.match(r".+\/\/([^.]+)", endpoint).group(1)
    url = endpoint.replace('hdlfs://', 'https://') + f"/catalog/v2/shares/{share}/schemas/{schema}/tables/{table}"
    headers = {'x-sap-filecontainer': container, 'content-type': 'application/json' }
    data_dict = {"name": table, "location": hdl_path, "cdfEnabled": cdf}
    data = json.dumps(data_dict)
    r = requests.put(url, cert=(certificate, key), headers=headers, data=data)
    if verbose:
        tp.print_request_info("PUT", endpoint.replace('hdlfs://', 'https://'), f"/catalog/v2/shares/{share}/schemas/{schema}/tables/{table}", headers,params, data_dict)

    if r.status_code not in [200, 201]:
        raise ValueError(f"Unsuccessful API-call - Status code: {r.status_code} - {r.text}")
    tp.info("Table successfully created", f"{share}: {schema}.{table}")


def delete_share(share: str, drop_cascade: bool, params, verbose=False) -> None:
    endpoint = params['endpoint']
    certificate = params['cert']
    key = params['key']
    container = re.match(r".+\/\/([^.]+)", endpoint).group(1)
    url = endpoint.replace('hdlfs://', 'https://') + f"/catalog/v2/shares/{share}"
    headers = {'x-sap-filecontainer': container}
    params = {'dropCascade': 'true' if drop_cascade else 'false'}
    r = requests.delete(url, cert=(certificate, key), headers=headers, params=params)
    if verbose:
        tp.print_request_info("DELETE", endpoint.replace('hdlfs://', 'https://'), f"/catalog/v2/shares/{share}", headers,params)

    if r.status_code != 200:
        raise ValueError(f"Unsuccessful API-call - Status code: {r.status_code} - {r.text}")
    tp.info("Share successfully deleted", share)

def delete_table(share: str, schema: str, table: str, params, verbose=False) -> None:
    endpoint = params['endpoint']
    certificate = params['cert']
    key = params['key']
    container = re.match(r".+\/\/([^.]+)", endpoint).group(1)
    url = endpoint.replace('hdlfs://', 'https://') + f"/catalog/v2/shares/{share}/schemas/{schema}/tables/{table}"
    headers = {'x-sap-filecontainer': container }
    r = requests.delete(url, cert=(certificate, key), headers=headers)
    if verbose:
        tp.print_request_info("DELETE", endpoint.replace('hdlfs://', 'https://'), f"/catalog/v2/shares/{share}/schemas/{schema}/tables/{table}", headers,params)

    if r.status_code  != 200:
        raise ValueError(f"Unsuccessful API-call - Status code: {r.status_code} - {r.text}")
    tp.info("Table successfully deleted", f"{share}: {schema}.{table}")

def get_table(share: str, schema: str, table: str, params, verbose=False) -> list:
    endpoint = params['endpoint']
    certificate = params['cert']
    key = params['key']
    container = re.match(r".+\/\/([^.]+)", endpoint).group(1)
    url = endpoint.replace('hdlfs://', 'https://') + f"/catalog/v2/shares/{share}/schemas/{schema}/tables/{table}"
    headers = {'x-sap-filecontainer': container}
    r = requests.get(url, cert=(certificate, key), headers=headers)
    if verbose:
        tp.print_request_info("GET", endpoint.replace('hdlfs://', 'https://'), f"/catalog/v2/shares/{share}/schemas/{schema}/tables/{table}", headers,params)

    if r.status_code != 200: 
        raise ValueError(f"Unsuccessful API-call - Status code: {r.status_code} - {r.text}")
    return json.loads(r.text)

def add_csn(share: str, schema: str, table: str, csn: dict, params, verbose=False) -> None:
    endpoint = params['endpoint']
    certificate = params['cert']
    key = params['key']
    container = re.match(r".+\/\/([^.]+)", endpoint).group(1)
    url = endpoint.replace('hdlfs://', 'https://') + f"/catalog/v2/shares/{share}/schemas/{schema}/tables/{table}/csn"
    headers = {'x-sap-filecontainer': container, 'content-type': 'application/json' }
    data = json.dumps(csn)
    r = requests.put(url, cert=(certificate, key), headers=headers, data=data)
    if verbose:
        tp.print_request_info("PUT", endpoint.replace('hdlfs://', 'https://'), f"/catalog/v2/shares/{share}/schemas/{schema}/tables/{table}/csn", headers,params, data)

    if r.status_code not in [200, 201]:
        raise ValueError(f"Unsuccessful API-call - Status code: {r.status_code} - {r.text}")
    tp.info("CSN successfully added", f"{share}: {schema}.{table}")

def get_csn(share: str, schema: str, table: str, params, verbose=False) -> dict:
    endpoint = params['endpoint']
    certificate = params['cert']
    key = params['key']
    container = re.match(r".+\/\/([^.]+)", endpoint).group(1)
    url = endpoint.replace('hdlfs://', 'https://') + f"/catalog/v2/shares/{share}/schemas/{schema}/tables/{table}/csn"
    headers = {'x-sap-filecontainer': container}
    r = requests.get(url, cert=(certificate, key), headers=headers)
    if verbose:
        tp.print_request_info("GET", endpoint.replace('hdlfs://', 'https://'), f"/catalog/v2/shares/{share}/schemas/{schema}/tables/{table}/csn", headers,params)

    if r.status_code != 200: 
        raise ValueError(f"Unsuccessful API-call - Status code: {r.status_code} - {r.text}")
    return json.loads(r.text)

def main():

    parser = argparse.ArgumentParser("Manage HDLFS shares")
    parser.add_argument("action", choices=['list', 'add', 'delete', 'get','addcsn', 'getcsn', 'addtables'], help=f"Command for \'target\'-argument")
    parser.add_argument("target", nargs="*", help="share schema table or hdlfs-path to tables (optional)")
    parser.add_argument("-r", "--recursive", help="List recursively", action="store_true")
    parser.add_argument("-m", "--metadata", help="Show metadata of table (action=list)", action="store_true")
    parser.add_argument("-p", "--path", help="HDLFS data folder")
    parser.add_argument("-c", "--config", help=f"HDLFs config in \'{HDLFSCONFIGFILE}\'", default ='default')
    parser.add_argument("-d", "--disable_cdf", help="Disable CDF", action="store_true")
    parser.add_argument("-f", "--force", help="Forcefully delete all share tables and share NOT IMPLEMENTED", action="store_true")
    parser.add_argument("-v", "--verbose", help="Print http-request details", action="store_true")

    args = parser.parse_args()

    with open(Path.home() / HDLFSCONFIGFILE  ) as fp:
        hdlfs_params = json.load(fp)["configs"][args.config]

    hdl_path = args.path if args.path else None

    cdf = True
    if args.disable_cdf:
        cdf = False
    target = args.target
    cascade = args.force

    match args.action:
        case 'list':
            tree = None
            match len(target):
                case 0:
                    tree = list_shares(hdlfs_params, args.verbose)
                    if args.recursive:
                        tree = dict.fromkeys(tree,list())
                        for share in tree.keys():
                            tree[share] = dict.fromkeys(list_schemas(share, hdlfs_params, args.verbose),list())
                            for schema in tree[share].keys():
                                tree[share][schema] = list_tables(share, schema, hdlfs_params, args.verbose) 
                                if args.metadata:
                                    tree[share][schema] = dict.fromkeys(tree[share][schema],list())
                                    for table in tree[share][schema].keys():
                                        metadata = get_table(share, schema, table, hdlfs_params, args.verbose)
                                        tree[share][schema][table] = [metadata['location'], metadata['type'],
                                                                    'cdf: '+ str(metadata['cdfEnabled'])]
                case 1:
                    share = target[0]
                    tree = {share: list_schemas(share, hdlfs_params, args.verbose)}
                    if args.recursive:
                        tree[share] = dict.fromkeys(tree[share],list())
                        for schema in tree[share].keys():
                            tree[share][schema] = list_tables(share, schema, hdlfs_params, args.verbose)
                            if args.metadata:
                                tree[share][schema] = dict.fromkeys(tree[share][schema],list())
                                for table in tree[share][schema].keys():
                                    metadata = get_table(share, schema, table, hdlfs_params, args.verbose)
                                    tree[share][schema][table] = [metadata['location'], metadata['type'],
                                                                'cdf: '+ str(metadata['cdfEnabled'])]

                case 2:
                    share, schema = target 
                    tree = {share: {schema: list_tables(share, schema, hdlfs_params, args.verbose)}}
                    if args.metadata:
                        tree[share][schema] = dict.fromkeys(tree[share][schema],list())
                        for table in tree[share][schema].keys():
                            metadata = get_table(share, schema, table, hdlfs_params, args.verbose)
                            tree[share][schema][table] = [metadata['location'], metadata['type'],
                                                            'cdf: '+ str(metadata['cdfEnabled'])]
                case _:
                    tp.error("Only 2 parameters (share, schema) expected for argument list")
                    return -1 
            tp.print_tree(tree)


        case 'add':
            match len(target):
                case 0:
                    rprint(f"[{tp.cwarn}]No target given: share, ((schema), (table))")
                case 1: 
                    add_share(target[0], hdlfs_params, args.verbose)
                case 2: 
                    tp.error("Only adding share or adding share, schema and table are implemented")
                case 3:
                    tp.info("New share", f"{target[0]}.{target[1]}.{target[2]}")
                    if not share_exist(hdlfs_params, target[0]):
                        tp.info("Create share", target[0])
                        add_share(target[0], hdlfs_params, args.verbose)
                    add_table(share=target[0], schema=target[1], table=target[2], hdl_path=hdl_path, cdf=cdf, 
                              params=hdlfs_params, verbose=args.verbose)


        case 'delete':
            match len(target):    
                case 0:
                    rprint(f"[{tp.cwarn}]No target given: share or share-schema-table")
                case 1: 
                    delete_share(target[0], cascade, hdlfs_params, verbose=args.verbose)
                case 2: 
                    tp.error("Only shares or share-schema-tables can be deleted")
                case 3:
                    delete_table(share=target[0], schema=target[1], table=target[2], params=hdlfs_params, verbose=args.verbose)

        case 'get':
            if len(target)!= 3:
                rprint(f"[{tp.cerror}]Share-schema-table target needs to be passed!")
                return -1
            
            table_info = get_table(target[0],target[1], target[2], params=hdlfs_params, verbose=args.verbose)
            
            try: 
                csn = get_csn(target[0], target[1], target[2], params=hdlfs_params, verbose=args.verbose)
                table_info["csn uploaded"] = True
            except Exception as e:
                table_info["csn uploaded"] = False
            
            tp.dictionary(table_info, title=f"Metadata of {'.'.join(target)}", columns=["key", "value"])

        case 'addcsn':
            if len(target)!= 4:
                rprint(f"[{tp.cerror}]Share-schema-table target needs to be passed and csn-filename!")
                return -1
            with open(target[3], 'r') as file:
                csn = json.load(file)
            add_csn(target[0], target[1], target[2], csn, hdlfs_params, verbose=args.verbose)

        case 'getcsn':
            if len(target) < 3:
                rprint(f"[{tp.cerror}]Share-schema-table target needs to be passed and filename to store csn!")
                return -1
            csn = get_csn(target[0], target[1], target[2], params=hdlfs_params, verbose=args.verbose)
            csn_json = json.dumps(csn,indent=4)
            print(csn_json)
            if len(target) == 4:
                with open(target[3], 'w') as file:
                    file.write(csn_json)

        case 'addtables':
            if len(target)!= 3:
                rprint(f"[{tp.cerror}]Share-schema and hdlfs-folder path needs to be passed!")
                return -1
            if not share_exist(hdlfs_params, target[0]):
                tp.info("Create share", target[0])
                add_share(target[0], hdlfs_params, args.verbose)

            hdlfs_connect = HDLFSConnect(endpoint=hdlfs_params['endpoint'], cert_file=hdlfs_params['cert'], key_file=hdlfs_params['key'])
            tables = [t for t in hdlfs_connect.list_content(target[2]) if not t.endswith("_errors") and not t == 'error_tables' ]
            for table in tables:
                tp.info("New table added to share:", f"{target[0]}.{target[1]}.{table}")
                location = target[2] + '/' + table

                metadata_path = '/' + target[2] + '/' + table + '/metadata.csn'
                try :
                    tp.info("Download:",metadata_path)
                    csn_json = hdlfs_connect.download(metadata_path)
                    add_table(share=target[0], schema=target[1], table=table, hdl_path=location, cdf=cdf, 
                            params=hdlfs_params, verbose=args.verbose)
                    csn = json.loads(csn_json)
                    tp.info("Metadata.csn updloaded")
                    add_csn(target[0], target[1], table, csn, hdlfs_params, verbose=args.verbose)
                except Exception as e:
                    tp.error("Exception - cannot add table to share: ", e)
                    continue
            # created_at = int(datetime.now().timestamp())
            # policy = {'name': target[0],'resources': 'share:'+target[0], 'privileges': ['open','browse'], 
            #           "author": "thh", "createdAt": created_at,
            #           'subjects':'x509:CN=TENANT_FORMATION_USER,L=2e776767-e02d-4a7b-8ecd-09052117924b_c592fc1f-1410-4d1f-a2ad-2de5d6ab4941,OU=6414e182-39c3-4ed4-b5d3-c49a9f5f479b,OU=Canary,OU=SAP Cloud Platform Clients,O=SAP SE,C=DE'}
            # hdlpolicy.add_policy(policy, hdlfs_params, verbose=args.verbose)


if __name__ == '__main__':
    main()