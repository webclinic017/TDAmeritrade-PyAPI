#!/usr/bin/python
##-------------------------------##
## TDAmeritrade PyAPI            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## WebSocket Class: Testing      ##
##-------------------------------##

## Imports
import unittest
import unittest.mock

from tdameritrade_api.websocket import WebSocket


## Classes
class Test_WebSocket(unittest.IsolatedAsyncioTestCase):

    # -Instance Methods
    async def asyncSetUp(self):
        pass

    async def asyncTearDown(self):
        pass


## Body
if __name__ == "__main__":
    unittest.main()
