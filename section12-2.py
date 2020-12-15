# Section 12 - 2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 생성)
conn = sqlite3.connect('C:/python_basic/resource/database.db')

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
#print('One -> \n' , c.fetchone())

# 지정 로우 선택
#print('Three -> \n', c.fetchmany(size= 3))

# 전체 로우 선택
#print('All -> \n', c.fetchall()) # 커서는 불러온 것의 위치를 기억한다.


# 순회 1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve > ', row)

# 순회 2
# for row in c.fetchall():
#     print('retrieve2 > ', row)

# 순회 3 역순으로
for row in c.execute('SELECT * From users ORDER BY id desc'):
    print('retrieve3 > ', row)

print()

# WHERE Retrieve1
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?', param1)

print('param1',c.fetchone())
print('param1',c.fetchall()) # 3번은 하나밖에 없음으로 데이터가 없다.(커서)

# WHERE Retrieve2
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' %param2) # %s(String), %f(Float), %d(integer)

print('param2',c.fetchone())
print('param2',c.fetchall()) #데이터 없음

# WHERE Retrieve3
c.execute('SELECT * FROM users WHERE id=:ID', {"ID" : 5}) # %s(String), %f(Float), %d(integer)

print('param3',c.fetchone())
print('param3',c.fetchall()) #데이터 없음

# Where Retrieve4
param4 = (3, 5)
c.execute('SELECT * FROM users WHERE id IN(?, ?)', param4)
print('param4', c.fetchall())

# Where Retrieve5
c.execute('SELECT * FROM users WHERE id IN("%d", "%d")'% (3, 4))
print('param4', c.fetchall())

# Where Retrieve6
c.execute('SELECT * FROM users WHERE id=:id1 OR id=:id2', {'id1' : 2, 'id2' : 5})
print('param4', c.fetchall())

# Dump 출력 (데이터베이스 백업) 덤프를 떠온다고 한다. / 데이터가 많아지면 분할이 필요하다.
with conn:
    with open('./resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')

# f.close(), conn.close() 도 with 문으로 인하여 자동으로 완료되었다.