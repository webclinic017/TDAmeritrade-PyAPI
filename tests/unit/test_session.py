#!/usr/bin/python
##-------------------------------##
## TDAmeritrade PyAPI            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Session Class: Testing        ##
##-------------------------------##

## Imports
import unittest

from tdameritrade_api.session import Session
from tdameritrade_api.utils.typing import CallbackURL


## Classes
class Test_Session(unittest.IsolatedAsyncioTestCase):

    # -Instance Methods
    async def asyncSetUp(self) -> None:
        # -Tuple Creation
        self.sessions: list[Session] = [
            Session(f"ID-{id_ + 1:03d}", (url, port))
            for id_, (url, port) in enumerate(zip(
                ("https://localhost", "https://www.valid-url.com"),
                (8080, 14891)
            ))
        ]
        # -CallbackURL Creation
        self.sessions.extend(
            Session(f"ID-{id_ + 3:03d}", CallbackURL(url, port))
            for id_, (url, port) in enumerate(zip(
                ("http://my_custom_url.com", "http://invalid-url.org"),
                (9866, 0)
            ))
        )
        self.s1, self.s2, self.s3, self.s4 = self.sessions

    async def asyncTearDown(self) -> None:
        for session in self.sessions:
            await session.close()

    def test_authentication_ids(self) -> None:
        self.assertEqual(self.s1.authentication_id, "ID-001@AMER.OAUTHAP")
        self.assertEqual(self.s2.authentication_id, "ID-002@AMER.OAUTHAP")
        self.assertEqual(self.s3.authentication_id, "ID-003@AMER.OAUTHAP")
        self.assertEqual(self.s4.authentication_id, "ID-004@AMER.OAUTHAP")

    def test_authentication_urls(self) -> None:
        self.assertEqual(
            self.s1.authentication_url,
            ("https://auth.tdameritrade.com/auth?response_type=code&client_id="
             "ID-001@AMER.OAUTHAP&redirect_uri=https://localhost:8080")
        )
        self.assertEqual(
            self.s2.authentication_url,
            ("https://auth.tdameritrade.com/auth?response_type=code&client_id="
             "ID-002@AMER.OAUTHAP&redirect_uri=https://www.valid-url.com:14891")
        )
        self.assertEqual(
            self.s3.authentication_url,
            ("https://auth.tdameritrade.com/auth?response_type=code&client_id="
             "ID-003@AMER.OAUTHAP&redirect_uri=http://my_custom_url.com:9866")
        )
        self.assertEqual(
            self.s4.authentication_url,
            ("https://auth.tdameritrade.com/auth?response_type=code&client_id="
             "ID-004@AMER.OAUTHAP&redirect_uri=http://invalid-url.org:0")
        )

    def test_ids(self) -> None:
        self.assertEqual(self.s1.id, "ID-001")
        self.assertEqual(self.s2.id, "ID-002")
        self.assertEqual(self.s3.id, "ID-003")
        self.assertEqual(self.s4.id, "ID-004")

    def test_urls(self) -> None:
        self.assertIsInstance(self.s1.callback_url, CallbackURL)
        self.assertIsInstance(self.s2.callback_url, CallbackURL)
        self.assertIsInstance(self.s3.callback_url, CallbackURL)
        self.assertIsInstance(self.s4.callback_url, CallbackURL)
        self.assertEqual(
            self.s1.callback_url,
            CallbackURL(url="https://localhost", port=8080)
        )
        self.assertEqual(
            self.s2.callback_url,
            CallbackURL(url="https://www.valid-url.com", port=14891)
        )
        self.assertEqual(
            self.s3.callback_url,
            CallbackURL(url="http://my_custom_url.com", port=9866)
        )
        self.assertEqual(
            self.s4.callback_url,
            CallbackURL(url="http://invalid-url.org", port=0)
        )


## Body
if __name__ == "__main__":
    unittest.main()
