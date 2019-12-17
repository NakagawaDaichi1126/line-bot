import json
import requests

def get_weather():
    #引用したい天気api
    url = "http://weather.livedoor.com/forecast/webservice/json/v1"

    # 大阪のcityタグのid
    #payload = {"city": "270000"}
    # 兵庫のcityタグのid
    payload = {"city": "280010"}

    # お天気情報をjsonで取得
    data = requests.get(url,params = payload).json()

    # お天気の情報を出力
    print("以下が{}の天気情報になります".format(data["location"]["city"]))

    for weather in data["forecasts"]:
        print("{}の天気は、{}でしょう".format(weather["dateLabel"],weather["telop"]))


if __name__=="__main__":
    get_weather()

