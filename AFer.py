import os
import time
import shutil
import zipfile
from os.path import join, getsize
import winreg
import binascii
import sys
def AFer():
    os.system("cls")
    print("")
    print("""当前版本号：Version 1.0 [2021.5.4]

!重要!：
1.AZFileLocker&FileUnlocker 正式版上线

消息：
“能在期限内上线正式版真的非常令我激动呢（笑）。”
“其实Beta测试版在五一前一个星期就已完成，实际上是程序的封装耗了很长时间”
“另外，如果有遇到bug请向我反馈”

更新：
1.我们有图标了
更多功能开发中...

修复：
1.暂无
更多头发失去中...

编辑时间：2021.5.4-14：14 by HKRTree""")
    print("")
    input("按任意键继续")
    second = 3
    for i in range(second,0,-1):
        print("\r"+'>>此页还将展示'+str(second)+'秒<',end="")
        time.sleep(1)
        second -= 1
