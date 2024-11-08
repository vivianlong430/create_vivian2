from flask import Flask,request
#from datetime import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login')
def login():
    return 'place to login'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'


@app.route('/chat')
def chat():
    #http://localhost:5000/chat?message=Hello%20Flask!
    message = request.args.get('message', '')
    return f"You said: {message}. That's interesting!"

#@app.route('/time')
#def current_time():
    #now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")
    #return f"The current time is: {current_time}"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)