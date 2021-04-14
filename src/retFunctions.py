import math as math

def getRetirementAge(age, salary, perSaved, goal):
    savePerYear = (salary * perSaved) * 1.35
    yrsTillGoal = math.ceil(goal/savePerYear)
    return age + yrsTillGoal

def getRetirementCategory(retAge):
    if (retAge < 100):
        return "Goal will be met"
    else:
        return "Goal will NOT be met"
