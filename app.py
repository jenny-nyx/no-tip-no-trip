from flask import Flask, render_template
import calculator

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def root():
    # this will probably take in miles and return trip?
    calculator.main()
    return render_template('home.html')

if __name__ == "__main__":
    app.run( debug = True)