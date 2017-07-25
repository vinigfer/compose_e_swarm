from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    nome = ""
    try:
        with open("/tmp/arquivo.txt", "r") as file:
            nome = file.read()
    except:
        pass
    return 'Hello World from ' + nome +'! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
