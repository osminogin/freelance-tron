#!/usr/bin/env python3
import os
import sys
import logging

from tronapi import Tron

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

def main():
    full_node = os.getenv('FULLNODE_URL', 'http://tron-fullnode:8090')
    solidity_node = os.getenv('SOLIDITY_URL', 'http://tron-fullnode:8091')
    # full_node = 'https://api.trongrid.io'
    # solidity_node = 'https://api.trongrid.io'
    # event_server = 'https://api.trongrid.io'

    logger.debug(f'Trying connect to {full_node}, {solidity_node}')
    
    tron = Tron(
        full_node=full_node,
        solidity_node=solidity_node,
        # event_server=event_server)
    )

    assert tron.is_connected(), "API connection required"

    # API calls
    test_account = tron.create_account
    current_block = tron.trx.get_block('latest')
    node_info = tron.trx.get_node_info()

    # Dumps some data
    logger.info('Node Info: %s', node_info)
    logger.info('Block Data: %s', current_block)

    logger.info('New Account generated!')

    logger.info('Private Key: %s',  test_account.private_key)
    logger.info('Public Key: %s', test_account.public_key)
    logger.info('Address: %s', test_account.address.base58)

if __name__ == '__main__':
    main()
