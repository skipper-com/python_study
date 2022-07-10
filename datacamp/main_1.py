from datacamp.helper import validate_and_execute
import logging

logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")

user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days and conversion units (<int>:minutes):\n")
    days_and_unit = user_input.split(":")
    days_and_units_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_units_dictionary)
    validate_and_execute(days_and_units_dictionary)