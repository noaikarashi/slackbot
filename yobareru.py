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

def botapp_run():
    botapp()

#def message_teiki():
#    @app.message('こんにちは！')
#    def message_hello(message, say):
#        say(f'<@{message["user"]}> さん、こんにちは！')       

if __name__ == '__main__':#直接yobareru.pyを実行した時だけ、def test()を実行する
    botapp()
    botapp_run()

print('モジュール名：{}'.format(__name__))  #実行したモジュール名を表示する