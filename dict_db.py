import pymysql
import re

db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user="root",
                     password = 'jiaxiangdehe',
                     database="dict",
                     charset='utf8')

cur = db.cursor()


f = open('dict.txt')
sql = "insert into words (word,comment) values (%s,%s);"
for line in f:
    # pattern = r"\S+"
    # word_list = re.findall(pattern,line)
    # word = word_list[0]
    #
    # comment = " ".join(word_list[1:])
    # sql = "insert into words (word,comment) values (%s,%s);"
    # cur.execute(sql,[word,comment])
    pattern = r"(\S+)\s+(\.*)"
    temp = re.findall(pattern,line)
    try:
        cur.execute(sql,temp)
        db.commit()
    except Exception:
        db.rollback()

f.close()
cur.close()
db.close()

