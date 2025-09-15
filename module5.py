empty_dict = {}

my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(my_dict["name"])
print(my_dict["age"])

#adding
my_dict["email"] = "alice@gmail.com"
print(my_dict)
my_dict.update({"a":1})
print(my_dict)

#delete
# del my_dict["age"]
# print(my_dict)
# my_dict.pop("email")
# print(my_dict)
# my_dict.clear()
# print(my_dict)

#return all keys/values
print(my_dict.keys())
print(my_dict.values())

#check for a key, value pair
print(my_dict.get("address", "Not Found"))