import pymysql

def connection(host='127.0.0.1',
                            user='happyeon', password='123', 
                            charset='utf8', db='play'):
    try:
        con = pymysql.connect(host=host, 
                            user=user, password=password, 
                            charset=charset, db=db)
        cur = con.cursor()
    except Exception as e:

        print ("error ->", e)
    
    return cur,con

