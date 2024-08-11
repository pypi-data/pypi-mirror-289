from datetime import datetime, timedelta
import json
import os
import time
from typing import Any, Dict, Optional
from ksxt.api.koreainvest import ImplicitAPI
from ksxt.async_.base.async_exchange import AsyncExchange
from ksxt.market.manager import MarketManager
from ksxt.parser.koreainvest import KoreaInvestParser


class KoreaInvest(AsyncExchange, ImplicitAPI):
    def __init__(self, config: Dict = None) -> None:
        super().__init__(config, "koreainvest.toml")
        self.parser = KoreaInvestParser()

    def safe_symbol(self, base_market: str, security: str) -> str:
        return f"{security}"

    def is_activate(self, path, security_type) -> bool:
        mode = "dev" if self.is_dev == True else "app"

        tr_id = self.apis[self.type][security_type][path][mode]["tr_id"]

        if not bool(tr_id):
            return False

        return super().is_activate(path=path, security_type=security_type)

    @AsyncExchange.check_token
    def sign(
        self,
        path,
        security_type,
        method_type,
        api_type: Any = "public",
        headers: Optional[Any] = None,
        body: Optional[Any] = None,
        params: Optional[Any] = None,
        config={},
    ):
        mode = "dev" if self.is_dev == True else "app"

        host_url = self.apis[self.type][mode]["hostname"]
        destination = self.apis[self.type][security_type][path]["url"]
        version = self.apis[self.type]["version"]
        params["version"] = version
        destination = self.implode_params(destination, params)

        url = host_url + "/" + destination

        tr_id = self.apis[self.type][security_type][path][mode]["tr_id"]
        authorization_token = f"Bearer {self.token}"
        custtype = ""
        if "custtype" in self.apis[self.type][security_type][path]:
            custtype = self.apis[self.type][security_type][path]["custtype"]

        if headers is None:
            headers = {}
            headers.update(
                {
                    "content-type": "application/json",
                    "authorization": authorization_token,
                    "appkey": self.open_key,
                    "appsecret": self.secret_key,
                    "tr_id": tr_id,
                    "custtype": custtype,
                }
            )

        if method_type.upper() == "POST":
            body = json.dumps(params)
            params = {}

        return {"url": url, "method": method_type, "headers": headers, "body": body, "params": params}

    # region _____
    def create_token(self):
        import logging

        mode = "dev" if self.is_dev == True else "app"
        host_url = self.apis[self.type][mode]["hostname"]
        destination = self.apis[self.type]["token"]["url"]
        url = host_url + "/" + destination

        request_headers = self.prepare_request_headers()

        body = {"grant_type": "client_credentials", "appkey": self.open_key, "appsecret": self.secret_key}

        body = json.dumps(body, separators=(",", ":"))

        try:
            res = self.fetch(url=url, method="POST", headers=request_headers, body=body)
        except Exception as ex:
            logging.error(ex)
            return

        if "access_token" in res.keys():
            token = res["access_token"]
            token_expired = res["access_token_token_expired"]
            self.save_token(self.open_key, token, token_expired)
        else:
            logging.error(res["error_description"])

    def get_response(self, result, request_params: dict):
        if self.safe_string(result, "rt_cd") == "0":
            response = self.get_success_response(result)
        else:
            response = self.get_error_response(result)

        response = self.update_header(response, request_params)
        return response

    def get_success_response(self, result):
        return super().get_success_response(
            # 성공 실패 여부
            response_code="0",
            # 응답 코드
            msg_code=self.safe_string(result, "msg_cd"),
            # 응답 메세지
            msg=self.safe_string(result, "msg1"),
            # 원본 데이터
            org_data=result,
        )

    def get_error_response(self, result):
        return super().get_error_response(
            error_code=self.safe_string(result, "msg_cd"),
            error_message=self.safe_string(result, "msg1"),
            org_data=result,
        )

    def update_header(self, response: dict, request_params: dict):
        response = self.update_success_response_header(
            response, {"request_time": time.time(), "request_params": request_params}
        )
        return response

    # endregion ____

    # region public feeder
    @AsyncExchange.check_token
    async def fetch_markets(self, market_name: str):
        db_path = os.path.join(os.getcwd(), f".ksxt-cache_market.{datetime.now().strftime('%Y%m%d')}.db")
        manager = MarketManager(db_path=db_path)
        manager._init()
        if market_name.lower() == "kospi":
            result = manager.kospi.all()
            base_market = "KRW"
        elif market_name.lower() == "kosdaq":
            result = manager.kosdaq.all()
            base_market = "KRW"
        elif market_name.lower() == "nyse":
            result = manager.nyse.all()
            base_market = "USD"
        elif market_name.lower() == "nasdaq":
            result = manager.nasdaq.all()
            base_market = "USD"
        elif market_name.lower() == "amex":
            result = manager.amex.all()
            base_market = "USD"
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{market_name} market is not yet supported."
            )

        params = {}
        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_markets(response=response, base_market=base_market)

    async def fetch_trade_fee(self, symbol: Optional[str] = "", base_market: str = "KRW"):
        params = {"base_market": base_market}

        result = {"rt_cd": "0", "output": {}}
        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_trade_fee(response, base_market)

    async def fetch_ticker(self, symbol: str, base_market: str = "KRW"):
        if base_market == "KRW":
            params = {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": symbol}
            result = await self.private_get_fetch_ticker_price_krw(self.extend(params))
        elif base_market == "USD":
            market_code = await self.get_market_code_in_feeder(symbol=symbol, base_market=base_market)
            params = {"AUTH": "", "EXCD": market_code, "SYMB": symbol}
            result = await self.fetchTickerForUS(self.extend(params))
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_ticker(response, base_market)

    async def fetch_historical_data(
        self,
        symbol: str,
        time_frame: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        base_market: str = "KRW",
    ):
        limit = 100

        if end is None:
            end = KoreaInvest.now(base_market=base_market)

        if start is None:

            if time_frame.endswith("m"):
                start = end - timedelta(minutes=30)

                if base_market == "KRW":
                    params = {
                        "FID_ETC_CLS_CODE": "",
                        "FID_COND_MRKT_DIV_CODE": "J",  # "U"
                        "FID_INPUT_ISCD": symbol,
                        "FID_INPUT_HOUR_1": start.strftime("%H%M%S"),  # 업종은 조회 간격만 입력 가능
                        "FID_PW_DATA_INCU_YN": "N",
                    }

                    result = await self.private_get_fetch_security_ohlcv_minute_krw(self.extend(params))

            elif time_frame.endswith("D"):
                start = end - timedelta(days=limit)
            elif time_frame.endswith("W"):
                start = end - timedelta(weeks=limit)
            elif time_frame.endswith("M"):
                start = end - timedelta(days=limit * 30)
            elif time_frame.endswith("Y"):
                start = end - timedelta(days=limit * 365)
            else:
                start = end

        if base_market == "KRW":
            params = {
                "FID_COND_MRKT_DIV_CODE": "J",
                "FID_INPUT_ISCD": symbol,
                "FID_INPUT_DATE_1": start.strftime("%Y%m%d"),
                "FID_INPUT_DATE_2": end.strftime("%Y%m%d"),
                "FID_PERIOD_DIV_CODE": time_frame,
                "FID_ORG_ADJ_PRC": "1",
            }

            result = await self.private_get_fetch_security_ohlcv_krw(self.extend(params))
            # index는 구분해서 날려야함
            # response = self.private_get_fetch_index_ohlcv_krw(self.extend(params))
        elif base_market == "USD":
            if time_frame == "D":
                gubn = "0"
            elif time_frame == "W":
                gubn = "1"
            elif time_frame == "M":
                gubn = "2"
            else:
                return self.get_error_response(
                    error_code="time frame error", error_message=f"{time_frame} time-frame is not supported."
                )

            market_code = await self.get_market_code_in_feeder(symbol=symbol, base_market=base_market)

            params = {
                "AUTH": "",
                "EXCD": market_code,
                "SYMB": symbol,
                "GUBN": gubn,
                "BYMD": end.strftime("%Y%m%d"),
                "MODP": "1",
                "KEYB": "",
            }

            result = await self.fetchOHLCVforUS(self.extend(params))
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_historical_data(response, base_market)

    async def fetch_is_holiday(self, dt: datetime, base_market: str = "KRW"):
        if base_market == "KRW":
            params = {"BASS_DT": dt.strftime("%Y%m%d"), "CTX_AREA_NK": "", "CTX_AREA_FK": ""}
            result = await self.private_get_fetch_calendar_holiday_krw(self.extend(params))

            response = self.get_response(result, params)
            if response["response"]["success"] != "0":
                return response

            return self.parser.parse_is_holiday(response, base_market)
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

    # endregion public feeder

    # region private feeder
    # @RestExchange.check_token
    async def fetch_balance(self, acc_num: str, base_market: str = "KRW"):
        if base_market == "KRW":
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "AFHR_FLPR_YN": "N",
                "OFL_YN": "",
                "INQR_DVSN": "01",
                "UNPR_DVSN": "01",
                "FUND_STTL_ICLD_YN": "N",
                "FNCG_AMT_AUTO_RDPT_YN": "N",
                "PRCS_DVSN": "01",
                "CTX_AREA_FK100": "",
                "CTX_AREA_NK100": "",
            }

            result = await self.private_get_fetch_balance_krw(self.extend(params))
        elif base_market == "USD":
            market_code = await self.get_market_code_in_feeder(symbol="ALL", base_market=base_market)
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "OVRS_EXCG_CD": market_code,
                "TR_CRCY_CD": "USD",
                "CTX_AREA_FK200": "",
                "CTX_AREA_NK200": "",
            }

            result = await self.private_get_fetch_balance_usd(self.extend(params))
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_balance(response, base_market)

    async def fetch_cash(self, acc_num: str, base_market: str = "KRW"):
        if base_market == "KRW":
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "AFHR_FLPR_YN": "N",
                "OFL_YN": "",
                "INQR_DVSN": "01",
                "UNPR_DVSN": "01",
                "FUND_STTL_ICLD_YN": "N",
                "FNCG_AMT_AUTO_RDPT_YN": "N",
                "PRCS_DVSN": "01",
                "CTX_AREA_FK100": "",
                "CTX_AREA_NK100": "",
            }

            result = await self.private_get_fetch_cash_krw(self.extend(params))
        elif base_market == "USD":
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                # 01: 원화, 02: 외화
                "WCRC_FRCR_DVSN_CD": "02",
                "NATN_CD": "840",
                "TR_MKET_CD": "00",
                "INQR_DVSN_CD": "00",
            }

            result = await self.fetchCashForUS(self.extend(params))
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_cash(response, base_market)

    async def fetch_orderbook(self, symbol: str, base_market: str = "KRW"):
        if base_market == "KRW":
            params = {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": symbol}

            result = await self.private_get_fetch_orderbook_krw(self.extend(params))
        elif base_market == "USD":
            params = {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": symbol}

            result = await self.fetchCashForUS(self.extend(params))
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_orderbook(response, base_market)

    async def fetch_pnl(self, acc_num: str, include_cost: bool = True, base_market: str = "KRW"):
        if base_market == "KRW":
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "AFHR_FLPR_YN": "N",
                "OFL_YN": "",
                "INQR_DVSN": "00",
                "UNPR_DVSN": "01",
                "FUND_STTL_ICLD_YN": "N",
                "FNCG_AMT_AUTO_RDPT_YN": "N",
                "PRCS_DVSN": "01",
                "COST_ICLD_YN": "Y" if include_cost else "N",
                "CTX_AREA_FK100": "",
                "CTX_AREA_NK100": "",
            }

            result = await self.private_get_fetch_pnl_krw(self.extend(params))
        elif base_market == "USD":
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                # 01: 원화, 02: 외화
                "WCRC_FRCR_DVSN_CD": "02",
                "NATN_CD": "840",
                "TR_MKET_CD": "00",
                "INQR_DVSN_CD": "00",
            }

            result = await self.fetchCashForUS(self.extend(params))
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_pnl(response, base_market)

    async def fetch_screener_list(self, user_id, base_market: str = "KRW"):
        params = {"USER_ID": user_id}

        if base_market == "KRW":
            result = await self.private_get_fetch_screener_list_krw(self.extend(params))
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_screener_list(response, base_market)

    async def fetch_screener(self, user_id: str, screen_id: str, base_market: str = "KRW"):
        if base_market == "KRW":
            params = {"USER_ID": user_id, "SEQ": screen_id}

            result = await self.private_get_fetch_screener_krw(self.extend(params))
        elif base_market == "USD":
            market_code = self.get_market_code_in_feeder(symbol="ALL", base_market=base_market)
            params = {"AUTH": "", "EXCD": market_code, "CO_YN_PRICECUR": 1}
            result = await self.fetchScreenerForUS(self.extend(params))

        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_screener(response, base_market)

    async def fetch_security(self, symbol: str, base_market: str = "KRW"):
        if base_market == "KRW":
            params = {"PRDT_TYPE_CD": "300", "PDNO": symbol}  # 주식

            result = await self.private_get_fetch_security_info_krw(self.extend(params))
        elif base_market == "USD":
            params = {"PRDT_TYPE_CD": "J", "PDNO": symbol}

            result = await self.fetchCashForUS(self.extend(params))
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_security(response, base_market)

    # endregion private feeder

    # region broker
    async def create_order(
        self,
        acc_num: str,
        symbol: str,
        ticket_type: str,
        price: float,
        qty: float,
        otype: str,
        base_market: str = "KRW",
    ):
        if base_market == "KRW":
            if otype.upper() == "limit".upper():
                order_dvsn = "00"
            elif otype.upper() == "market".upper():
                order_dvsn = "01"

            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "PDNO": symbol,
                "ORD_DVSN": order_dvsn,
                "ORD_QTY": str(qty),  # string type 으로 설정
                "ORD_UNPR": str(price),  # string type 으로 설정
            }

            if ticket_type == "EntryLong":
                result = await self.private_post_send_order_entry_krw(self.extend(params))
            elif ticket_type == "ExitLong":
                result = await self.private_post_send_order_exit_krw(self.extend(params))
            else:
                return
        elif base_market == "USD":
            if otype.upper() == "limit".upper():
                order_dvsn = "00"
            elif otype.upper() == "market".upper():
                # 미국장은 시장가를 세부적으로 구분하여 지원함. -> 시장가 거래를 우선 지원하지 않는다.
                # https://apiportal.koreainvestment.com/apiservice/apiservice-overseas-stock#L_e4a7e5fd-eed5-4a85-93f0-f46b804dae5f
                return self.get_error_response(
                    error_code="market_error", error_message=f"{base_market} market is not yet supported."
                )

            if ticket_type == "entry_long":
                sell_type = ""
            elif ticket_type == "exit_long":
                sell_type = "00"
            else:
                return

            market_code = await self.get_market_code_in_broker(symbol=symbol, base_market=base_market)
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "OVRS_EXCG_CD": market_code,
                "PDNO": symbol,
                "ORD_DVSN": order_dvsn,
                "ORD_QTY": str(qty),  # string type 으로 설정
                "SLL_TYPE": sell_type,
                "OVRS_ORD_UNPR": str(price),  # string type 으로 설정
                "ORD_SVR_DVSN_CD": "0",
            }

            if ticket_type == "entry_long":
                result = await self.sendOrderEntryForUS(self.extend(params))
            elif ticket_type == "exit_long":
                result = await self.sendOrderExitForUS(self.extend(params))
            else:
                return
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_create_order(response, base_market)

    async def cancel_order(
        self,
        acc_num: str,
        order_id: str,
        symbol: Optional[str] = "",
        qty: float = 0,
        base_market: str = "KRW",
        **kwargs,
    ):
        if base_market == "KRW":
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "KRX_FWDG_ORD_ORGNO": "",
                "ORGN_ODNO": str(order_id),
                "RVSE_CNCL_DVSN_CD": "02",
                "ORD_DVSN": "00",
                "ORD_QTY": str(qty),
                "ORD_UNPR": str(0),
                "QTY_ALL_ORD_YN": "N",
            }

            # 수량 미입력시 전량 취소
            if qty == 0:
                params["QTY_ALL_ORD_YN"] = "Y"

            result = await self.private_post_send_cancel_order_krw(self.extend(params))
        elif base_market == "USD":
            if qty == 0:
                return self.get_error_response(
                    error_code="qty_error", error_message=f"{base_market} cancel order need to set qty."
                )

            market_code = await self.get_market_code_in_broker(symbol=symbol, base_market=base_market)
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "OVRS_EXCG_CD": market_code,
                "PDNO": symbol,
                "ORGN_ODNO": str(order_id),
                "RVSE_CNCL_DVSN_CD": "02",
                "ORD_QTY": str(qty),
                "OVRS_ORD_UNPR": str(0),
            }

            result = await self.sendCancelOrderForUS(self.extend(params))
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_cancel_order(response, base_market)

    async def modify_order(
        self,
        acc_num: str,
        order_id: str,
        price: float,
        qty: float,
        symbol: Optional[str] = "",
        base_market: str = "KRW",
        **kwargs,
    ):
        if base_market == "KRW":
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "KRX_FWDG_ORD_ORGNO": "",
                "ORGN_ODNO": str(order_id),
                "RVSE_CNCL_DVSN_CD": "01",
                "ORD_DVSN": "00",
                "ORD_QTY": str(qty),
                "ORD_UNPR": str(price),
                "QTY_ALL_ORD_YN": "N",
            }

            # 수량 미입력시 전량 수정
            if qty == 0:
                params["QTY_ALL_ORD_YN"] = "Y"

            result = await self.private_post_send_modify_order_krw(self.extend(params))
        elif base_market == "USD":
            market_code = await self.get_market_code_in_broker(symbol=symbol, base_market=base_market)
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "OVRS_EXCG_CD": market_code,
                "PDNO": symbol,
                "ORGN_ODNO": str(order_id),
                "RVSE_CNCL_DVSN_CD": "01",
                "ORD_QTY": str(qty),
                "OVRS_ORD_UNPR": str(price),
            }

            result = await self.sendModifyOrderForUS(self.extend(params))
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_modify_order(response, base_market)

    async def fetch_open_order(
        self,
        acc_num: str,
        symbol: Optional[str] = "",
        start: Optional[str] = None,
        end: Optional[str] = None,
        base_market: str = "KRW",
    ):
        if start is None:
            start = KoreaInvest.now(base_market=base_market).strftime("%Y%m%d")

        if end is None:
            end = KoreaInvest.now(base_market=base_market).strftime("%Y%m%d")

        if base_market == "KRW":
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "INQR_STRT_DT": start,
                "INQR_END_DT": end,
                "SLL_BUY_DVSN_CD": "00",
                "INQR_DVSN": "00",
                "PDNO": symbol,
                "CCLD_DVSN": "02",
                "ORD_GNO_BRNO": "",
                "ODNO": "",
                "INQR_DVSN_3": "00",
                "INQR_DVSN_1": "",
                "CTX_AREA_FK100": "",
                "CTX_AREA_NK100": "",
            }

            result = await self.private_get_fetch_opened_order_krw(self.extend(params))
        elif base_market == "USD":
            market_code = await self.get_market_code_in_broker("ALL", base_market=base_market)
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "PDNO": symbol if symbol is not None else "%",
                "OVRS_EXCG_CD": market_code,
                "SORT_SQN": "DS",  # DS : 정순, AS : 역순
                "CTX_AREA_NK200": "",
                "CTX_AREA_FK200": "",
            }

            result = await self.fetchOpenedOrderForUS(self.extend(params))
        else:
            return self.get_error_response(
                error_code="market_error", error_message=f"{base_market} market is not yet supported."
            )

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_open_order_history(response, base_market)

    async def fetch_closed_order(
        self,
        acc_num: str,
        symbol: Optional[str] = "",
        start: Optional[str] = None,
        end: Optional[str] = None,
        base_market: str = "KRW",
    ):
        if start is None:
            start = KoreaInvest.now(base_market=base_market).strftime("%Y%m%d")

        if end is None:
            end = KoreaInvest.now(base_market=base_market).strftime("%Y%m%d")

        if base_market == "KRW":
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "INQR_STRT_DT": start,
                "INQR_END_DT": end,
                "SLL_BUY_DVSN_CD": "00",
                "INQR_DVSN": "00",
                "PDNO": symbol,
                "CCLD_DVSN": "01",
                "ORD_GNO_BRNO": "",
                "ODNO": "",
                "INQR_DVSN_3": "00",
                "INQR_DVSN_1": "",
                "CTX_AREA_FK100": "",
                "CTX_AREA_NK100": "",
            }

            result = await self.private_get_fetch_closed_order_krw(self.extend(params))
        elif base_market == "USD":
            market_code = await self.get_market_code_in_broker("ALL", base_market=base_market)
            params = {
                "CANO": acc_num[:8],
                "ACNT_PRDT_CD": acc_num[-2:],
                "PDNO": symbol if symbol is not None else "%",
                "ORD_STRT_DT": start,
                "ORD_END_DT": end,
                "SLL_BUY_DVSN": "00",
                "CCLD_NCCS_DVSN": "01" if not self.is_dev else "00",
                "OVRS_EXCG_CD": market_code,
                "SORT_SQN": "DS",  # DS : 정순, AS : 역순
                "ORD_DT": "",
                "ORD_GNO_BRNO": "",
                "ODNO": "",
                "CTX_AREA_NK200": "",
                "CTX_AREA_FK200": "",
            }

            result = await self.fetchClosedOrderForUS(self.extend(params))

        response = self.get_response(result, params)
        if response["response"]["success"] != "0":
            return response

        return self.parser.parse_closed_order_history(response, base_market)

    # endregion broker

    async def get_market_code_in_feeder(self, symbol: str, base_market: str = "KRW"):
        if base_market == "KRW":
            return ""
        elif base_market == "USD":
            if symbol.upper() == "ALL":
                return "NASD"

            response = await self.fetch_security(symbol=symbol, base_market=base_market)
            return response["exchange"]
        else:
            return ""

    async def get_market_code_in_broker(self, symbol: str, base_market: str = "KRW"):
        if base_market == "KRW":
            return ""
        elif base_market == "USD":
            if symbol.upper() == "ALL":
                return "NASD"

            response = await self.fetch_security(symbol=symbol, base_market=base_market)
            exname = response["exchange"]
            if exname == "NYS":
                return "NYSE"
            elif exname == "NAS":
                return "NASD"
            elif exname == "AMS":
                return "AMEX"
            else:
                return ""
        else:
            return ""
