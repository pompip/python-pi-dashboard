from flask import Flask,render_template
from collections import defaultdict
app = Flask(__name__,static_folder="assets")


@app.route('/')
def index():
    di = defaultdict( lambda : defaultdict( lambda : defaultdict(int) ) )

    di = {
        "men":{"total",10},
        "user":"liukechong",
        "model":{"pimodel":"hello world"},
        "os":["hi"],
        "cpu":{"freq":1003300},
        "model":{"id":"raspberry-pi"}
        }
    di["cpu"]={"freq":1103300}
    return render_template('index.html',D=di)

app.run(host='0.0.0.0',debug=True)