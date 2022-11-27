import os
import sys
import logging

from web3 import Web3, HTTPProvider

from crawler.fetch_util import *

DIR = sys.path.append(os.path.realpath(os.path.dirname(__file__)))
LOGFIL = "crawler.log"
#LOGFIL = "{}/{}".format(DIR, LOGFIL)
refresh_logger(LOGFIL)
logging.basicConfig(filename=LOGFIL, level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)

class Fetcher(object):

    def __init__(
        self,
        block_num=0,
        start=True,
        APIKey = '8dc4d68113f456c734f016b4f4f197a657de3b48',
        host="https://fabled-bitter-pallet.discover.quiknode.pro/",
        delay=0.0001) -> None:

        #logging.debug("Init Crawler")
        self.url = "{}{}".format(host, APIKey)
        self.headers = {"content-type": "application/json"}
        self.delay = delay

        self.w3 = Web3(HTTPProvider(self.url))

        if start:
            self.block_detail = self.getBlockByNumber(block_num)
            self.run()

    def getBlockByNumber(self, n, txfull=False):
        """Get a specific block from the chain and filer the data"""
        data = self.w3.eth.get_block(n)
        #logging.info(data)
        #block = fetch_util.decodeBlock(data)
        return data

    def run(self):
        """
        Run the process
        """

        logging.debug("Start to request quick node to fetch block")
        logging.info("wanted block details: {}".format(self.block_detail))

        print("Done!\n")


if __name__ == "__main__":

    f = Fetcher()
