# Import flask
from flask import Flask 

# Create flask instance
app = Flask(__name__)

# Define root path
@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)