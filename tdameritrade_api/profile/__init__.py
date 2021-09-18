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
