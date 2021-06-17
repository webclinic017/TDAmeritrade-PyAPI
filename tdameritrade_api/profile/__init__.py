##-----------------------------##
## TDAmeritrade PyAPI          ##
## Written By: Ryan Smith      ##
##-----------------------------##
## Profile Class               ##
##-----------------------------##

## Imports
from __future__ import annotations

## Constants


## Functions


## Classes
class Profile:
    """"""

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
        """"""

        # -Constructor
        def __init__(self, _id: str) -> Profile.Session:
            self.id: str = _id + "@AMER.OAUTHAP"
            self.callback_url: tuple[str, int]


## Body
