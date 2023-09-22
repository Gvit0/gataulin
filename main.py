from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/otvet')
def otvet():
    a = request.args.get('a', '')
    b = request.args.get('b', '')
    c = int(a)*int(b)
    return render_template('otvet.html', otvetic=c)

if __name__ == '__main__':
    app.run(host='0.0.0.0')