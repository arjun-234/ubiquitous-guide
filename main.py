from flask import Flask

app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def hello_world():
    return 'Greetings!'

if __name__ == '__main__':
    app.run(debug=True)
