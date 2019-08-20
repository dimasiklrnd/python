import json
filename = 'lessons/files_and_exceptions/numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)