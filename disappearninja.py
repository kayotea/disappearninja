from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def color(color):
    print color
    if (color == 'blue' or color == 'Blue'):
        #leonardo
        return render_template('blue.html')
    elif (color == 'orange' or color == 'Orange'):
        #michaelangelo
        return render_template('orange.html')
    elif (color == 'red' or color == 'Red'):
        #raphael
        return render_template('red.html')
    elif (color == 'purple' or color == 'Purple'):
        #donatello
        return render_template('purple.html')
    else:
        #nope
        return render_template('nope.html')


app.run(debug = True)