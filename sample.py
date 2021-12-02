def botapp():
    import os
    from dotenv import load_dotenv

    #時間を読み取るためのライブラリ
    import datetime

    #「.env」で定義した環境変数を使えるようにする。
    load_dotenv()

    #Botを動かすためのライブラリ
    from slack_bolt import App
    from slack_bolt.adapter.socket_mode import SocketModeHandler

    #アプリの初期化
    app = App(token=os.environ['SLACK_BOT_TOKEN'])

            
    #こんにちは！と送るとメンションしてこんにちはと返してくれる機能
    @app.message('こんにちは！')
    def message_hello(message, say):
        say(f'<@{message["user"]}> さん、こんにちは！')


    @app.message('今何時？')
    def clock(message, say):
        time_now = datetime.datetime.now().strftime('%H時%M分%S秒')
        say('現在' + time_now + 'です。')

            
            
    #アプリの起動
    if __name__ == '__main__':
        SocketModeHandler(app, os.environ['SLACK_APP_TOKEN']).start()


#00 ライブラリをインポート
import schedule
from time import sleep
from datetime import datetime,date

#01 定期実行する関数を準備
def task():
    botapp()
    
#02 スケジュール登録
schedule.every(30).seconds.do(task)

#02 何時まで実行するか定義
year   = date.today().year
month  = date.today().month
hour   = 22
minute = 0
second = 0
set_until_time = datetime(year,month,date.today().day,hour,minute,second)

#03 イベント実行 (特定の時間が来るまで定期実行)
while datetime.now() < set_until_time:
    schedule.run_pending()
    sleep(1)