from flask import Flask
#123
app = Flask(__name__)


@app.route('/api/v1/hello-world-8')
def hello_world():
    return 'Hello, World-8'


app.run()