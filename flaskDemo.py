from flask import Flask
from flask import request

app = Flask(__name__)

products = [{"name": "bats", "price": 40}, {"name": "ball", "price": 20}]

 

@app.route('/')

def home():
    return "<h1>Welcome to the Flask App!</h1>"

 

@app.route('/new')
def new():
    return "This is a new url"

 

@app.route('/listofProducts')
def listOfProducts():
    return products

@app.route('/Calculator')
def Calculator():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2',  type=float)
    action = request.args.get('action')
    if(action == "addition"):
        return str(int(num1)+int(num2))
    if(action == "substration"):
        return str(int(num1)-int(num2))
    if(action == "multiplication"):
        return str(int(num1)*int(num2))
    if(action == "division"):
        return str(int(num1)/int(num2))

@app.route('/Calculator/add')
def Add():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    return str(int(num1)+int(num2))

@app.route('/Calculator/sub')
def Sub():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    return str(int(num1)-int(num2))

@app.route('/Calculator/multi')
def Multi():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    return str(int(num1)*int(num2))

@app.route('/Calculator/div')
def Div():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    return str(int(num1)/int(num2))

@app.route('/Calculator/mod')
def Mod():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    return str(int(num1)%int(num2))

if __name__ == '__main__':
    app.run(debug=True)