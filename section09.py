# Section 09
# 파일 읽기, 쓰기
# 읽기 모드 : r(read), 쓰기 모드(기존 파일 삭제) : w(write), 추가 모드(파일 생성 또는 추가) : a(apeend)
# .. : 상대경로, . : 절대 경로

# 파일 읽기
# 예제 1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 변환
f.close()

print('----------------------------------------------------')

# 예제 2
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print('----------------------------------------------------')
print('----------------------------------------------------')

# 예제 3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print('----------------------------------------------------')
print('----------------------------------------------------')

# 예제 4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()  #내용이 없으니 > 이후로 글이 나오지 않는다.
    print(">", content) 

print('----------------------------------------------------')
print('----------------------------------------------------')

with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end = '### ')
        line = f.readline()

print('----------------------------------------------------')
print('----------------------------------------------------')

# 예제 6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents :
        print(c, end = ' ******** ')

print()

# 예제 7
score = []
with open('./resource/score.txt', 'r') as f :
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기

# 예제 1
with open('./resource/text1.txt', 'w') as f:
    f.write('Hey Their\n')

# 예제 2
with open('./resource/text1.txt', 'a') as f:
    f.write("What's up!\n")

# 예제 3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제 4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['Kim\n,', 'Park\n', 'Cho\n']
    f.writelines(list)

# 예제 5
# 파일로 로그를 찍을 때 쓰일 수 있는 내용
with open('./resource/text4.txt', 'w') as f:
    print('Test Contests! 1', file = f)
    print('Test Contests! 2', file = f)

print('----------------------------------------------------')
print('----------------------------------------------------')

