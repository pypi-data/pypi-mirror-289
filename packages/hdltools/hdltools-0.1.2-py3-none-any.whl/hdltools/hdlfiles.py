import argparse
import json
from pathlib import Path

try:
    import termprint as tp
    import hdlfsapi as hdl
except (ModuleNotFoundError, ImportError):
    import hdltools.termprint as tp
    import hdltools.hdlfsapi as hdl

HDLFSCONFIGFILE = ".hdlfscli.config.json"


class HDLConnect:
    
    def __init__(self, url: str, cert: str, key: str) :
        self.url = url
        self.certificate = cert
        self.key = key


def main() :

    parser = argparse.ArgumentParser("HDL Files command line")
    parser.add_argument("config", help='Config of hdlfscli.config.json-file')
    parser.add_argument("action", choices=['ls'], help=f"Command for \'target\'-argument")
    parser.add_argument("-p", "--path",help=f"Path (default='/')", default='/')
    parser.add_argument("-v", "--verbose", help="Print http-request details", action="store_true")

    args = parser.parse_args()

    with open(Path.home() / HDLFSCONFIGFILE  ) as fp:
        hdlfs_params = json.load(fp)["configs"][args.config]

    client = HDLConnect(hdlfs_params['endpoint'], hdlfs_params['cert'], hdlfs_params['key'])

    resp = hdl.list_path(client.url, client.certificate, client.key,path=args.path, verbose=args.verbose)
    content = hdl.get_path_content(resp)

    tp.bullet_list(content,title=f"file content of: {args.path}")


if __name__ == '__main__':
    main()