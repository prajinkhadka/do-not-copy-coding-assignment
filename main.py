import argparse 
from ast_to_json import make_ast 
from change_names import no_of_func, change_func_name, change_func_occurence, change_var_name, back_to_ast, ast_to_python

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--python_file', action='store', type=str, required=True)
args = my_parser.parse_args()
old_file_location = str(args.python_file)

def main():
    with open(old_file_location) as f:
        code = f.read()
        f.close()

    data = make_ast(code)
    count_no_f = no_of_func(data)
    data, count_no_f, list_of_func_names_old, list_of_func_names_new = change_func_name(data, count_no_f)
    change_func_occurence(data, count_no_f,list_of_func_names_new)
    data, var_names_old, var_names_new = change_var_name(data)

    final_code_ast = back_to_ast(code,list_of_func_names_old,list_of_func_names_new,var_names_old, var_names_new)
    new_file_location = old_file_location.split(".")[0] + "_new_" + ".py"
    print("New File name: ", new_file_location)
    final_code = ast_to_python(final_code_ast)
    text_file = open(new_file_location, "w")
    n = text_file.write(final_code)
    text_file.close()


if __name__ == "__main__":
    main()
