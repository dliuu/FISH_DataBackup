import requests

#Utility Functions:

def merge_constraints(key_list, type_list, value_list):
    '''
    Takes three lists of strings and returns a list of dictionaries in the form:
    [ { "key": "unitname", "constraint_type": "equals", "value": "Unit A" } ,{ "key": "unitnumber", "constraint_type": "greater than", "value": "3" }]

    '''
    if len(key_list) != len(type_list) or len(key_list) != len(value_list):
        raise ValueError("Input lists must have the same length")

    merged_dicts = []
    for i in range(len(key_list)):
        merged_dicts.append({
            "key": key_list[i],
            "constraint_type": type_list[i],
            "value": value_list[i]
        })
    return merged_dicts

def single_GET_request(url:str, **kwargs):
    '''GET call for a single Bubble record. URL needs to contain obj/data_type/unique_id

    example usage:
    1. print(single_GET_request('https://fish-platform.bubbleapps.io/version-test/api/1.1/obj/Loan/1711461138915x125141837305315250'))

    '''
    r = requests.get(url)
    print(r.status_code)
    response = r.json()

    return response

def GET_all_objects(url:str, **kwargs):
    '''
    Three optional parameters for constraints:
    key_list: list of str
    type_list: list of str
    value_list: list of str

    example usage: GET_all_objects('https://fish-platform.bubbleapps.io/version-test/api/1.1/obj/Loan')
    '''
    key_list = kwargs.get(key_list)
    type_list = kwargs.get(type_list)
    value_list = kwargs.get(value_list)

    constraints = merge_constraints(key_list, type_list, value_list)

    if len(constraints) == 0:
        r = requests.get(url)
        return r.json()

    else:
        url = f"{url}?constraints={constraints}"
        r = requests.get(url)
        return r.json()

#__Main__
print(GET_all_objects('https://fish-platform.bubbleapps.io/version-test/api/1.1/obj/Loan'))