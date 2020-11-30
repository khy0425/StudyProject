# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon

print('apple;orange;banana;lemon')
# 3. 화면에 * 기호 100개를 표시하세요.
print('*' * 100)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
TT = "30"
print(int(TT))
print(float(TT))
print(complex(TT))
print(str(TT))
# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
Question = "Niceman"
print(Question[-3:])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
Question2 = "Strawberry"
print(Question2[::-1])

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
Question3 = '010-7777-9999'
print(Question3[0:3] + Question3[4:8] + Question3[9:13])

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
Q4 = "http://daum.net".lstrip("http://")
print(Q4)

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
Q5 = "NiceMan"
Q5_Up = Q5.upper()
Q5_Low = Q5.lower()

print(Q5_Up)
print(Q5_Low)

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
Q6 = "abcdefghijklmn"
print(Q6[2:5])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
Q7 = ["Banana", "Apple", "Orange"]

Q7.remove("Apple")

print(Q7)

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)

Q8 = (1,2,3,4)
Q8_list = list(Q8)
print(Q8_list)

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
Q9 = {"성인" : 100000 , "청소년" : 70000 , "아동" : 30000}
print(Q9)

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
Q9['소아'] = 0
print(Q9)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
for i in Q9.keys():
    print(i)

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(list(Q9.values()))

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
