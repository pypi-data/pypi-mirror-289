"""
This Library is intended to provide an ergonomic abstraction around the set of utility functions provided
by the MetaTrader5 official python library, This library employs an Object oriented Approach to structing
the functions and their interactions, its extends the core functionality by abstract certain data/values as 
new datatypes which makes the interaction more seamless

Author: Brian Obot <brianobot9@gmail.com>
"""
from typing import Literal

import MetaTrader5 as meta_trader

from .order import BuyTradeOrder, SellTradeOrder


class Account:
    def __init__(self, account_number: int, password: str, server: str):
        self.account_number = int(account_number)
        self.password = password
        self.server = server
        self.connected = False
        print(f"Data = {self.to_data()}")

    def connect(self) -> tuple[bool, bool]:
        init_status = meta_trader.initialize()
        login_status = meta_trader.login(
            self.account_number,
            self.password,
            self.server,
        )
        return init_status, login_status

    def disconnect(self) -> None:
        meta_trader.shutdown()

    def info(self) -> dict:
        self.connect()
        account_info = meta_trader.account_info()
        return account_info._asdict() if account_info else None

    def to_data(self) -> dict:
        """
        Convert an account instance to a dictionary of it core attributes
        """
        return {
            "account_number": self.account_number,
            "password": self.password,
            "server": self.server,
        }

    def create_order_request(self, type: Literal['buy', 'sell'], symbol: str = "EURUSD", pip_factor: int = 10):
        point = meta_trader.symbol_info(symbol).point
        price = meta_trader.symbol_info_tick(symbol).ask
        return {
            "symbol": symbol,
            "price": price,
            "lot": 0.01,  # TODO change
            "sl": round(price - 1000 * point, 3) if type == "buy" else round(price + 1000 * point, 3),
            "tp": round(price + pip_factor * point, 3) if type == "buy" else round(price - pip_factor * point, 3),
            "deviation": 20,  # TODO change
        }

    def create_buy_order(self, symbol: str = "EURUSD", pip_factor: int = 10, execute: bool = True) -> BuyTradeOrder:
        return BuyTradeOrder(**self.create_order_request("buy", symbol, pip_factor), execute=execute)

    def create_sell_order(self, symbol: str = "EURUSD", pip_factor: int = 10, execute: bool = True) -> SellTradeOrder:
        return SellTradeOrder(**self.create_order_request("sell", symbol, pip_factor), execute=execute)

    @property
    def last_error(self) -> str:
        return meta_trader.last_error()

    @classmethod
    def from_data(cls, data: dict) -> "Account":
        """
        Instaniate an Account from a dictionary of its core attribute
        """
        return Account(**data)

    def __eq__(self, account: "Account") -> bool:
        return self.to_data() == account.to_data()

    def __repr__(self) -> str:
        return f"Account({self.account_number}-{self.server})"


def create_test_account() -> Account:
    return Account("83230967", "CfAiUs!7", "MetaQuotes-Demo")
