"""
This Library is intended to provide an ergonomic abstraction around the set of utility functions provided
by the MetaTrader5 official python library, This library employs an Object oriented Approach to structing
the functions and their interactions, its extends the core functionality by abstract certain data/values as 
new datatypes which makes the interaction more seamless

Author: Brian Obot <brianobot9@gmail.com>
"""

# import MetaTrader5 as meta_trader


class Account:
    def __init__(self, account_number: int, password: str, server: str):
        self.account_number = int(account_number)
        self.password = password
        self.server = server
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
        return meta_trader.account_info()._asdict()

    def to_data(self) -> dict:
        """
        Convert an account instance to a dictionary of it core attributes
        """
        return {
            "account_number": self.account_number,
            "password": self.password,
            "server": self.server 
        }

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