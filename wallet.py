# -*- coding: utf-8 -*-
import threading


class Wallet:
    def __init__(self):
        self.__money = 0
        self.__bank = 500000

    def get_money(self) -> int:
        return self.__money

    def get_bank(self) -> int:
        return self.__bank

    def set_money(self, amount: int):
        self.__money = max(0, amount)

    def set_bank(self, amount: int):
        self.__bank = max(0, amount)

    def check_money(self, amount: int):
        return self.__money >= amount

    def check_bank(self, amount: int):
        return self.__bank >= amount


class MutexWallet(Wallet):
    def __init__(self):
        super(Wallet, self).__init__()
        self.__lock = threading.Lock()
    
    def lock(self, *, block=False) -> bool:
        return self.__lock.acquire(blocking=block)

    def release(self):
        self.__lock.release()
