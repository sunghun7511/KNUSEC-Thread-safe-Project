# -*- coding: utf-8 -*-
from wallet import Wallet, MutexWallet


RUN_BANK_WITH_MUTEX = False

my = MutexWallet() if RUN_BANK_WITH_MUTEX else Wallet()

logs = ["Started KNUSEC Bank APP"]


def append_log(log: str):
    logs.append(log)


def build_data() -> dict:
    global my, logs
    return {"money": my.get_money(), "bank": my.get_bank(), "logs": logs[::-1]}
