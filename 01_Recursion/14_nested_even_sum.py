# obj1 = {
#   "outer": 2,
#   "obj": {
#     "inner": 2,
#     "otherObj": {
#       "superInner": 2,
#       "notANumber": True,
#       "alsoNotANumber": "yup"
#     }
#   }
# }

# obj2 = {
#   "a": 2,
#   "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
#   "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
#   "d": 1,
#   "e": {"e": {"e": 2}, "ee": 'car'}
# }

# nested_even_sum(obj1)   # 6
# nested_even_sum(obj2)   # 10

def nested_even_sum(obj):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nested_even_sum(obj[key])
        elif type(obj[key]) is int and obj[key]%2 == 0:
            sum += obj[key]
    return sum