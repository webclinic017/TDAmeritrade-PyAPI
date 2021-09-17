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
    def __repr__(self) -> str:
        return f"(url='{self.url}', port={self.port})"

    def __str__(self) -> str:
        return f"{self.url}:{self.port}"

    # -Class Properties
    url: str
    port: int
