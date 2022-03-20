from ast import *
import ast


def no_of_func(data):
    count_no_f = 0
    for item in data:
        for i in range(len((data[item]['body']))):
            if list(data[item]['body'][i].keys())[0] ==  'FunctionDef':
                count_no_f += 1
    return count_no_f


def change_func_name(data, count_no_f):
    count_no_f = no_of_func(data)
    list_of_func_names_old = []
    list_of_func_names_new = []

    for k in data.keys():
        for j in range(count_no_f):
            list_of_func_names_old.append(data[k]['body'][j]['FunctionDef']['name'])
            data[k]['body'][j]['FunctionDef']['name']=   data[k]['body'][j]['FunctionDef']['name'] + str("_my_new_func")
            list_of_func_names_new.append(data[k]['body'][j]['FunctionDef']['name'])

    return data, count_no_f, list_of_func_names_old, list_of_func_names_new

            
def change_func_occurence(data, count_no_f, list_of_func_names_new):
    start_index = count_no_f
    for i in range((count_no_f)):
        data['Module']['body'][start_index]['Assign']['value']['Call']['func']['Name']['id'] = list_of_func_names_new[i]
        start_index += 1
    


def change_var_name(data):
    var_names_old = []
    var_names_new = []
    for i, term in enumerate((data['Module']['body'])):
        if (list(term.keys())[0] == 'Assign'):
            var_names_old.append(data['Module']['body'][i]['Assign']['targets'][0]['Name']['id'])
            data['Module']['body'][i]['Assign']['targets'][0]['Name']['id'] = data['Module']['body'][i]['Assign']['targets'][0]['Name']['id'] + str("_my_new_var")
            var_names_new.append(data['Module']['body'][i]['Assign']['targets'][0]['Name']['id'])

    return data, var_names_old, var_names_new


def back_to_ast(code,list_of_func_names_old,list_of_func_names_new,var_names_old, var_names_new ):
    tree = ast.parse(code)
    d_to_be_replaced = ast.dump(tree) 
    
    for i, func_name in enumerate(list_of_func_names_old):
        d_to_be_replaced = d_to_be_replaced.replace(list_of_func_names_old[i], list_of_func_names_new[i])
    
    
    for i, func_name in enumerate(var_names_new):
        d_to_be_replaced = d_to_be_replaced.replace(var_names_old[i], var_names_new[i])
        
    return d_to_be_replaced
    


def ast_to_python(ast_string):

    def to_ast(d):
        if isinstance(d, ast.Call):
            return getattr(ast, d.func.id)(*map(to_ast, d.args), 
                         **{i.arg:to_ast(i.value) for i in d.keywords}, **{'lineno': None, 'col_offset': None, 'end_lineno': None, 'end_col_offset': None})
        if isinstance(d, ast.List):
            return list(map(to_ast, d.elts))
        return d.value

    def ast_to_code(ast_string):
        return ast.unparse(to_ast(ast.parse(ast_string).body[0].value))

    return (ast_to_code(ast_string))
