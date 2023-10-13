'''from flask import *
app = Flask(__name__)






if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
'''

from flask import  *
import random

app = Flask(__name__)




@app.route('/', methods=['GET'])
def home():
    if request.args.get("g") != None:
        g = int(request.args.get("g"))
        print(g)
    else:
        g = 0
    return render_template('index.html', g = g)


if __name__ == '__main__':
    app.run(debug=True)