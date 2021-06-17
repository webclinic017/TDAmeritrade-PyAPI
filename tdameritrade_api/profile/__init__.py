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

        # -Instance Methods
        def get_auth_url(self) -> str:
            ''''''
            return (
                "https://auth.tdameritrade.com/auth?response_type=code&"
                f"client_id={self.id}&redirect_uri={self.get_callback_url()}"
            )

        def get_callback_url(self) -> str:
            ''''''
            return f"{self.callback_url[0]}:{self.callback_url[1]}"
