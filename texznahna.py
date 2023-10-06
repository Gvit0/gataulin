import time

from flask import *
app = Flask(__name__)

@app.route('/')
def test():

    return render_template("postread.html")



def itr(otvet):
    pass

@app.route('/post', methods=['POST'])
def tset():
    number = int(request.form['number'])
    if 100 >=number or number <=999:
        otvet = "ДА"
    else:
        otvet = "НЕТ"

    return render_template("postotvet.html",otvet = otvet)

@app.route('/postc', methods=['POST'])
def colod():
    otvet = request.form['number']
    return render_template("postotvetcold.html")
    print("1")
    time.sleep(1)
    return redirect("/post", otvet=otvet)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)