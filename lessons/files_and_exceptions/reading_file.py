file_read = 'lessons/files_and_exceptions/learning_python.txt'

with open(file_read) as string:
    for i in string:
        print(i.strip())


with open(file_read) as target:
    read=target.readlines()

print(read)

for i in read:
    print(i.strip())

r_string = ''
for i in read:
    r_string += i.rstrip()
print(r_string)

print(r_string[:25] + '...')

for i in read:
    print(i.replace('Python', 'C++').strip())
