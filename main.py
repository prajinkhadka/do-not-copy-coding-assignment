from ast_to_json import make_ast 
from change_code import no_of_func, change_func_name, change_function_dec

data = make_ast("""
def sort():
    print("this is a sorting fucntion")
    
def search():
    print("this is a search fucntion")
    
def binary_search():
    print("this is a search fucntion")
    
def linear_search():
    print("this is a leareraefasdfhdsfhuh search fucntion")
    
s = sort() 
s1 = sort()
s2  = sort()
s3 = search()
linear = linear_search()
    
""")

count_no_f = no_of_func(data) 
data = change_func_name(data, count_no_f)
data = change_function_dec(data)

print(data)

# To Do: Convert json to AST -> Python
