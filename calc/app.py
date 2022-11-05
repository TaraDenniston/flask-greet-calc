# Put your app in here.

from flask import Flask, request
import operations as o

app = Flask(__name__)

@app.route('/math/<oper>')
def math_page(oper):
    a = int(request.args["a"])
    b = int(request.args["b"])

    operations = {
        'add': o.add(a, b),
        'sub': o.sub(a, b),
        'mult': o.mult(a, b),
        'div': o.div(a, b)
    }

    return str(operations.get(oper))

