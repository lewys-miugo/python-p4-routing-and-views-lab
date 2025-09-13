#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:number>')
def count(number):
    numbers = [str(n) for n in range(number)] 
    for n in numbers:
        print(n)
    return "\n".join(numbers) + "\n"

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == '+':
        result = num1 +num2
    elif operation == '-':
        result = num1 - num2
    elif operation == 'div':
        result = num1/num2
    elif operation == '*':
        result = num1*num2
    elif operation == '%':
        result = num1%num2
    else:
        result = "Invalid inputs"

    print(result)
    return str(result)

    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
