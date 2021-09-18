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
from asyncio import AbstractEventLoop

import aiohttp

from ..utils.typing import CallbackURL


## Classes
class Session:
    """TDAmeritrade Session"""

    # -Constructor
    def __init__(
        self, id_: str, callback_url: CallbackURL | tuple[str, int], *,
        loop: AbstractEventLoop | None = None, ainit: bool = True
    ) -> Session:
        self.id: str = id_
        if not isinstance(callback_url, CallbackURL):
            callback_url = CallbackURL(*callback_url)
        self.callback_url: CallbackURL = callback_url
        self._loop: AbstractEventLoop = loop if loop else asyncio.get_event_loop()
        self._aiosession: aiohttp.ClientSession | None = None
        self._ready: asyncio.Event = asyncio.Event()
        if ainit:
            self._loop.create_task(self.__ainit__())

    # -Dunder Methods
    async def __ainit__(self) -> None:
        self._aiosession = aiohttp.ClientSession(loop=self._loop, raise_for_status=True)
        self._ready.set()

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
        self._ready.clear()

    async def wait_ready(self) -> None:
        """"""
        await self._ready.wait()

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
    def ready(self) -> bool:
        return self._ready.is_set()


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
