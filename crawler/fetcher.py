import os
import sys
import logging

from web3 import Web3, HTTPProvider

import fetch_util

DIR = sys.path.append(os.path.realpath(os.path.dirname(__file__)))
LOGFIL = "crawler.log"
#LOGFIL = "{}/{}".format(DIR, LOGFIL)
fetch_util.refresh_logger(LOGFIL)
logging.basicConfig(filename=LOGFIL, level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)

class Fetcher(object):

    def __init__(
        self,
        start=True,
        host="",
        delay=0.0001) -> None:

        logging.debug("Starting Crawler")
        self.url = ""
        self.headers = {"content-type": "application/json"}

        self.delay = delay
        self.w3 = Web3(HTTPProvider('https://fabled-bitter-pallet.discover.quiknode.pro/8dc4d68113f456c734f016b4f4f197a657de3b48/'))

        if start:
            self.run()

    def getBlockByNumber(self, n = 'latest'):
        """Get a specific block from the chain and filer the data"""
        data = self.w3.eth.get_block(n)
        logging.info(data)
        block = fetch_util.decodeBlock(data)

    def run(self):
        pass

if __name__ == "__main__":

    f = Fetcher()
    f.getBlockByNumber()