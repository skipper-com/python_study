def days_to_units(num_of_days, conversion_unit):   
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} seconds"
    else:
        return "unsupported unit"

def validate_and_execute(days_and_units_dictionary):
    try:
        user_input_number = int(days_and_units_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_units_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a zero value")
        else:
            print("you entered a negative value")
    except ValueError:
        print("enter a positive integer number")