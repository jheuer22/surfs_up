
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

hello_world()

num = [0, 1, 2, 3, 4]
for num in range(5):
    print(num)


