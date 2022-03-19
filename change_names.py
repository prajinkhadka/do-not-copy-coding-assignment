def no_of_func(data)
    count_no_f = 0
    for item in data:
        for i in range(len((data[item]['body']))):
            if list(data[item]['body'][i].keys())[0] ==  'FunctionDef':
                count_no_f += 1
    return count_no_f


def change_func_name(data, count_no_f):
    for k in data.keys():
        for j in range(count_no_f):
            data[k]['body'][j]['FunctionDef']['name']= 'newFuncName' + str(j)
    return data 

def change_function_dec(data):
    for i, term in enumerate((data['Module']['body'])):
        if (list(term.keys())[0] == 'Assign'):
            data['Module']['body'][i]['Assign']['targets'][0]['Name']['id'] = 'new Name' +str(i)
