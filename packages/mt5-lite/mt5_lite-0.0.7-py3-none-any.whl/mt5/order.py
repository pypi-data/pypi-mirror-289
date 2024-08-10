import MetaTrader5 as meta_trader


BUY_ORDER = meta_trader.ORDER_TYPE_BUY
SELL_ORDER = meta_trader.ORDER_TYPE_SELL

TRADE_ACTION_DEAL = meta_trader.TRADE_ACTION_DEAL


class TradeOrder:
    def __init__(
        self,
        symbol: str,
        price: float,
        lot: float,
        type: str,
        tp: float,
        sl: float,
        deviation: int,
        execute: bool = False,
    ):
        self.symbol = symbol
        self.price = price
        self.lot = lot
        self.type = type
        self.tp = tp
        self.sl = sl
        self.deviation = deviation
        self.execute = execute
        self.request = {
            "action": TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": type,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": deviation,
            "magic": 234000,
            "comment": "test python script open",
            "type_time": meta_trader.ORDER_TIME_GTC,
            "type_filling": meta_trader.ORDER_FILLING_IOC,
        }
        self.send_result = None
        if execute:
            self.send()

    def send(self):
        self.send_result = meta_trader.order_send(self.request)
        return self.send_result

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(symbol={self.symbol}, price={self.price}, lot={self.lot})"


class BuyTradeOrder(TradeOrder):
    def __init__(self, **kwargs):
        kwargs["type"] = BUY_ORDER
        super().__init__(**kwargs)


class SellTradeOrder(TradeOrder):
    def __init__(self, **kwargs):
        kwargs["type"] = SELL_ORDER
        super().__init__(**kwargs)
