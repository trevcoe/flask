# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def do_add():
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        result = add(a,b)

        return str(results)

@app.route("/sub")
def do_sub():
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        result = sub(a,b)

        return str(results)

"""mult and div are basically the same exact thing, just sub out the words"""

"""further study addresses this..."""

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}
@app.route("/math/<operation>")
def do_math(operation):

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operation](a,b)

    return str(results)




