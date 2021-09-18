#!/usr/bin/python
##-------------------------------##
## TDAmeritrade PyAPI            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Type Hinting Classes          ##
##-------------------------------##

## Imports
from typing import NamedTuple


## Classes
class CallbackURL(NamedTuple):
    """Callback URL Type Hint"""

    # -Dunder Methods
    def __str__(self) -> str:
        return f"{self.url}:{self.port}"

    # -Properties
    url: str
    port: int
