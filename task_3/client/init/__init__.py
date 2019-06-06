from argparse import ArgumentParser

import yaml


def __parse_config():
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', type=str, help='Sets run configuration file')
    return parser.parse_args()


def setup_config():
    host = '0.0.0.0'
    port = 8080
    buffersize = 1024
    encoding = 'utf-8'

    args = __parse_config()
    if args.config:
        with open(args.config) as file:
            config = yaml.load(file, Loader=yaml.Loader)
            host = config.get('host')
            port = config.get('port')

    return host, port, buffersize, encoding
