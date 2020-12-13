# Section 11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MINE - text/csv
import csv

# 예제 1
with open ('./resource/sample1.csv') as f:
    reader = csv.reader(f)
    # next(reader) # 패싱하기 위해 사용 (해더 스킵용도)

    # 확인
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader :
        print(c)


# 예제 2
with open ('./resource/sample2.csv') as f:
    reader = csv.reader(f, delimiter = '|') # delimiter 는 문자열을 기준으로 스플릿 해서 보여줌
    # next(reader) # 패싱하기 위해 사용 (해더 스킵용도)

    # 확인
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader :
        print(c)

# 예제 3 (Dict 변환)
# Key, Value 값으로 저장이 가능하다.
with open ('./resource/sample1.csv') as f:
    reader = csv.DictReader(f)

    for c in reader : 
        for k, v in c.items():
            print(k, v)
        print('---------------------------')

# 예제 4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15,],[16, 17, 18]]

with open ('./resource/sample3.csv', 'w', newline= '') as f: # 대용량을 사용 할 때 자동 줄바꿈을 방지할 수 있는 것이 newline
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)


# 예제 5
with open ('./resource/sample4.csv', 'w', newline= '') as f:
    wt = csv.writer(f)
    wt.writerows(w)

# XSL, XLSX
# openpyxl, xlswriter, xlrd, xlutils
# pandas 를 주로 사용 (openpyxl, xlrd)
# pip install op... , xlrd, pandas

# >> 해당 read_excel은 Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or conda to install xlrd.
# 오류로 확인이 불가능

# import pandas as pd

# # sheetname = '시트명' 또는 숫자, header = 숫자, skiprow = 숫자
# xlsx = pd.read_excel('./resource/sample.xlsx')

# # 상위 데이터 확인
# print(xlsx.head())

# # 데이터 확인
# print(xlsx.tail())

# # 데이터 확인
# print(xlsx.shape) # 행, 열

# xlsx.to_csv('./resource/result.xlsx', index = False)