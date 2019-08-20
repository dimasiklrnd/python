import json

filename='lessons/files_and_exceptions/username.json'
with open(filename)as f_obj:
    username=json.load(f_obj)

print('С возвращением, ' + username)