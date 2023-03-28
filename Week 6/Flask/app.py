from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome!'

@app.route('/api/data')
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'johndoe@example.com'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
