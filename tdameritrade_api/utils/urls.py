##-----------------------------##
## TDAmeritrade PyAPI          ##
## Written By: Ryan Smith      ##
##-----------------------------##
## URL Endpoints               ##
##-----------------------------##

## Constants
# -Base URLs
base = "https://api.tdameritrade.com/v1/"
# -Authorization Endpoints
# [POST]
auth_oauth = "oauth2/token"  # [POST]
# -Account Endpoints
account_get_by_id = "accounts/{}"  # [GET]
account_get_by_ids = "accounts"    # [GET]
# -Account: Transaction Endpoints
transaction_get_by_id = "accounts/{}/transactions/{}"    # [GET]
transaction_get_by_account = "accounts/{}/transactions"  # [GET]
# -Account: Order Endpoints
order_list = "orders"  # [GET]
# [POST] | [GET]
order_create = order_get_by_account = "accounts/{}/orders"
# [PUT] | [DELETE] | [GET]
order_replace = order_delete = order_get_by_id = "accounts/{}/orders/{}"
# -Account: Saved Order Endpoints
# [PUT] | [DELETE]  | [GET]
so_replace = so_delete = so_get_by_id = "accounts/{}/watchlists/{}"
# [POST] | [GET]
so_create = so_get_by_account = "accounts/{}/savedorders"
# -Account: Watchlist Endpoints
watchlist_list = "accounts/watchlists"  # [GET]
# [POST] | [GET]
watchlist_create = watchlist_get_by_account = "accounts/{}/watchlists"
# [PATCH] | [PUT] | [DELETE] | [GET]
watchlist_update = watchlist_replace = watchlist_delete = watchlist_get_by_id =\
    "accounts/{}/watchlists/{}"
# -Account: User Info & Preference Endpoints
principals_list = "userprincipals"                             # [GET]
subscription_list = "userprincipals/streamersubscriptionkeys"  # [GET]
# [PUT] | [GET]
preference_update = preference_get_by_id = "accounts/{}/preferences"
# -Instrument Endpoints
instrument_list = "instruments"          # [GET]
instrument_get_by_id = "instruments/{}"  # [GET]
# -Market Data: Hour Endpoints
hours_list = "marketdata/hours"          # [GET]
hours_get_by_id = "marketdata/{}/hours"  # [GET]
# -Market Data: Mover Endpoints
mover_get_by_id = "marketdata/{}/movers"  # [GET]
# -Market Data: Quote Endpoints
quote_get_by_id = "marketdata/{}/quotes"  # [GET]
quote_get_by_ids = "marketdata/quotes"    # [GET]
# -Market Data: Option Endpoints
option_list = "marketdata/chains"  # [GET]
# -Market Data: Historical Endpoints
historical_get_by_id = "marketdata/{}/pricehistory"  # [GET]
