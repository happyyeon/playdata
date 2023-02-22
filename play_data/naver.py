import requests
import pandas as pd 

def get_stock(code, page):
    naver_url = "https://finance.naver.com/item/sise_day.naver?code={}&page={}"
    head = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
    r= requests.get(naver_url.format(code,page),headers=head)
    return pd.read_html(r.text)[0].dropna()

if __name__ == "__main__":
    print("haha")