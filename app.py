from flask import Flask, render_template, request
import calculator

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
@app.route('/home')
def root():
    return render_template('home.html')

@app.route('/calculator', methods = ['POST', 'GET'])
def calculate():
    if request.method == "POST":
      form_data = request.form.to_dict()
      calcOutput = calculator.calculate( form_data )
    return render_template('calculator', calcOutput = calcOutput)

if __name__ == "__main__":
    app.run( debug = True)