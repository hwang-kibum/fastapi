import pymysql

#전역변수 선언
conn=None
cur=None
sql=""

id="test"
userName="test"
email="tes@test.com"
bithYaer=""

conn=pymysql.connect( 
    host='localhost',
    port=3307, 
    user='root', 
    passwd='wlfks@09!', 
    db='test', 
    charset='utf8')#접속 정보
cur=conn.cursor() #커서 생성.

sql ="""
    CREATE TABLE IF NOT EXISTS userTable(
        id char(4) not null,
        userName char(10) not null,
        email char(15) not null,
        bithYear int not null,
        primary key(id)
        );""" #실행할 sql문
cur.execute(sql)#커서로 sql문 실행
conn.commit()
sql2 ="INSERT INTO userTable(id, userName, email, birthYear) VALUES('"+id+"','"+userName+"','"+email+"','"+bithYaer+"')"

cur.execute(sql2)
conn.commit() #저장


conn.close() #커넥션 종료