from flask import Flask, render_template, request
# Import the Maths package here
from Maths.mathematics import summation, subtraction, multiplication

app = Flask("Mathematics Problem Solver")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    return "The sum of {} and {} is {}".format(num1, num2, summation)

@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    return "The result of substracting {} from {} is {}".format(num2, num1, substraction)

@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here  
    return "The product of {} and {} is {}".format(num1, num2, multiplication)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
