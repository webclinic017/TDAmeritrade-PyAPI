##-----------------------------##
## TDAmeritrade PyAPI          ##
## Written By: Ryan Smith      ##
##-----------------------------##
## Profile Class               ##
##-----------------------------##

## Imports
from __future__ import annotations
import asyncio
import json
import urllib
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Union

import aiohttp

from ..utils import urls


## Classes
class Profile:
    """TDAmeritrade Profile"""

    # -Constructor
    def __init__(self, _id: str) -> Profile:
        self.id: str = _id
        self.session: Profile.Session = Profile.Session(_id)

    # -Dunder Methods

    # -Instance Methods
    def to_dict(self) -> dict[str, str]:
        '''Saves the profile to a given file'''
        return {
            'id': self.id,
            'authorization': {
                'token': self.session.refresh_token,
                'expire': self.session.refresh_expiration.strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                'callback': self.session.callback_url
            }
        }

    async def to_file(self, file_path: Union[str, Path]) -> None:
        '''Saves the profile to a given file'''
        # -TODO: Async file handling
        # -TODO: Binary file storage(?)
        _dict = self.to_dict()
        with open(file_path, 'w+') as f:
            json.dump(_dict, f)

    # -Class Methods
    @classmethod
    async def from_file(
        cls, file_path: Union[str, Path], renew_refresh: bool = True
    ) -> Profile:
        '''Loads a profile from the given file. If refresh
        is enabled, will get a new refresh token'''
        # -TODO: Async file handling
        # -TODO: Binary file storage(?)
        # -Load file
        with open(file_path, 'r') as f:
            _dict = json.load(f)
        _cls = cls(_dict['id'])
        _cls.callback_url = _dict['authorization']['callback']
        _cls.session.refresh_token = _dict['authorization']['token']
        _cls.session.refresh_expiration = datetime.strptime(
            _dict['authorization']['expire'], "%Y-%m-%d %H:%M:%S"
        )
        # -Check refresh token time
        if not _cls.session.get_refresh_token_expired():
            # -Renew refresh token
            if renew_refresh:
                await _cls.session.renew_refresh_token()
            else:
                await _cls.session.renew_access_token()
        return _cls

    # -Sub-Classes
    class Session:
        """TDAmeritrade Session"""

        # -Constructor
        def __init__(self, _id: str) -> Profile.Session:
            self.id: str = _id
            self.auto_renew_access: bool = True
            self.auto_renew_refresh: bool = False
            self.authenticated: bool = False
            self.callback_url: Optional[tuple[str, int]] = None
            self.access_expiration: Optional[datetime] = None
            self.refresh_token: Optional[str] = None
            self.refresh_expiration: Optional[datetime] = None
            self.client_session: aiohttp.ClientSession = aiohttp.ClientSession()

        # -Dunder Methods
        def __del__(self) -> None:
            asyncio.get_running_loop().create_task(self.client_session.close())

        # -Instance Methods: Public
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

        def get_access_token_expired(self, delay: Optional[timedelta] = None) -> bool:
            '''Returns true if access token has expired'''
            d = datetime.now()
            if delay:
                return d >= self.access_expiration - delay
            return d >= self.access_expiration

        def get_refresh_token_expired(self, delay: Optional[timedelta] = None) -> bool:
            '''Returns true if refresh token has expired'''
            d = datetime.now()
            if delay:
                return d >= self.refresh_expiration - delay
            return d >= self.refresh_expiration

        async def request_access_token(self, code: str, decode: bool = True) -> bool:
            '''Request access token from authorization code'''
            d = datetime.now()
            payload = self._get_auth_dict(use_refresh=False)
            payload['code'] = urllib.parse.unquote(code) if decode else code
            res = await self.client_session.post(urls.auth_oauth, data=payload)
            if res.status != 200:
                return False
            self.authenticated = True
            res = await res.json()
            # -Expiration of access and refresh token
            self.access_expiration = d + timedelta(seconds=res['expires_in'])
            self.refresh_expiration = d + timedelta(
                seconds=res['refresh_token_expires_in']
            )
            # -Get tokens
            self.client_session.headers.update({
                'AUTHORIZATION': "Bearer " + res['access_token']
            })
            self.refresh_token = res['refresh_token']
            return True

        async def renew_access_token(self) -> bool:
            '''Renew access token from refresh token'''
            d = datetime.now()
            payload = self._get_auth_dict(offline=False)
            res = await self.client_session.post(urls.auth_oauth, data=payload)
            if res.status != 200:
                print(res)
                return False
            self.authenticated = True
            res = await res.json()
            # -Expiration of access token
            self.access_expiration = d + timedelta(seconds=res['expires_in'])
            # -Get token
            self.client_session.headers.update({
                'AUTHORIZATION': "Bearer " + res['access_token']
            })
            return True

        async def renew_refresh_token(self) -> bool:
            '''Renew refresh token from refresh token'''
            d = datetime.now()
            payload = self._get_auth_dict()
            res = await self.client_session.post(urls.auth_oauth, data=payload)
            if res.status != 200:
                return False
            self.authenticated = True
            res = await res.json()
            # -Expiration of access and refresh token
            self.access_expiration = d + timedelta(seconds=res['expires_in'])
            self.refresh_expiration = d + timedelta(
                seconds=res['refresh_token_expires_in']
            )
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
            '''Returns a proper dict for auth requests'''
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
