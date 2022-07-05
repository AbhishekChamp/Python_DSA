# obj = {
#     "stuff": 'foo',
#     "data": {
#         "val": {
#             "thing": {
#                 "info": 'bar',
#                 "moreInfo": {
#                     "evenMoreInfo": {
#                         "weMadeIt": 'baz'
#                     }
#                 }
#             }
#         }
#     }
# }

# collect_strings(obj) # ['foo', 'bar', 'baz']

def collect_strings(obj):
    result = []
    for key in obj:
        if type(obj[key]) is str:
            result.append(obj[key])
        if type(obj[key]) is dict:
            result = result + collect_strings(obj[key])
    return result