#!/usr/bin/python
##-------------------------------##
## TDAmeritrade PyAPI            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Profile Class                 ##
##-------------------------------##

## Imports
from __future__ import annotations

from .session import Session, WebSocket
from ..utils import urls

## Constants
__all__ = [
    "Profile", Session, WebSocket
]


## Classes
class Profile:
    """TDAmeritrade Profile"""

    # -Constructor
    def __init__(self, session: Session) -> Profile:
        self._session: Session = session

    # -Instance Methods
    async def me(
        self, *, preferences: bool = True, surrogates: bool = True,
        streamer_info: bool = True, streamer_keys: bool = True
    ) -> dict[str, str]:
        '''Profile details'''
        fields = []
        if preferences:
            fields.append("preferences")
        if surrogates:
            fields.append("surrogateIds")
        if streamer_info:
            fields.append("streamerConnectionInfo")
        if streamer_keys:
            fields.append("streamerSubscriptionKeys")
        return await self._session.get(urls.user_principals, params={
            'fields': ','.join(fields)
        })
