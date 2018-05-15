import requests
import itchat
from baiduyuyin import post_recording,text_to_audio

KEY = '1107d5601866433dba9599fac1bc0083'

'''备用KEY解决次数限制
8edce3ce905a4c1dbb965e6b35c3834d
eb720a8970964f3f855d863d24406576
1107d5601866433dba9599fac1bc0083
71f28bf79c820df10d39b4074345ef8c
'''


def get_response(msg):
    apiurl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiurl, data=data).json()
        return r.get('text')
    except:
        return


@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def tuling_reply1(msg):
    default_reply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    print(msg)
    return reply or default_reply


@itchat.msg_register(itchat.content.RECORDING,  isFriendChat=True)
def tuling_reply2(msg):
    msg['Text'](msg['FileName'])   # 下载语音
    recording_text = post_recording(msg['FileName'])
    reply_text = get_response(recording_text)
    itchat.send(reply_text,  msg['FromUserName'])


itchat.auto_login(hotReload=True)
itchat.run()
print('用微信扫描二维码登录，你就拥有自己的WeChat-Robot')