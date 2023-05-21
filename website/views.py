from flask import Blueprint, render_template, request, flash

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template('home.html')

@views.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':  
      data = request.form.to_dict() # takes the information that was from the post request that came from the form'
      keys = data.keys()
      values = data.values()
      return render_template('calculator.html', data=values)
    return render_template('calculator.html')