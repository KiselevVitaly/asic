import socket
import select
import argparse

from asinc_chat.services.parse_cli_arguments import parse_cli_arguments
from asinc_chat.services.JIMProtocol import MessageBuilder
from asinc_chat.services.log_decorator import Log

BLOCK_LEN: int = 1024
EOM: bytes = b'ENDOFMESSAGE___'
ENCODING_ = 'utf-8'
