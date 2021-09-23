#!/usr/bin/python
##-------------------------------##
## TDAmeritrade PyAPI            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## WebSocket Class               ##
##-------------------------------##

## Imports
from __future__ import annotations
from datetime import datetime
from typing import Any

from aiohttp import ClientWebSocketResponse


## Classes
class WebSocket:
    """TDAmeritrade WebSocket"""

    # -Constructor
    def __init__(self, url: str, websocket: ClientWebSocketResponse) -> WebSocket:
        self.url: str = url
        self.id: int | None = None
        self.source: str | None = None
        self.request_counter: int = 0
        self.authenticated: bool = False
        self._aiowebsocket: ClientWebSocketResponse = websocket

    # -Dunder Methods
    def __repr__(self) -> str:
        str_ = f"WebSocket(url={self.url}, authenticated={self.authenticated}"
        return str_ + (f", id={self.id}, source={self.source})" if self.id else ")")

    # -Instance Methods: Private
    def _request_make(
        self, service: str, command: str, params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        ''''''
        dict_ = {
            'service': service,
            'command': command,
            'account': self.id,
            'source': self.source,
            'requestid': self.request_counter
        }
        self.request_counter += 1
        if params:
            dict_['parameters'] = params
        return dict_

    async def _request_send(self, requests: dict[str, Any] | list[dict, Any]) -> None:
        ''''''
        if not isinstance(requests, list):
            requests = [requests]
        await self._aiowebsocket.send_json({
            "requests": requests
        })

    # -Instance Methods: Public
    async def authorize(
        self, id_: int, token: str, company: str, segment: str,
        domain: str, group: str, access: str, datetime_: datetime,
        app_id: str, acl: str
    ) -> None:
        from urllib.parse import urlencode
        self.id = id_
        self.source = app_id
        request = self._request_make(
            "ADMIN", "LOGIN", params={
                'credential': urlencode({
                    'userId': id_,
                    'token': token,
                    'company': company,
                    'segment': segment,
                    'cddomain': domain,
                    'usergroup': group,
                    'accesslevel': access,
                    'authorized': "Y",
                    'timestamp': int(datetime_.timestamp()) * 1000,
                    'appid': app_id,
                    'acl': acl,
                }),
                'token': token,
                'version': WebSocket.get_version_string()
            }
        )
        await self._request_send(request)
        ws_res_dict = (await self.poll_message())[0]
        if ws_res_dict['content']['code'] != 0:
            # throw error
            pass
        self.authenticated = True

    async def close(self) -> None:
        self.authenticated = False
        await self._aiowebsocket.close()

    async def poll_message(self):
        msg = await self._aiowebsocket.receive_json()
        return msg['response']

    async def request(self, immediate: bool = False):
        pass

    # -Static Methods
    @staticmethod
    def get_version_string() -> str:
        return '.'.join(str(i) for i in WebSocket.version)

    # -Class Properties
    version = (1, 0)
