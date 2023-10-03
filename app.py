from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def adding():
    add_a = request.args['a']
    add_b = request.args['b']
    add_result = add(int(add_a), int(add_b))
    return f"{add_result}"

@app.route('/sub')
def subtracting():
    sub_a = request.args['a']
    sub_b = request.args['b']
    sub_result = sub(int(sub_a), int(sub_b))
    return f"{sub_result}"

@app.route('/mult')
def multiplying():
    mult_a = request.args['a']
    mult_b = request.args['b']
    mult_result = mult(int(mult_a), int(mult_b))
    return f"{mult_result}"

@app.route('/div')
def dividing():
    div_a = request.args['a']
    div_b = request.args['b']
    div_result = div(int(div_a), int(div_b))
    return f"{div_result}"