def calc_bmi(feet, inches, weight):
    total_inches = (feet * 12) + inches
    converted_weight = weight * 0.45
    converted_height = total_inches * 0.025
    conv_height_sqr = converted_height * converted_height
    return converted_weight / conv_height_sqr


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25.0:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"
