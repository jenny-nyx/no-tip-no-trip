from flask import Flask, render_template, request
import calculator

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
@app.route('/home')
def root():
    return render_template('home.html')

@app.route('/calculator', methods = ['POST', 'GET'])
def tripCalculator():
    # this will probably take in miles and return trip?
    form_data = request.form.to_dict()
    print(form_data)
    calculator.main()
    return render_template('calculator.html', form_data = form_data)

if __name__ == "__main__":
    app.run( debug = True)