import math as math


def get_retirement_age(age, salary, per_saved, goal):
    save_per_year = (salary * per_saved) * 1.35
    yrs_till_goal = math.ceil(goal / save_per_year)
    return age + yrs_till_goal


def get_retirement_category(ret_age):
    if (ret_age < 100):
        return "Goal will be met"
    else:
        return "Goal will NOT be met"
