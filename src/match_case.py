variable = 12.3
match variable:
    case str():
        print("Variable is a string.")
    case int():
        print("Variable is an integer.")
    case float():
        print("Variable is a float.")
    case _:
        print("Variable is another type.")
