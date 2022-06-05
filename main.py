from flask import Flask, render_template, request


# create an instance for your flask app
app = Flask(__name__)

# decorator for url routing
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user')
def hello_user():
    return 'Hello User!'

@app.route('/html')
def get_html():
    return render_template("index.html")

@app.route('/qs')
def get_qs():
    if request.args:
        req = request.args
        return " ".join(f"{k}:{v}" for k,v in req.items() )

    return "No query"

if __name__ == '__main__':
    app.run()
    # app.run(debug=True)