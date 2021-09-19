#!/usr/bin/python
##-------------------------------##
## TDAmeritrade PyAPI            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Session + WebSocket Classes   ##
##-------------------------------##

## Imports
from __future__ import annotations
import asyncio

from aiohttp import ClientSession

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
        self._aiosession: ClientSession = ClientSession(raise_for_status=True)

    # -Dunder Methods
    def __repr__(self) -> str:
        return (
            f"Session(id='{self.id}', callback_url='{self.callback_url}', "
            f"ready={self._ready.is_set()})"
        )

    # -Instance Methods: Private

    # -Instance Methods: Public
    async def close(self) -> None:
        if self._aiosession:
            await self._aiosession.close()

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
