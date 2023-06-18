import socket
import select
import argparse

from services.parse_cli_arguments import parse_cli_arguments
from services.JIMProtocol import MessageBuilder

BLOCK_LEN: int = 1024
EOM: bytes = b'ENDOFMESSAGE___'
ENCODING_ = 'utf-8'
