##-----------------------------##
## TDAmeritrade PyAPI          ##
## Written By: Ryan Smith      ##
##-----------------------------##
## Profile Class               ##
##-----------------------------##

## Imports
from __future__ import annotations
import asyncio
import urllib
from datetime import datetime
from pathlib import Path
from typing import Optional, Union

import aiohttp

from ..utils import urls

## Constants


## Functions


## Classes
class Profile:
    """TDAmeritrade Profile"""

    # -Constructor
    def __init__(self, _id: str) -> Profile:
        self.id: str = _id
        self.session: Profile.Session = Profile.Session(_id)

    # -Dunder Methods

    # -Instance Methods

    # -Class Methods

    # -Static Methods

    # -Properties

    # -Class Properties

    # -Sub-Classes
    class Session:
        """TDAmeritrade Session"""

        # -Constructor
        def __init__(self, _id: str) -> Profile.Session:
            self.id: str = _id
            self.callback_url: Optional[tuple[str, int]] = None
            self.access_expiration: Optional[datetime] = None
            self.refresh_token: Optional[str] = None
            self.refresh_expiration: Optional[datetime] = None
            self.client_session: aiohttp.ClientSession = aiohttp.ClientSession()

        # -Dunder Methods
        def __del__(self) -> None:
            asyncio.get_running_loop().create_task(self.client_session.close())

        # -Instance Methods: Public
        def setup(
            self,
            callback_url: tuple[str, int],
            file_path: Optional[Union[str, Path]] = None
        ) -> bool:
            '''Setup session with callback url and optional credentials file'''
            self.callback_url = callback_url

        def get_auth_id(self) -> str:
            '''Returns the authorization ID'''
            return self.id + "@AMER.OAUTHAP"

        def get_auth_url(self) -> str:
            '''Returns the authorization url'''
            return (
                "https://auth.tdameritrade.com/auth?response_type=code&client_id"
                f"={self.get_auth_id()}&redirect_uri={self.get_callback_url()}"
            )

        def get_callback_url(self) -> str:
            '''Returns the callback url as a string'''
            return f"{self.callback_url[0]}:{self.callback_url[1]}"

        async def request_access_token(self, code: str, decode: bool = True) -> bool:
            '''Request access token from authorization code'''
            payload = self._get_auth_dict(use_refresh=False)
            payload['code'] = urllib.parse.unquote(code) if decode else code
            res = await self.client_session.post(urls.auth_oauth, data=payload)
            if res.status != 200:
                return False
            # -TODO: Expiration of access and refresh token
            res = await res.json()
            # -Get tokens
            self.client_session.headers.update({
                'AUTHORIZATION': "Bearer " + res['access_token']
            })
            self.refresh_token = res['refresh_token']
            return True

        async def renew_access_token(self) -> bool:
            '''Renew access token from refresh token'''
            payload = self._get_auth_dict(offline=False)
            res = await self.client_session.post(urls.auth_oauth, data=payload)
            if res.status != 200:
                return False
            # -TODO: Expiration of access token
            res = await res.json()
            # -Get token
            self.client_session.headers.update({
                'AUTHORIZATION': "Bearer " + res['access_token']
            })
            return True

        async def renew_refresh_token(self) -> bool:
            '''Renew refresh token from refresh token'''
            payload = self._get_auth_dict()
            res = await self.client_session.post(urls.auth_oauth, data=payload)
            if res.status != 200:
                return False
            # -TODO: Expiration of access and refresh token
            res = await res.json()
            # -Get tokens
            self.client_session.headers.update({
                'AUTHORIZATION': "Bearer " + res['access_token']
            })
            self.refresh_token = res['refresh_token']
            return True

        # -Instance Methods: Private
        def _get_auth_dict(
            self, *, use_refresh: bool = True, offline: bool = True
        ) -> dict[str, str]:
            ''''''
            _dict = {
                'client_id': self.get_auth_id(),
                'grant_type': "refresh_token" if use_refresh else "authorization_code"
            }
            if offline:
                _dict['access_type'] = "offline"
            if use_refresh:
                _dict['refresh_token'] = self.refresh_token
            else:
                _dict['redirect_uri'] = self.get_callback_url()
            return _dict
