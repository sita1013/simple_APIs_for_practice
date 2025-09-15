# import json

# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }

# #convert python dicts to JSON - send information over the web
# my_json = json.dumps(my_dict)

# #convert JSON to python dicts
# # my_dict = json.load(my_json)
class ValueTooHigh(Exception):
    pass
class ValueTooLow(Exception):
    pass

try: 
    input = int(input("Please enter a number between 5 and 10: "))
    if input < 5:
        raise ValueTooLow
    if input > 10:
        raise ValueTooHigh
except: 
    print("Error: please enter a number between 5 and 10.")