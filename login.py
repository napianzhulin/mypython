import pymysql

db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user="root",
                     password = 'jiaxiangdehe',
                     database="stu",
                     charset='utf8')
cur = db.cursor()

def register():
    name = input("请输入姓名：")
    passward = input("请输入密码：")
    sql = "select * from user where name = '%s';" % name
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return False
    try:
        sql = "insert into user (name,passward) values (%s,%s);"
        cur.execute(sql,[name,passward])
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        return  False

def login():
    name = input("请输入用户名：")
    passward = input("请输入密码：")
    sql = "select * from user where name = '%s' and passward = '%s';" % (name,passward)
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return True

while True:
    print("""
            =============================
              1.注册               2.登录
            =============================
    """)
    cmd = input("请选择登录还是注册：")
    if cmd == '1':
        if register():
            print("注册成功！")
        else:
            print("注册失败！")
    elif cmd =='2':
        if login():
            print("登录成功！")
            break
        else:
            print("登录失败！")
    else:
        print("输入错误，请重新输入！")


cur.close()
db.cursor()