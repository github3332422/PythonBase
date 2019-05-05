import xlwt as ExcelWrite


def writeXLS(file_name):
    value = [["name", "jim", "hmm", "lilei"], ["sex", "man", "woman", "man"], ["age", 19, 24, 24],
             ["country", "USA", "CHN", "CHN"]]
    xls = ExcelWrite.Workbook()
    sheet = xls.add_sheet("Sheet2")

    for i in range(0, 4):
        for j in range(0, len(value)):
            sheet.write(j, i, value[i][j])
    xls.save(file_name)


if __name__ == "__main__":
    writeXLS("test_write.xls");