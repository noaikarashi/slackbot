from slacker import Slacker
import weather
 
def main():
 
    dic_weather = {
        '晴れ' : 'sunny',
        '曇り' : 'cloud',
        '雨' : 'rain_cloud',
        '雪' : 'snow_cloud',
        '曇時々晴' : 'barely_sunny',
    }
 
    dic_date = {
        '今日': 0,
        '明日': 1,
        '明後日': 2
    }
 
    w = weather.get_weather(130010)
    t = w['forecasts'][dic_date['今日']]
    telop = t['telop']
 
    # 辞書にない天気が来たら絵文字に空文字を設定する
    if telop in dic_weather:
        emoji = ':' + dic_weather[telop] + ':'
    else:
        emoji = ""
 
　　　　　　　　# APIトークンを設定する
    slack = Slacker("xoxb-465993750257-2725436585474-iHg7n6zU0Z0Fni3jabIepAjj")
　　　　　　　　# Slackにメッセージを送信する
    slack.chat.post_message('timeline', '今日の天気は%sです%s' % (telop, emoji), as_user=True)
 
if __name__ == "__main__":
    main()