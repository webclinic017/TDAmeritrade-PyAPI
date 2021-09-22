#!/usr/bin/python
##-----------------------------##
## TDAmeritrade PyAPI          ##
## Written By: Ryan Smith      ##
##-----------------------------##
## URL Endpoints               ##
##-----------------------------##

## Imports
from __future__ import annotations

## Constants
# -Base URLs
base = "https://api.tdameritrade.com/v1/"
# -Authorization
auth_oauth = base + "oauth2/token"
# -Account
base_account = base + "accounts"
# -User Principals
user_principals = base + "userprincipals"
user_subscription = user_principals + "/streamersubscriptionkeys"


## Functions
def account_id(id_: int, preferences: bool = False) -> str:
    """Returns account endpoint based on parameters"""
    return f"{base_account}/{str(id_)}" + ("/preferences" if preferences else "")
