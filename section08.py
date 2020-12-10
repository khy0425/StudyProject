# Section 08
# 파이썬 모둘과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리로 이동
# .  : 현재 디렉토리


# 사용 1(클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print('ex1 : ', Fibonacci.fib2(400))
print('ex1 : ', Fibonacci().title)

# 사용 2(클래스)
from pkg.fibonacci import * # 필요하지 않은 것은 메모리 낭비가 될 수 있음으로 권장하지 않음

Fibonacci.fib(500)

print('ex2 : ', Fibonacci.fib2(600))
print('ex2 : ', Fibonacci().title)

# 사용 3(클래스)
from pkg.fibonacci import Fibonacci as fb

Fibonacci.fib(1000)

print('ex3 : ', Fibonacci.fib2(1600))
print('ex3 : ', Fibonacci().title)

# 사용 4(함수)
import pkg.calculations as c

print('ex 4: ', c.add(10, 100))
print('ex 4: ', c.mul(10, 100))


# 사용 5(함수)
from pkg.calculations import div as d  # 필요 한 것만 가져와서 사용하는 것이 코드상 명시적으로도 리소스량으로도 좋다
print('ex5 : ', int(d(100,10)))

# 사용 6
import pkg.prints as p
import builtins
p.prt1()
p.prt2()
# print(dir(builtins))