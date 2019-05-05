import json

# file = open('job.json','r')

# for line in file.readline():
#     # dic = json.loads(line)
#     print(line)
# print(json.loads(file.readline()))
with open('job.json','r')as fp:
    row = fp.readline()
    while row:
        persons = json.loads(row)
        print(persons)
        row = fp.readline()

