from flask import Flask, send_from_directory, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for all routes

data = ""

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/post')
def postdata():
    global data
    data = request.args.get('data')
    
    if data:
        return f'The received data is: {data}'
    else:
        return 'No data received.'

@app.route('/data')
def senddata():
    return data

if __name__ == '__main__':
    #app.run(debug=False)
    app.run(debug=False, host='0.0.0.0', port=5000)
