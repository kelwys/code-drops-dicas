list_of_strings = ['python', 'python', 'python', 'python']

# Check if all elements are same
result = all(elem == list_of_strings[0] for elem in list_of_strings)
print(result)
# output: True

# Check if all elements are same to a specific value 
result = all(value == 'python' for value in list_of_strings)
print(result)
# output: True

result = all(value == 'java' for value in list_of_strings)
print(result)
# output: False