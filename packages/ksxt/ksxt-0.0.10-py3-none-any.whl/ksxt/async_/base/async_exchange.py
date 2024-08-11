import asyncio
import aiohttp
import json
import os
import platform
import tomllib
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Literal, Optional

import yarl

from ksxt.async_.base.throttler import Throttler
from ksxt.base.errors import NotSupportedError
from ksxt.base.rest_exchange import RestExchange
from ksxt.config import CONFIG_DIR
import ksxt.models


class AsyncExchange(RestExchange):
    synchronous = False

    def __init__(self, config: Dict = None, filename: str = None):
        super().__init__(config, filename)

        self.asyncio_loop = asyncio.get_event_loop()
        self.session = aiohttp.ClientSession()
        self.throttle = Throttler({}, self.asyncio_loop)

    async def initialize(self):
        if self.asyncio_loop is None:
            self.asyncio_loop = asyncio.get_event_loop()
        if self.session is None:
            self.session = aiohttp.ClientSession()
        if self.throttle is None:
            self.throttle = Throttler({}, self.asyncio_loop)

    async def close(self):
        if self.session:
            await self.session.close()
            self.session = None

    async def __aenter__(self):
        await self.initialize()
        return self

    async def __aexit__(self, *args):
        await self.close()

    def _get_api_from_file(self, filename: str):
        if filename is None:
            tr_config_filename = "tr_dev.json" if self.is_dev else "tr_app.json"
        else:
            tr_config_filename = filename

        config_path = os.path.join(CONFIG_DIR, tr_config_filename)

        if Path(tr_config_filename).suffix == ".json":
            with open(
                config_path,
                encoding="utf-8",
            ) as f:
                c = json.load(f)
                return {"apis": c[self.name]}

        elif Path(tr_config_filename).suffix == ".toml":
            with open(config_path, mode="rb") as f:
                c = tomllib.load(f)
                return c

    async def fetch(self, url, method="GET", headers=None, body=None, params=None):
        request_headers = headers
        request_body = str(body).encode() if body else None
        request_params = params

        session_method = getattr(self.session, method.lower())

        try:
            async with session_method(
                url,
                # yarl.URL(url, encoded=True),
                headers=request_headers,
                data=request_body,
                params=request_params,
                timeout=aiohttp.ClientTimeout(total=int(self.timeout / 1000)),
            ) as response:
                http_response = await response.text(errors="replace")
                json_response = self.parse_json(http_response)
                return json_response
        except asyncio.TimeoutError as e:
            details = f"{self.id} {method} {url}"
            raise TimeoutError(details) from e

    async def fetch2(
        self, path, security_type, params={}, headers: Optional[Any] = None, body: Optional[Any] = None, config={}
    ):
        is_activate = self.apis[self.type][security_type][path]["activate"]
        if not is_activate:
            return {
                "response": {
                    # 성공 실패 여부
                    "success": "-1",
                    # 응답코드
                    "code": "fail",
                    # 응답메세지
                    "message": f"지원하지 않는 함수({path}) 입니다.",
                }
            }

        # if self.enableRateLimit:
        #     cost = self.calculate_rate_limiter_cost(api, method, path, params, config)
        #     self.throttle(cost)

        # self.lastRestRequestTimestamp = self.milliseconds()

        method_type = self.apis[self.type][security_type][path]["method"]
        api_type = self.apis[self.type][security_type][path]["api"]
        request = self.sign(path, security_type, method_type, api_type, headers, body, params, config)
        return await self.fetch(
            request["url"], request["method"], request["headers"], request["body"], request["params"]
        )

    # region base method
    async def fetch_markets(self, market_name: str) -> ksxt.models.KsxtMarketResponse:
        raise NotSupportedError(f"{self.id} {self.fetch_markets.__qualname__}() is not supported yet.")

    async def fetch_security(self, symbol: str, base_market: str = "KRW") -> ksxt.models.KsxtSecurityResponse:
        raise NotSupportedError(f"{self.id} {self.fetch_security.__qualname__}() is not supported yet.")

    async def fetch_ticker(self, symbol: str, base_market: str = "KRW") -> ksxt.models.KsxtTickerResponse:
        raise NotSupportedError(f"{self.id} {self.fetch_ticker.__qualname__}() is not supported yet.")

    async def fetch_orderbook(self, symbol: str, base_market: str = "KRW") -> ksxt.models.KsxtSingleOrderBookResponse:
        raise NotSupportedError(f"{self.id} {self.fetch_orderbook.__qualname__}() is not supported yet.")

    async def fetch_historical_data(
        self,
        symbol: str,
        time_frame: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        base_market: str = "KRW",
    ) -> ksxt.models.KsxtHistoricalDataResponse:
        raise NotSupportedError(f"{self.id} {self.fetch_historical_data.__qualname__}() is not supported yet.")

    async def fetch_is_holiday(self, dt: datetime, base_market: str = "KRW"):
        raise NotSupportedError(f"{self.id} {self.fetch_is_holiday.__qualname__}() is not supported yet.")

    async def fetch_user_info(self, base_market: str = "KRW"):
        raise NotSupportedError(f"{self.id} {self.fetch_user_info.__qualname__}() is not supported yet.")

    async def fetch_balance(self, acc_num: str, base_market: str = "KRW") -> ksxt.models.KsxtBalanceResponse:
        raise NotSupportedError(f"{self.id} {self.fetch_balance.__qualname__}() is not supported yet.")

    async def fetch_cash(self, acc_num: str, base_market: str = "KRW") -> ksxt.models.KsxtCashResponse:
        raise NotSupportedError(f"{self.id} {self.fetch_cash.__qualname__}() is not supported yet.")

    async def fetch_screener_list(self, base_market: str = "KRW"):
        raise NotSupportedError(f"{self.id} {self.fetch_screener_list.__qualname__}() is not supported yet.")

    async def fetch_screener(self, screen_id: str, base_market: str = "KRW"):
        raise NotSupportedError(f"{self.id} {self.fetch_screener.__qualname__}() is not supported yet.")

    async def fetch_deposit_history(
        self, acc_num: str, base_market: str = "KRW"
    ) -> ksxt.models.KsxtDepositHistoryResponse:
        raise NotSupportedError(f"{self.id} {self.fetch_deposit_history.__qualname__}() is not supported yet.")

    async def fetch_withdrawal_history(
        self, acc_num: str, base_market: str = "KRW"
    ) -> ksxt.models.KsxtWithdrawalHistoryResponse:
        raise NotSupportedError(f"{self.id} {self.fetch_withdrawal_history.__qualname__}() is not supported yet.")

    async def create_order(
        self,
        acc_num: str,
        symbol: str,
        ticket_type: Literal["EntryLong", "EntryShort", "ExitLong", "ExitShort"],
        otype: Literal["limit", "market"],
        price: Optional[float] = 0,
        qty: Optional[float] = 0,
        amount: Optional[float] = 0,
        base_market: str = "KRW",
    ) -> ksxt.models.KsxtCreateOrderResponse:
        raise NotSupportedError(f"{self.id} {self.create_order.__qualname__}() is not supported yet.")

    async def cancel_order(
        self, acc_num: str, order_id: str, symbol: Optional[str] = "", qty: float = 0, *args, base_market: str = "KRW"
    ) -> ksxt.models.KsxtCancelOrderResponse:
        raise NotSupportedError(f"{self.id} {self.cancel_order.__qualname__}() is not supported yet.")

    async def modify_order(
        self,
        acc_num: str,
        order_id: str,
        price: float,
        qty: float,
        *args,
        symbol: Optional[str] = "",
        base_market: str = "KRW",
    ):
        raise NotSupportedError(f"{self.id} {self.modify_order.__qualname__}() is not supported yet.")

    async def fetch_open_order(
        self,
        acc_num: str,
        symbol: Optional[str] = "",
        start: Optional[str] = None,
        end: Optional[str] = None,
        base_market: str = "KRW",
    ) -> ksxt.models.KsxtOpenOrderResponse:
        raise NotSupportedError(f"{self.id} {self.fetch_open_order.__qualname__}() is not supported yet.")

    async def fetch_closed_order(
        self,
        acc_num: str,
        symbol: Optional[str] = "",
        start: Optional[str] = None,
        end: Optional[str] = None,
        base_market: str = "KRW",
    ) -> ksxt.models.KsxtClosedOrderResponse:
        raise NotSupportedError(f"{self.id} {self.fetch_closed_order.__qualname__}() is not supported yet.")

    async def reserve_order(
        self, acc_num: str, symbol: str, price: float, qty: float, target_date: str, base_market: str = "KRW"
    ):
        raise NotSupportedError(f"{self.id} {self.reserve_order.__qualname__}() is not supported yet.")

    # endregion base method

    async def sleep(self, milliseconds):
        return await asyncio.sleep(milliseconds / 1000)
