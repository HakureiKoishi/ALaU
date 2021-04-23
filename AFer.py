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
    print("""当前版本号：Beta Version 1.0 [2021.4.24]

!重要!：
1.AZFileLocker&FileUnlocker Beta测试版正式上线

消息：
“能在五一前完成所有基本功能并上线测试版真的是非常令我激动呢（笑）。”
“另外，如果有遇到bug请向我反馈”

更新：
1.新增「关于」与「更新日志」
更多功能开发中...

修复：
1.「解密加密容器」的功能现在一切正常（应该）
更多头发失去中...

编辑时间：2021.4.24-1:24 by HKRTree""")
    print("")
    input("按任意键继续")
    second = 3
    for i in range(second,0,-1):
        print("\r"+'>>此页还将展示'+str(second)+'秒<',end="")
        time.sleep(1)
        second -= 1
