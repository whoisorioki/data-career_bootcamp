from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome!'

@app.route('/data')
def get_data():
    data = {
        'name': 'Adrian Orioki',
        'age': 21,
        'email': 'adrianorioki@gmail.com'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
