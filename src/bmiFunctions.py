def calcBMI(feet, inches, weight):
    totalInches = (feet * 12) + inches
    convertedWeight = weight * 0.45
    convertedHeight = totalInches * 0.025
    convHeightSqr = convertedHeight * convertedHeight
    return convertedWeight/convHeightSqr

def getBMICategory(bmi):
    if (bmi < 18.5):
        return "underweight"
    elif (bmi < 25.0):
        return "normal"
    elif (bmi < 30):
        return "overweight"
    else:
        return "obese"