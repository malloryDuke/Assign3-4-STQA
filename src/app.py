from flask import Flask, render_template, request
import bmiFunctions
import retFunctions

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

    feet = str(feet)
    inches = str(inches)
    weight = str(weight)

    if ((int(feet) <= 0) or (int(inches) <= 0) or (int(weight) <= 0)):
        finalBMI = "Feet, inches, or weight cannot be negative or equal to 0 -- Enter valid inputs"
    else:
        bmi = bmiFunctions.calcBMI(int(feet), int(inches), int(weight))
        category = bmiFunctions.getBMICategory(bmi)
        formatBMI = "{:.4f}".format(bmi)
        finalBMI = "Your BMI is: " + str(formatBMI) + " [" + category + "]"

    return render_template('main.html', bmi=finalBMI, feet=feet, inches=inches, weight=weight)

@app.route('/getRetAge', methods=['POST'])
def getRetAge():
    age = request.form['age']
    salary = request.form['salary']
    perSaved = request.form['perSave']
    goal = request.form['goal']

    age = str(age)
    salary = str(salary)
    perSaved = str(perSaved)
    goal = str(goal)

    if (int(age) <= 0):
        retAge = "Current age cannot be negative or equal to 0 -- Enter a correct age"
    elif (int(salary) <= 0):
        retAge = "Salary cannot be negative or equal to 0 -- Enter a correct salary"
    elif (float(perSaved) <= 0):
        retAge = "Percent saved cannot be negative or 0 -- Enter a correct value"
    elif (int(goal) <= 0):
        retAge = "Savings goal cannot be negative or 0 -- Enter a valid savings goal"
    else:
        retAgeValue = retFunctions.getRetirementAge(int(age), int(salary), float(perSaved), int(goal))
        retCat = retFunctions.getRetirementCategory(retAgeValue)
        retAge = "Your retirment age is: " + str(retAgeValue) + " - " + retCat

    return render_template('main.html', retAge = retAge, currentAge = age, salary=salary, perSaved=perSaved, goal=goal)

#host='localhost', port='5050'
app.run()
