from flask import Flask, render_template
import calculator

app = Flask("main")


@app.route('/')
def root():
    calculator.main()
    return render_template('home.html')
