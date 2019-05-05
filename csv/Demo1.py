import csv

csvfile = open('mn_headers.csv','rt',encoding='UTF-8')
reader = csv.reader(csvfile)
#存放的是简写名和全名，全部的数据
dict = {}
for row in reader:
    # print(row[0],'\t',row[1])
    dict[row[0]] = row[1]
csvfile.close()
print(len(dict))


file = open('mn.csv','rt',encoding='UTF-8')
reader = csv.reader(file)
header = [h for h in reader]
headers = header[0:1]
# print(header[0:1][0][1:-1])
print(len(header[0:1][0][1:-1]))

list_full = []
for header in headers:
    for row in header[1:-1]:
        # print(row)
        print(row,dict.get(row, None))
        print("*"*50)
        list_full.append(dict.get(row, None))

# for lis in list_full:
#     print(lis)
