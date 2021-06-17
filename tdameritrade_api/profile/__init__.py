##-----------------------------##
## TDAmeritrade PyAPI          ##
## Written By: Ryan Smith      ##
##-----------------------------##
## Profile Class               ##
##-----------------------------##

## Imports
from __future__ import annotations
import asyncio
from typing import Optional

import aiohttp

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
            self.access_token: Optional[str] = None
            self.refresh_token: Optional[str] = None
            self.client_session: aiohttp.ClientSession = aiohttp.ClientSession()

        # -Dunder Methods
        def __del__(self) -> None:
            asyncio.get_running_loop().create_task(self.client_session.close())

        # -Instance Methods
        def get_auth_id(self) -> str:
            '''Returns the auth ID'''
            return self.id + "@AMER.OAUTHAP"

        def get_auth_url(self) -> str:
            '''Returns the auth url'''
            return (
                "https://auth.tdameritrade.com/auth?response_type=code&client_id"
                f"={self.get_auth_id()}&redirect_uri={self.get_callback_url()}"
            )

        def get_callback_url(self) -> str:
            '''Returns the callback url as a string'''
            return f"{self.callback_url[0]}:{self.callback_url[1]}"
