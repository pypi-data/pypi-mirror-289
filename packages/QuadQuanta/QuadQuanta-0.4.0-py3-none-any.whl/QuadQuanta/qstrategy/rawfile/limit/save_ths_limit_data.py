# 同花顺涨停数据
import csv

if __name__ == '__main__':
    with open("2022-05-26.csv") as csvfile:
        test2 = csv.reader(csvfile)
        for row in test2:
            print(row)
