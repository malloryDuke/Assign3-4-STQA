from flask import Flask, render_template, request
import bmiFunctions
import retFunctions

app = Flask(__name__)

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

    bmi = bmiFunctions.calcBMI(int(feet), int(inches), int(weight))
    category = bmiFunctions.getBMICategory(bmi)
    formatBMI = "{:.4f}".format(bmi)
    return render_template('main.html', bmi= "Your BMI is: " + str(formatBMI) + " [" + category + "]", feet=feet, inches=inches, weight=weight)

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

    retAge = retFunctions.getRetirementAge(int(age), int(salary), int(perSaved), int(goal))
    retCat = retFunctions.getRetirementCategory(retAge)
    return render_template('main.html', retAge = "Your retirement age is: " + str(retAge) + " - " + retCat, currentAge = age, salary=salary, perSaved=perSaved, goal=goal)

app.run(host='localhost', port='5050')
