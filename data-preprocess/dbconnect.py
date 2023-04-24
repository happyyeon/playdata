import pymysql


def connection(
    host="127.0.0.1", user="happyeon", password="123", charset="utf8", db="play"
):
    """
    host: temp
    return cur,con
    """
    try:
        con = pymysql.connect(
            host=host, user=user, password=password, charset=charset, db=db
        )
        cur = con.cursor()
    except Exception as e:

        print("error ->", e)

    return cur, con


def foo():
    print("함수를 호출했습니다.")


if __name__ == "__main__":
    print("위 함수가 잘 동작하는지 테스트 해보는 중입니다.")
    foo()
    print("잘 동작하네요!")
