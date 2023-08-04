import argparse


def parse_cli_arguments(desc: str):
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-a', '--host', type=str, default='localhost')
    parser.add_argument('-p', '--port', type=int, default=7777)
    args = parser.parse_args()
    return args
