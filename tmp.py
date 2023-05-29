import requests 
url = "https://api.finance.naver.com/siseJson.naver?symbol=011200&requestType=1&startTime=20210710&endTime=20220317&timeframe=day"
r = requests.post(url)
stock = eval(r.text.strip())