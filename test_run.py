#coding: utf-8
#import sys
#sys.path.insert(0, ".")

#import logging
#logging.getLogger().setLevel(logging.INFO)

#環境変数を扱うためのライブラリ
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





# coding: utf-8

#from slackbot.bot import respond_to     # @botname: で反応するデコーダ
#from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
#from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない



#@respond_to('メンション')
#def mention_func(message):
#    message.reply('私にメンションと言ってどうするのだ') # メンション

#@listen_to('リッスン')
#def listen_func(message):
#    message.send('誰かがリッスンと投稿したようだ')      # ただの投稿
#    message.reply('君だね？')                           # メンション

#@respond_to('かっこいい')
#def cool_func(message):
#    message.reply('ありがとう。スタンプ押しとくね')     # メンション
#    message.react('+1')     # リアクション

#count = 0

#@default_reply()
#def default_func(message):
#    global count        # 外で定義した変数の値を変えられるようにする
#    count += 1
#    message.reply('%d 回目のデフォルトの返事です' % count)  # メンション

#@respond_to(r'^ping\s+\d+\.\d+\.\d+\.\d+\s*$')
#def ping_func(message):
#    message.reply('それはpingのコマンドですね。実行できませんが')   # メンション

#def_word = 'デフォルトの返事です'

#@default_reply()
#def default_func(message):
#    message.reply(def_word)     # def_wordの文字列を返す

#@respond_to(r'^set\s+\S.*')
#def set_default_func(message):
#    text = message.body['text']     # メッセージを取り出す
#    temp, word = text.split(None, 1)    # 設定する言葉を取り出す。tempには'set'が入る
#    global def_word     # 外で定義した変数の値を変えられるようにする
#    def_word = word     # デフォルトの返事を上書きする
#    msg = 'デフォルトの返事を以下のように変更しました。\n```' + word + '```'
#    message.reply(msg)


