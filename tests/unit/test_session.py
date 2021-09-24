#!/usr/bin/python
##-------------------------------##
## TDAmeritrade PyAPI            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Session Class: Testing        ##
##-------------------------------##

## Imports
import unittest
from unittest import mock

import aiohttp

from tdameritrade_api.session import Session
from tdameritrade_api.utils.typing import CallbackURL


## Classes
class Test_Session(unittest.IsolatedAsyncioTestCase):

    # -Instance Methods
    async def asyncSetUp(self) -> None:
        self.session_01 = Session("ID-01", ("http://localhost", 0))
        self.session_02 = Session("ID-02", ("http://custom_url.com", 0))
        self.mock_auth_update = mock.patch(
            'tdameritrade_api.session.Session._authorization_update'
        )

    async def asyncTearDown(self) -> None:
        await self.session_01.close()
        await self.session_02.close()

    def test_ids(self) -> None:
        self.assertEqual(self.session_01.id, "ID-01")
        self.assertEqual(self.session_02.id, "ID-02")
        self.assertEqual(self.session_01.authentication_id, "ID-01@AMER.OAUTHAP")
        self.assertEqual(self.session_02.authentication_id, "ID-02@AMER.OAUTHAP")

    async def test_renew_tokens(self) -> None:
        pass

    async def test_request_tokens(self) -> None:
        pass

    def test_urls(self) -> None:
        self.assertEqual(
            self.session_01.callback_url,
            CallbackURL(url="http://localhost", port=0)
        )
        self.assertEqual(
            self.session_02.callback_url,
            CallbackURL(url="http://custom_url.com", port=0)
        )
        self.assertEqual(
            self.session_01.authentication_url,
            ("https://auth.tdameritrade.com/auth?response_type=code&client_id="
             "ID-01@AMER.OAUTHAP&redirect_uri=http://localhost:0")
        )
        self.assertEqual(
            self.session_02.authentication_url,
            ("https://auth.tdameritrade.com/auth?response_type=code&client_id="
             "ID-02@AMER.OAUTHAP&redirect_uri=http://custom_url.com:0")
        )


## Body
if __name__ == "__main__":
    unittest.main()
