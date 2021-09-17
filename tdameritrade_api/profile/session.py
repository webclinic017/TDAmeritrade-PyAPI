#!/usr/bin/python
##-------------------------------##
## TDAmeritrade PyAPI            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Session + WebSocket Classes   ##
##-------------------------------##

## Imports
from __future__ import annotations
from ..utils.typing import CallbackURL

## Variables


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

    # -Dunder Methods
    def __repr__(self) -> str:
        return f"Session(id='{self.id}', callback_url={repr(self.callback_url)})"

    # -Instance Methods

    # -Class Methods

    # -Static Methods

    # -Properties

    # -Class Properties

    # -Sub-Classes


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
