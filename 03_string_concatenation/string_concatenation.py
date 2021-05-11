name = 'John Doe'

# 1 Using + operator
string = 'The name is ' + name
print(string)
# output: The name is John Doe

# 2 Using % operator
string = 'The name is %s' %name
print(string)
# output: The name is John Doe

# 3 Using f-string (Literal String Interpolation)
string = f'The name is {name}'
print(string)
# output: The name is John Doe

# 4 Using format() function
string = 'The name is {}'.format(name)
print(string)
# output: The name is John Doe