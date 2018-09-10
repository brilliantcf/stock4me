#coding=utf-8
#这里需要引入三个模块
import time, os, sched

# 以需要的时间间隔执行某个命令

import time, os

def re_exe(cmd, inc = 60):
    while True:
        os.system(cmd);
        time.sleep(inc)

re_exe("echo %time%", 5)