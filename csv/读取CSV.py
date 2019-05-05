import csv
#rb 是只读二进制打开
csvfile = open('2.csv','rt',encoding='UTF-8')
# print(csv.DictReader(csvfile))

header_rdr = csv.DictReader(csvfile)
header_rows = [h for h in header_rdr]
# print(header_rows[:2])

for header_row in header_rows:
    #获取键值对
    # for dkey,dval in header_row.items():
    for dval in header_row.values():
        print(dval)
    print("*"*50)
# for header_row in header_rows:
#     print(header_row['1510065000'],header_row['230.3800049'])

# reader = csv.reader(csvfile)
#
# for row in reader:
#     print(row)