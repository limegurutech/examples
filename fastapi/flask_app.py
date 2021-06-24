from flask import Flask
app = Flask(__name__)

@app.route('/')
def read_root():
    return {"Hello": "World"}

app.run()
