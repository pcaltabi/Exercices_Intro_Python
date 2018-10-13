import sqlite3
import csv 

try:
    conn = sqlite3.connect('shop.db')
    cur = conn.cursor()
    #cur.execute("INSERT INTO articles VALUES (null, 'HARMONIEUSE', '2018 SpringSummer', 140, 10);")
    #conn.commit()
except Error as e:
    print('An error occurred with query')
    conn.rollback()
finally:
    conn.close()


