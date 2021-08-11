import itchat, time, random, _thread, os, pickle
from itchat.content import *

def refresh():
    while True:
        itchat.get_friends(update=True)
        print('刷新完成')
        time.sleep(5*60)

olddate=''
randnum=0
def rand():
    global date, randnum, olddate
    newdate=time.strftime("%Y%m%d", time.localtime())
    if newdate==olddate:
        return randnum
    else:
        randnum=8+random.randint(0,9)
        olddate=newdate
        return randnum

os.environ['NO_PROXY'] = 'webpush.wx.qq.com'
try:
    with open('signined.txt','rb') as f:
        signined=pickle.load(f)
except FileNotFoundError:
    signined=[]

@itchat.msg_register(TEXT, isGroupChat=True)
#@itchat.msg_register(TEXT)
def text_reply(msg):
    global signined
    text=msg.text
    if ('#接龙' in text) or ('＃接龙' in text) and ('平安' in text) and (not '%s平安'%realname in text):
        date=time.strftime("%Y%m%d", time.localtime())
        print('已签到：'+str(signined))
        if not date in signined:
            print('随机名次：'+str(rand()))
            lines=text.splitlines()
            lastline=lines[-1]
            #print(lastline)
            number=int(lastline.split('.')[0])
            mynum=number+1
            if mynum>=rand():
                mytext=text+'\n%s. %s平安'%(mynum,realname)
                msg.user.send(mytext)
                signined.append(date)
                with open('signined.txt','wb') as f:
                    pickle.dump(signined,f)

itchat.auto_login(hotReload=True)
_thread.start_new_thread(refresh,())
itchat.run(True)
