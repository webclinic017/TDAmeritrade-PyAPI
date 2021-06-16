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
auth_oauth = "oauth2/token"  # [POST]
# -Account Endpoints
account_get_by_id = "accounts/{}"  # [GET]
account_get_by_ids = "accounts"    # [GET]
# -Account: Transaction Endpoints
transaction_get_by_id = "accounts/{}/transactions/{}"    # [GET]
transaction_get_by_account = "accounts/{}/transactions"  # [GET]
# -Account: Order Endpoints
order_create = "accounts/{}/orders"          # [POST]
order_replace = "accounts/{}/orders/{}"      # [PUT]
order_delete = "accounts/{}/orders/{}"       # [DELETE]
order_list = "orders"                        # [GET]
order_get_by_id = "accounts/{}/orders/{}"    # [GET]
order_get_by_account = "accounts/{}/orders"  # [GET]
# -Account: Saved Order Endpoints
so_create = "accounts/{}/savedorders"        # [POST]
so_replace = "accounts/{}/savedorders/{}"    # [PUT]
so_delete = "accounts/{}/savedorders/{}"     # [DELETE]
so_get_by_id = "accounts/{}/savedorders/{}"  # [GET]
so_get_by_account = "{}/savedorders"         # [GET]
# -Account: Watchlist Endpoints
watchlist_create = "accounts/{}/watchlists"          # [POST]
watchlist_update = "accounts/{}/watchlists/{}"       # [PATCH]
watchlist_replace = "accounts/{}/watchlists/{}"      # [PUT]
watchlist_delete = "accounts/{}/watchlists/{}"       # [DELETE]
watchlist_list = "accounts/watchlists"               # [GET]
watchlist_get_by_id = "accounts/{}/watchlists/{}"    # [GET]
watchlist_get_by_account = "accounts/{}/watchlists"  # [GET]
# -Account: User Info & Preference Endpoints
principals_list = "userprincipals"                             # [GET]
subscription_list = "userprincipals/streamersubscriptionkeys"  # [GET]
preference_update = "accounts/{}/preferences"                  # [PUT]
preference_get_by_id = "accounts/{}/preferences"               # [GET]
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
