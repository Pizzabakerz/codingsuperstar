from flask import Flask

app = Flask(__name__)

@app.route('/<name>/<name2>')
def sample(name,name2):
    print(name)
    return name+" "+name2

if __name__ == '__main__':
    app.run()