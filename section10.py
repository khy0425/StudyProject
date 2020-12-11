# Section 10
# Python 예외 처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만 , 코드 실행(런타임) 시 프로세스에서 발생하는 예외 처리도 중요
# IDE 에서 linter : 코드 스타일, 문법 체크를 도와줌

# SyntaxError : 잘못된 문법

# print('Test)

# if True
#     pass

# x => y

# NameError : 참조 변수 없음

a = 10
b = 15

# print(c)

# ZeroDivisionError : 0 나누기 에러
# print( 10 / 0 )

# IndexError : 인덱스 범위 오버

x = [10, 20, 30]
print(x[0])
# print(x[3]) # 인덱스 범위 예외 발생

# KeyError :

dic = {'name' : 'Kim', 'Age' : 33, 'City' : 'Seoul'}

# print(dic['hobby'])
print(dic.get('hobby'))

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시 예외

import time
print(time.time())
# print(time.month())

# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]

# x.remove(10)
# x.index(10)

# FileNotFoundError

# f = open('test.txt', 'r') # 예외 발생

#TypeError

x = [1, 2]
y = (1, 2)
z = 'test'

# print( x + y ) # 예외
# print(x + z)

# print(x + list(y)) # 형변환으로는 가능

# 항상 예외가 발생하지 않을 것으로 가정 후 코딩
# 그 후 실행 때 런타임 에러 발생 시 예외 처리 코딩을 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드에서 실행
# except : 에러명 1
# except : 에러명 2
# else :  에러가 발생하지 않았을 경우 실행
# finally : 항상 실행되는 구문

# 예제 1

name = ['Kim', 'Lee', 'Park']

# try:
#     z = 'Kim'
#     x = name.index(z)
#     print('{} Found it ! in name'.format(z, x+1))
# except ValueError:
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('OK! else!')

# 예제 2
try:
    z = 'Jin'
    x = name.index(z)
    print('{} Found it ! in name'.format(z, x+1))
except:
    print('Not found {}! - Occurred Error!'.format(z))
else:
    print('OK! else!')

# 예제 3
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it ! in name'.format(z, x+1))
except:
    print('Not found {}! - Occurred Error!'.format(z))
else:
    print('OK! else!')
finally:
    print('finally OK!')


# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print('OK Finally !!!!')

# 예제 5
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it ! in name'.format(z, x+1))
except ValueError as l:
    print(l) # as 를 활용하면 무슨 에러인지 print 시켜준다.
    print('Not found {}! - Value Error!'.format(z))
except IndexError:
    print('Not found {}! - IndexError Error!'.format(z))
except Exception:
    print('Not found {}! - Occurred Error!'.format(z))
else:
    print('OK! else!')

# 예제 6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try: 
    a = '333'
    if a == 'Kim' :
        print('OK 허가')
    else: 
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('OK !')