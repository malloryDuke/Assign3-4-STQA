from validation import validate_text, validate_int, validate_float


def perform_validations(str_inputs, cast_to_ints):
    valid_strings = validate_input_lengths(str_inputs)
    if valid_strings and cast_to_ints:
        num_inputs = list((map(int, str_inputs)))
        return validate_num_values(num_inputs, True)
    elif valid_strings:
        num_inputs = list((map(float, str_inputs)))
        return validate_num_values(num_inputs, False)
    else:
        return "Must enter all values"


def validate_input_lengths(strInputs):
    try:
        list((filter(lambda val: validate_text(val, min_length=1), strInputs)))
        return True
    except ValueError:
        return False


def validate_num_values(num_inputs, is_ints):
    try:
        if is_ints:
            list((filter(lambda val: validate_int(val, min_value=1), num_inputs)))
        else:
            list((filter(lambda val: validate_float(val, min_value=1.0), num_inputs)))
        return True
    except ValueError or TypeError:
        return "Inputs cannot be negative or equal to 0 -- Enter correct inputs"
