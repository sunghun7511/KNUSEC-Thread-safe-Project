# -*- coding: utf-8 -*-
from flask import Flask
import wallet
import route
import data


if __name__ == "__main__":
    app = Flask(__name__,
                 static_folder="web/static",
                 template_folder="web/template")

    route.routing(app)

    app.run(debug=True)
