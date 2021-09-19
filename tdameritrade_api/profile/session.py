#!/usr/bin/python
##-------------------------------##
## TDAmeritrade PyAPI            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Session + WebSocket Classes   ##
##-------------------------------##

## Imports
from __future__ import annotations
import urllib
from datetime import datetime, timedelta, timezone

from aiohttp import ClientResponse, ClientSession

from ..utils import urls
from ..utils.typing import CallbackURL


## Classes
class Session:
    """TDAmeritrade Session"""

    # -Constructor
    def __init__(
        self, id_: str, callback_url: CallbackURL | tuple[str, int]
    ) -> Session:
        self.id: str = id_
        if not isinstance(callback_url, CallbackURL):
            callback_url = CallbackURL(*callback_url)
        self.callback_url: CallbackURL = callback_url
        self.authenticated: bool = False
        self._aiosession: ClientSession = ClientSession(raise_for_status=False)
        self.access_token_expiration: datetime | None = None
        self.refresh_token: str | None = None
        self.refresh_token_expiration: datetime | None = None

    # -Dunder Methods
    def __repr__(self) -> str:
        return (
            f"Session(id='{self.id}', callback_url='{self.callback_url}', "
        )

    # -Instance Methods: Private
    async def _authorization_update(self, res: ClientResponse) -> dict[str, str]:
        '''Updates Session authorization fields'''
        datetime_ = datetime.now(timezone.utc)
        res_dict = await res.json()
        self.authenticated = True
        self._aiosession.headers.update({
            'AUTHORIZATION': "Bearer " + res_dict['access_token']
        })
        self.access_token_expiration = datetime_ + timedelta(
            seconds=res_dict['expires_in']
        )
        if 'refresh_token' in res_dict:
            self.refresh_token = res_dict['refresh_token']
            self.refresh_token_expiration = datetime_ + timedelta(
                seconds=res_dict['refresh_token_expires_in']
            )

    # -Instance Methods: Public
    async def close(self) -> None:
        self.authenticated = False
        if self._aiosession:
            await self._aiosession.close()

    async def renew_tokens(self, refresh_token: bool = False) -> None:
        if 'AUTHORIZATION' in self._aiosession.headers:
            del self._aiosession.headers['AUTHORIZATION']
        payload = {
            'client_id': self.authentication_id,
            'grant_type': "refresh_token",
            'refresh_token': self.refresh_token,
        }
        if refresh_token:
            payload['access_type'] = "offline"
        res = await self._aiosession.post(urls.auth_oauth, data=payload)
        await self._authorization_update(res)

    async def request_tokens(self, code: str, *, decode: bool = True) -> None:
        res = await self._aiosession.post(
            urls.auth_oauth,
            data={
                'client_id': self.authentication_id,
                'grant_type': "authorization_code",
                'access_type': "offline",
                'redirect_uri': str(self.callback_url),
                'code': urllib.parse.unquote(code) if decode else code,
            }
        )
        await self._authorization_update(res)

    # -Properties
    @property
    def authentication_id(self) -> str:
        return self.id + "@AMER.OAUTHAP"

    @property
    def authentication_url(self) -> str:
        return (
            "https://auth.tdameritrade.com/auth?response_type=code&client_id="
            f"{self.authentication_id}&redirect_uri={self.callback_url}"
        )

    @property
    def access_token_duration(self) -> timedelta:
        return self.access_token_expiration - datetime.now(timezone.utc)

    @property
    def access_token_expired(self) -> bool:
        return datetime.now(timezone.utc) >= self.access_token_expiration

    @property
    def refresh_token_duration(self) -> timedelta:
        return self.refresh_token_expiration - datetime.now(timezone.utc)

    @property
    def refresh_token_expired(self) -> bool:
        return datetime.now(timezone.utc) >= self.refresh_token_expiration


class WebSocket:
    """TDAmeritrade WebSocket"""

    # -Constructor
    def __init__(self) -> WebSocket:
        pass

    # -Dunder Methods

    # -Instance Methods

    # -Class Methods

    # -Static Methods

    # -Properties

    # -Class Properties

    # -Sub-Classes
