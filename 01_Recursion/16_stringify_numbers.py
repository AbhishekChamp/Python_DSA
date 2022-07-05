# obj = {
#     "num": 1,
#     "test": [],
#     "data": {
#         "val": 4,
#         "info": {
#             "isRight": True,
#             "random": 66
#         }
#     }
# }

# stringify_numbers(obj)

# {'num': '1',
#   'test': [],
#   'data': {'val': '4',
#            'info': {'isRight': True, 'random': '66'}
#           }
# }

def stringify_numbers(obj):
    new_obj = obj
    for key in new_obj:
        if type(new_obj[key]) is int:
            new_obj[key] = str(new_obj[key])
        if type(new_obj[key]) is dict:
            new_obj[key] = stringify_numbers(new_obj[key])
    return new_obj