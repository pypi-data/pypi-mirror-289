"""
Python interface to SAP HDLFS.

Status: Work in progress, unsupported

by Thorsten Hapke, thorsten.hapke@sap.com
"""

import json
import re
from datetime import datetime
from pathlib import PurePath, Path
import requests_pkcs12
import requests
from rich import print as rprint
from rich.table import Table


try:
    import termprint as tp
except (ModuleNotFoundError, ImportError):
    import hdltools.termprint as tp

HDLFSCONFIGFILE = ".hdlfscli.config.json"

blue4 = "rgb(137,209,255)"
blue7 = "rgb(0,112,242)"

info = blue4
variable = blue7


def get_path_content(response: dict) -> list:
    """
    Extracts the path items from response of LISTSTATUS API
    :param response: Response from LISTSTATUS
    :return: List of path items (folders and files)
    """
    return [f['pathSuffix'] for f in response['FileStatuses']['FileStatus']]


def get_recursive_path_content(response: dict) -> list:
    """
    Extracts the path items from response of LISTSTATUS_RECURSIVE API
    :param response: Response from LISTSTATUS_RECURSIVE
    :return: List of path items (folders and files)
    """
    page_id = response['DirectoryListing']['pageId']
    tp.info("Page ID", page_id)
    f_list = response['DirectoryListing']['partialListing']['FileStatuses']['FileStatus']
    return [f['pathSuffix'] for f in f_list]


def hdlfs_api(method: str, operation: str) -> dict:
    """
    DECORATOR for all API-calls
    :param method: HTTP-method [get, put, ..]
    :param operation: RESTAPI name
    :return: response of Rest API
    """
    def inner_hdlfs_api(func):
        def call_api(endpoint, certificate, password, verify=True, verbose=False, **kwargs):
            container = re.match(r".+\/\/([^.]+)", endpoint).group(1)
            headers = {'x-sap-filecontainer': container}
            params = {'op': operation}
            endpoint = endpoint.replace('hdlfs://', 'https://') + '/webhdfs/v1/'
            updated = func(endpoint, certificate, password, **kwargs)
            if 'path' in updated and len(updated['path']) > 0 and updated['path'][0] =='/':
                updated['path'] = updated['path'][1:]
            path = updated['path']
            endpoint = endpoint + str(updated.pop('path', ''))
            headers.update(updated.pop('headers', dict()))
            params.update(updated.pop('params', dict()))
            data = updated.pop('data', None)
            suffix = PurePath(certificate).suffix
            if suffix in ['.crt', '.pem']:
                r = requests.request(method, endpoint, cert=(certificate, password), headers=headers, params=params,
                                     data=data, verify=verify)
            elif suffix in ['.pkcs12', '.p12', '.pfx']:
                r = requests_pkcs12.request(method, endpoint, pkcs12_filename=certificate, pkcs12_password=password,
                                            headers=headers, params=params, data=data, verify=verify)
            if verbose:
                tp.print_request_info(method, endpoint, path, headers, params)

            if r.status_code not in [200, 201]:
                raise ValueError(f"Unsuccessful API-call - Status code: {r.status_code} - {r.text}")
            if operation != 'OPEN':
                return json.loads(r.text)
            else:
                return r

        return call_api
    return inner_hdlfs_api


@hdlfs_api(method='get', operation='OPEN')
def open(endpoint: str, certificate: str, password: str, path='',
         offset=0, length=None, noredirect=False, headers={}, verify=True, verbose=False) \
        -> dict:
    """
    Upload file to HDFS using CREATE-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param path: path of file
    :param offset: The starting byte position
    :param length: The number of bytes to be processed.
    :param noredirect: API parameter
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    return {'path': path,
            'params': {'offset': offset, 'length': length, 'noredirect': noredirect},
            'headers': headers}


@hdlfs_api(method='put', operation='CREATE')
def upload(endpoint: str, certificate: str, password: str, destination='', data="", noredirect=False, headers={}, verify=True, verbose=False) \
        -> dict:
    """
    Upload file to HDFS using CREATE-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param destination: destination path of file
    :param data: file content
    :param noredirect: API parameter
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    return {'path': destination,
            'data': data,
            'params': {'noredirect': noredirect},
            'headers': {'Content-Type': 'application/octet-stream'}}


@hdlfs_api(method='put', operation='RENAME')
def rename(endpoint: str, certificate: str, password: str, path='', destination='', headers={}, verify=True, verbose=False) -> dict:
    """
    Rename/Move file in HDFS with RENAME-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param path: path to source file
    :param destination: destination of file
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    destination = '/' + destination if destination[0] != '/' else destination
    return {'path': path,
            'params': {'destination': destination},
            'headers': headers}


@hdlfs_api(method='put', operation='COPY')
def copy(endpoint, certificate, password, path='', destination='', a_sync=False, headers={}, verify=True, verbose=False):
    """
    Copy file in HDFS with Copy-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param path: path to source file
    :param destination: destination of file
    :param a_sync: API parameter
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    destination = '/' + destination if destination[0] != '/' else destination
    return {'path': path,
            'params': {'destination': destination, 'async': a_sync},
            'headers': headers}


@hdlfs_api(method='del', operation='DELETE')
def delete(endpoint: str, certificate: str, password: str, path='', headers={}, verify=True, verbose=False) -> dict:
    """
    Delete file in HDFS with DELETE-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param path: path to source file
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    headers.update({'Content-Type': 'application/json'})
    dt = datetime.isoformat(datetime.utcnow())
    return {'path': path,
            'headers': headers,
            'snapshotname': datetime.isoformat(datetime.utcnow())}


@hdlfs_api(method='get', operation='GETFILESTATUS')
def file_status(endpoint: str, certificate: str, password: str, path='', headers={}, verify=True, verbose=False):
    """
    Get file status
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param path: path to source file
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    headers.update({'Content-Type': 'application/json'})
    return {'path': path,
            'headers': headers}


@hdlfs_api(method='get', operation='LISTSTATUS')
def list_path(endpoint: str, certificate: str, password: str, path='', headers={}, verify=True):
    """
    Get all items of folder by using LISTSTATUS-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param path: path to source file
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    headers.update({'Content-Type': 'application/json'})
    return {'path': path,
            'headers': headers}


@hdlfs_api(method='get', operation='LISTSTATUS_RECURSIVE')
def list_path_recursive(endpoint: str, certificate: str, password: str, path='', start_after=None, headers={},
                        verify=True, verbose=False) -> dict:
    """
    Get all items of folder and sub-folders by using LISTSTATUS_RECURSIVE-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param path: path to source file
    :param start_after: API parameter for paging result
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    headers.update({'Content-Type': 'application/json'})
    return {'path': path,
            'params': {'startAfter': start_after},
            'headers': headers}


@hdlfs_api(method='get', operation='WHOAMI')
def whoami(endpoint: str, certificate: str, password: str, verify=True, verbose=False):
    """
    Get user information by WHOAMI-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param verify: Enables/ disables server verification
    :return: response
    """
    return {'headers': {'Content-Type': 'application/json'}}


# UNTESTED
@hdlfs_api(method='get', operation='GETOPERATIONSTATUS')
def get_operations_status(endpoint: str, certificate: str, password: str, token='',verify=True, verbose=False) -> dict:
    """
    Get operation status by GETOPERATIONSTATUS-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param verify: Enables/ disables server verification
    :return: response
    """
    return {'params': {'token': token},
            'headers': {'Content-Type': 'application/json'}}

# UNTESTED
@hdlfs_api(method='get', operation='GETRESTORESNAPSHOTSTATUS')
def get_operations_status(endpoint, certificate, password, token='', verify=True, verbose=False):
    return {'params': {'token': token},
            'headers': {'Content-Type': 'application/json'}}

