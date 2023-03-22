from flask import Flask, render_template, request
import bmi_functions
import ret_functions
import validation_functions

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/getBMI', methods=['POST'])
def getBMI():
    feet = request.form['feet']
    inches = request.form['inches']
    weight = request.form['weight']

    string_inputs = [feet, inches, weight]
    answer = validation_functions.perform_validations(string_inputs, True)

    if not isinstance(answer, bool):
        final_bmi = answer
    else:
        int_inputs = list((map(int, string_inputs)))
        bmi = bmi_functions.calc_bmi(int_inputs[0], int_inputs[1], int_inputs[2])
        category = bmi_functions.get_bmi_category(bmi)
        format_bmi = "{:.4f}".format(bmi)
        final_bmi = "Your BMI is: " + str(format_bmi) + " [" + category + "]"

    return render_template('main.html', bmi=final_bmi, feet=feet, inches=inches, weight=weight)


@app.route('/getRetAge', methods=['POST'])
def getRetAge():
    age = request.form['age']
    salary = request.form['salary']
    per_saved = request.form['perSave']
    goal = request.form['goal']

    string_inputs = [age, salary, per_saved, goal]
    answer = validation_functions.perform_validations(string_inputs, False)

    if not isinstance(answer, bool):
        ret_age = answer
    else:
        float_inputs = list((map(float, string_inputs)))
        per_saved_dec = (float_inputs[2] / 100.0)
        ret_age_value = ret_functions.get_retirement_age(float_inputs[0], float_inputs[1], float(per_saved_dec), float_inputs[3])
        ret_cat = ret_functions.get_retirement_category(ret_age_value)
        ret_age = "Your retirement age is: " + str(ret_age_value) + " - " + ret_cat

    return render_template('main.html', retAge=ret_age, currentAge=age, salary=salary, perSaved=per_saved, goal=goal)


# host='localhost', port='5050'
app.run()
