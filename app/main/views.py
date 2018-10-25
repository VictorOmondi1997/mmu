from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from .calc import Calc
from .forms import CalculatorForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = CalculatorForm()
    answer = 0.00
    error = None
    num1 = form.num1.data
    num2 = form.num2.data
    calc = Calc(num1, num2)
    if form.validate_on_submit():
        operator = form.operator.data
        answer = calculations(operator, calc)
    elif num1 == 0 or num2 == 0:
        operator = form.operator.data
        answer = calculations(operator, calc)
    else:
        error = "Enter numbers only"

        # using try except to catch errors where the input is not a number

    return render_template('index.html', form=form, answer=answer, error=error)


def calculations(opr, calc):
    if opr == 'Multiply':
        answer = calc.multiply()
        flash('Multiplies Successfully', category='danger')
    elif opr == 'Add':
        answer = calc.addition()
        flash('Added Successfully', category='danger')
    elif opr == 'Divide':
        check = calc.divide()
        if check == 0:
            answer = 'Cannot divide by zero'
        else:
            answer = check
            flash('Divided Successfully', category='danger')
    elif opr == 'Subtract':
        answer = calc.subtraction()
        flash('Subtracted Successfully', category='danger')
    elif opr == 'Reminder':
        check = calc.divide()
        if check == 0:
            answer = 'Cannot divide by zero'
        else:
            answer = check
            flash('Divided Successfully', category='danger')
    return answer

    # if str(num1).isnumeric() and str(num2).isnumeric():
