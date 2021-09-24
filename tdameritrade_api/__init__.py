#!/usr/bin/python
##-------------------------------##
## TDAmeritrade PyAPI            ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
from .profile import Profile
from .session import Session
from .websocket import WebSocket

## Constants
__author__ = "Ryan Smith"
__title__ = "TDAmeritrade PyAPI"
__version__ = (1, 0, 0)
__all__ = [
    Profile, Session, WebSocket
]


## Functions
def get_version_string() -> str:
    """Returns project version as a string"""
    return '.'.join([str(i) for i in __version__])
