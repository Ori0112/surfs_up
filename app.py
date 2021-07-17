

from flask import Flask

# Create new flask app instance

app = Flask(__name__)

#Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'

#Run a flask app
if __name__ == "__main__":
    app.run()
