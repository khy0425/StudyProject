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