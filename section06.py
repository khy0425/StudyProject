# Section 06
# 파이선 함수식 및 람다 (lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제 1.


def hello(world):
    print("Hello", world)


hello("Python")
hello(7777)

# 예제2


def hello_return(world):
    val = "Hello" + str(world)
    return val


str = hello_return("Python !!!")
print(str)

# 예제 3( 다중 리턴 )


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = func_mul(100)
print(val1, val2, val3, type(val1))

# 예제 4( 데이터 타입 반환)


def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


lt = func_mul2(100)
print(lt, type(lt))


# 예제 4
# *args, *kwargs

# args = 다양한 매개변수 몇개가 들어갈 지 모르겠는 방식을 사용 할 때 사용

def args_func(*args):
    # for t in args :
    #     print(t)
    for i, v in enumerate(range(10)):   # index를 붙일 때 사용하는 방식
        print(i, v)


args_func('kim')
args_func('kim', 'Park')
args_func('kim', 'Park', 'Lee')

# kwargs
# args처럼 가변인자가 몇개가 들어가던 유연하게 들어갈 수 있음
# *가 하나일 땐 튜플로 ** 일 땐 딕셔너리로 받는 형식

def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


kwargs_func(name='kim')
kwargs_func(name='kim', name2='Park', name3='Lee')


# 전체 혼합

def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(10, 20) #args 는 가변인자가 없어도 실행이 가능
example_mul(10, 20, 'park', 'kim', age1=24, age2=35) #인자를 넣으면 갯수가 몇개라도 튜플형, 딕셔너리형으로 받아 올 수 있다.

# 중첩함수( 클로저 )

# 데코레이터 검색 요망


def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print("in func")
    func_in_func(num + 10000)


nested_func(10000)

# 힌트 ( x : 자료형) -> 자료형
# 예외는 발생시키지는 않지만 어떤 자료형을 기입하고 어떤자료형으로 출력이 되는지를 힌트로 보여주는 방식

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리로스 (메모리) 할당
# 람다는 즉시 실행( Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당


def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))

# 람다는 익명함수를 사용할 때 사용

lambda_mul_10 = lambda num: num * 10

print('>>>>>',lambda_mul_10(10))

def func_final(x, y, func):
    print( x * y * func(10))

func_final(10, 10, lambda_mul_10)


print(func_final(10, 10, lambda x : x * 1000))