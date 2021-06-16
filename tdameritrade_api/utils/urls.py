##-----------------------------##
## TDAmeritrade PyAPI          ##
## Written By: Ryan Smith      ##
##-----------------------------##
## URL Endpoints               ##
##-----------------------------##

## Imports
from typing import Optional

## Constants
# -Base URLs
base = "https://api.tdameritrade.com/v1/"
base_account = base + "accounts"
base_market = base + "marketdata/"
# -Authorization Endpoints
auth_oauth = base + "oauth2/token"  # [POST]
# -Account: User Info & Preference Endpoints
preference_by_id = base_account + "/{}/preferences"  # [GET] | [PUT]
# -Market Data: Mover Endpoints
mover_by_id = base_market + "{}/movers"  # [GET]
# -Market Data: Option Endpoints
option_list = base_market + "chains"  # [GET]
# -Market Data: Historical Endpoints
historical_by_id = base_market + "{}/pricehistory"  # [GET]


## Functions
def get_account_endpoint(_id: Optional[int] = None) -> str:
    """Returns the account endpoint url depending on ID"""
    return base_account + (f"/{_id}" if _id else "")


def get_principals_endpoint(subscription: bool = False) -> str:
    """Returns the principals endpoint url depending on subscription bool"""
    return (base + "userprincipals"
           + ("/streamersubscriptionkeys" if subscription else ""))


def get_transaction_endpoint(id1: int, id2: Optional[int] = None) -> str:
    """Returns the transaction endpoint url depending on IDs"""
    return base_account + f"/{id1}/transactions" + (f"/{id2}" if id2 else "")


def get_watchlist_endpoint(id1: Optional[int] = None, id2: Optional[int] = None) -> str:
    """Returns the watchlist endpoint url depending on IDs"""
    return (base_account + (f"/{id1}" if id1 else "")
           + "/watchlists" + (f"/{id2}" if id2 else ""))


def get_orders_endpoint(id1: Optional[int] = None, id2: Optional[int] = None) -> str:
    """Returns the orders endpoint url depending on IDs"""
    return ((base_account + f"/{id1}/" if id1 else base)
           + "orders" + (f"/{id2}" if id2 else ""))


def get_saved_orders_endpoint(id1: int, id2: Optional[int] = None) -> str:
    """Returns the saved orders endpoint url depending on IDs"""
    return base_account + f"/{id1}/savedorders" + (f"/{id2}" if id2 else "")


def get_instrument_endpoint(_id: Optional[str] = None) -> str:
    """Returns the instrument endpoint url depending on ID"""
    return base + "instruments" + (f"/{_id}" if _id else "")


def get_market_hours_endpoint(_id: Optional[str] = None) -> str:
    """Returns the market hours endpoint url depending on ID"""
    return base_market + (f"{_id}/" if _id else "") + "hours"


def get_market_quote_endpoint(_id: Optional[str] = None) -> str:
    """Returns the market quotes endpoint url depending on ID"""
    return base_market + (f"{_id}/" if _id else "") + "quotes"
