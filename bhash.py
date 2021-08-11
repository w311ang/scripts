from flask import Flask
import subprocess
import time
import psutil
import _thread
from pytools import pytools
import re
app = Flask(__name__)

def starthash():
    global behash
    behash=subprocess.Popen('behash.exe')
    #print(get_pid('becard.exe'))
    time.sleep(3)
    for _ in range(60):
        time.sleep(1)
        if get_pid('becard.exe')==[]:
            #print(get_pid('becard.exe'))
            stop()
            start()
        else:
            return

def get_pid(name):
    '''
     作用：根据进程名获取进程pid
    '''
    re=[]
    pids = psutil.process_iter()
    #print("[" + name + "]'s pid is:")
    for pid in pids:
        if(pid.name() == name):
            re.append(pid.pid)
    return re

def kill(name):
    pid=get_pid(name)
    if pid!=[]:
        for i in pid:
            p=psutil.Process(i)
            p.terminate()
    else:
        return 'not running'

@app.route('/')
def status():
    pid=get_pid("becard.exe")
    if pid!=[]:
        p=psutil.Process(pid[0])
        gpustat=pytools.execCmd('nvidia-smi')
        gputemp=re.findall('[0-9]+C',gpustat)[0]
        return '%s, %s'%(p.status(),gputemp)
    else:
        return 'not running!!'

@app.route('/restart')
def restart():
    stop()
    time.sleep(3)
    starthash()
    return 'success'

@app.route('/start')
def start():
    if behash.poll()!=None:
        starthash()
        return 'success'
    else:
        return '已在运行'

@app.route('/stop')
def stop():
    behash.terminate()
    kill('becard.exe')
    return 'success'

def check():
    while True:
        text=pytools.execCmd('quser')
        for line in text.splitlines():
            if ('wangyg' in line) and ('运行中' in line):
                tmpstop()
        time.sleep(30)

def tmpstop():
    stop()
    time.sleep(60*60)
    start()

@app.route('/tmpstop')
def starttmpstop():
    _thread.start_new_thread(tmpstop,())
    return 'success'

if __name__ =="__main__":
    kill('behash.exe')
    kill('becard.exe')
    _thread.start_new_thread(starthash,())
    _thread.start_new_thread(check,())
    app.run(host='0.0.0.0',port=1234)
