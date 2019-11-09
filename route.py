# -*- coding: utf-8 -*-
from flask import *
from data import build_data, append_log, my
from time import sleep
from threading import Thread


SLEEP_TIME = 10


def main_view():
    return render_template("index.html", **build_data())


def wallet_view():
    return render_template("wallet.html", **build_data())


def log_view():
    return render_template("log.html", **build_data())


def deposit_view():
    param = build_data()
    if request.method == "POST":
        success = False
        message = "Unknown"
        try:
            amount = int(request.form["amount"])
            user_message = request.form["message"]

            if my.check_money(amount):
                append_log("Transaction queued ({})".format(amount))

                sleep(SLEEP_TIME)

                my.set_bank(my.get_bank() + amount)
                my.set_money(my.get_money() - amount)

                message = "Transaction successful ({} / {})".format(amount, user_message)
                success = True
            else:
                message = "Not enough money"
        except:
            message = "Cannot decode amount"

        append_log("Deposit {} -> {}".format("Failed" if not success else "Success", message))

        param["message"] = message
        param["success"] = success
        # return redirect(url_for("log_view"))

    return render_template("deposit.html", **param)


def withdraw_view():
    param = build_data()
    if request.method == "POST":
        success = False
        message = "Unknown"
        try:
            amount = int(request.form["amount"])
            user_message = request.form["message"]
            if my.check_bank(amount):
                append_log("Transaction queued ({})".format(amount))

                sleep(SLEEP_TIME)

                my.set_money(my.get_money() + amount)
                my.set_bank(my.get_bank() - amount)

                message = "Transaction successful ({}{})".format(amount, " / {}".format(user_message) if len(user_message) > 0 else "")
                success = True
            else:
                message = "Not enough money"
        except:
            message = "Cannot decode amount"

        append_log("Withdrawal {} -> {}".format("Failed" if not success else "Success", message))

        param["message"] = message
        param["success"] = success
        # return redirect(url_for("log_view"))

    return render_template("withdraw.html", **param)


def routing(app: Flask):
    app.add_url_rule("/", view_func=main_view)
    app.add_url_rule("/index", view_func=main_view)
    app.add_url_rule("/log", view_func=log_view)
    app.add_url_rule("/wallet", view_func=wallet_view)
    app.add_url_rule("/deposit", methods=["GET", "POST"], view_func=deposit_view)
    app.add_url_rule("/withdraw", methods=["GET", "POST"], view_func=withdraw_view)
