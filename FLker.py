#-----------------------引用-----------------------
import os
import time
import shutil
import zipfile
from os.path import join, getsize
import winreg
import pyzipper
import binascii
import sys
def FileLocker():
#-----------------------定义-----------------------
    #↓解压缩↓
    def unzip_file(zip_src, dst_dir):
        r = zipfile.is_zipfile(zip_src)
        if r:
            fz = zipfile.ZipFile(zip_src, 'r')
            for file in fz.namelist():
                fz.extract(file, dst_dir)
        else:
            print('This is not zip')
    #zip_src:是zip文件的全路径
    #dst_dir：是要解压到的目的文件夹

    #↓解压缩加密-不支持AES↓
    def unzip_file_WithPassword_WithoutAES(FilePassWord,zip_src,dst_dir):
        zip_file = zipfile.ZipFile(zip_src)  # 文件的路径与文件名
        zip_list = zip_file.namelist()  # 得到压缩包里所有文件
        for f in zip_list:
            zip_file.extract(f,dst_dir, pwd=str(FilePassWord).encode("utf-8"))  # 循环解压文件到指定目录
        zip_file.close()  # 关闭文件，必须有，释放内存

    #↓解压缩加密-支持AES#
    def unzip_file_WithPassword_WithAES(FilePassWord,zip_src,dst_dir):
        with pyzipper.AESZipFile(zip_src,'r',compression=pyzipper.ZIP_LZMA,encryption=pyzipper.WZ_AES) as zf:
            zf.extractall(path=dst_dir, pwd=str(FilePassWord).encode("utf-8"))

    #↓加密压缩↓
    def zip_file_WithPassword(password, dirpath, outFullName):
        #password#密码
        #dirpath#待压缩的文件路径及文件
        #outFullName#压缩文件的输出路径及文件名
        cmd = r'C:\"Program Files"\WinRAR\WinRAR.exe a -y -ibck -p%s %s %s' % (password, outFullName, dirpath)#password为压缩密码
        os.system(cmd)
    #-----------------------程序-----------------------
    os.system("cls")
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
    Desktop = winreg.QueryValueEx(key, "Desktop")[0]

    # File = Desktop+r'\233'
    # print(File)
    # File_Ziped = Desktop+r'\test.zip'
    # print(File_Ziped)
    # zip_file_WithPassword('a123be', File, File_Ziped)
    #unzip_file_WithPassword_WithAES(123,File_Ziped,r'C:\Users\ss2007ghc\Desktop\AZFileLocker')

    if os.path.exists(Desktop+r'\请把需要加密的文件放入此文件夹'):
        print("读取文件夹已存在于桌面，！请将根据文件夹内的> Readme.txt <的指引进行操作 ！然后再执行下一步")
        pass
    else:
        print("读取文件夹已在桌面创建，！请将根据文件夹内的> Readme.txt <的指引进行操作 ！然后再执行下一步")
        os.makedirs(Desktop+r'\请把需要加密的文件放入此文件夹')
        file = open(Desktop+r'\请把需要加密的文件放入此文件夹\Readme.txt','w')
        readme = '''>本程序尚处于开发测试版本，使用该程序进行加密或解密前，请做好文件备份以防止不必要的意外损失<
    ！请勿移动任何程序生成的文件夹的路径 !
    *请勿在桌面仍保留> 加密文件容器.AZLocked <为名的文件的情况下进行本次加密，否则本次加密将无法生效*
    读取文件夹使用说明：将需要加密的文件放入此文件夹中
    密钥文件夹使用说明：请把需要当做密钥的文件放入密钥文件夹（密钥文件夹内必须且只能存在一个文件，不限后缀）目前只能使用密钥文件加密，请妥善保存！'''
        file.write(readme)
        file.close()
    if os.path.exists(Desktop+r'\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）'):
        pass
    else:
        os.makedirs(Desktop+r'\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）')
    Choice = input("是否完成文件的放置?(Y/N):")
    if Choice == "Y"or"y":
        #↓一次加密↓
        keyfile_list = os.listdir(Desktop+r'\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）')
        print("使用："+str(keyfile_list)+" 为密钥进行一次加密")
        try:
            keyfile = keyfile_list[0]
        except:
            quit()
        with open(Desktop+r"\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）\\"+str(keyfile), 'rb') as f:
            content = f.read()
        ZipPassword = binascii.hexlify(content)
        ZipPassword = ZipPassword[:8017]
        File = Desktop+r'\请把需要加密的文件放入此文件夹'
        #print(File)
        File_Ziped = r'C:\Users\Public\Documents'+r'\LockedX1.zip'
        #print(File_Ziped)
        zip_file_WithPassword(str(ZipPassword),File, File_Ziped)
        #↓二次加密↓
        keyfile_list = os.listdir(Desktop+r'\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）')
        print("使用："+str(keyfile_list)+" 为密钥进行二次加密")
        keyfile = keyfile_list[0]
        with open(Desktop+r"\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）\\"+str(keyfile), 'rb') as f:
            content = f.read()
        ZipPassword = binascii.hexlify(content)
        ZipPassword = ZipPassword[-8020:]
        File = r'C:\Users\Public\Documents'+r'\LockedX1.zip'
        #print(File)
        File_Ziped = r'C:\Users\Public\Documents'+r'\LockedX2.zip'
        #print(File_Ziped)
        zip_file_WithPassword(str(ZipPassword),File, File_Ziped)
        if os.path.exists(r'C:\Users\Public\Documents'+r'\LockedX1.zip'):
            os.remove(r'C:\Users\Public\Documents'+r'\LockedX1.zip')
            #"压缩包已删除"
        else:
            pass
            #"找不到旧版数据压缩包"
        #↓三次加密↓
        keyfile_list = os.listdir(Desktop+r'\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）')
        print("使用："+str(keyfile_list)+" 为密钥进行三次加密")
        keyfile = keyfile_list[0]
        with open(Desktop+r"\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）\\"+str(keyfile), 'rb') as f:
            content = f.read()
        ZipPassword = binascii.hexlify(content)
        ZipPassword = ZipPassword[8037:15000]
        File = r'C:\Users\Public\Documents'+r'\LockedX2.zip'
        #print(File)
        File_Ziped = r'C:\Users\Public\Documents'+r'\LockedX3.zip'
        #print(File_Ziped)
        zip_file_WithPassword(str(ZipPassword),File, File_Ziped)
        if os.path.exists(r'C:\Users\Public\Documents'+r'\LockedX2.zip'):
            os.remove(r'C:\Users\Public\Documents'+r'\LockedX2.zip')
            #"压缩包已删除"
        else:
            pass
            #"找不到旧版数据压缩包"
        #↓四次加密↓
        keyfile_list = os.listdir(Desktop+r'\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）')
        print("使用："+str(keyfile_list)+" 为密钥进行四次加密")
        keyfile = keyfile_list[0]
        with open(Desktop+r"\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）\\"+str(keyfile), 'rb') as f:
            content = f.read()
        ZipPassword = binascii.hexlify(content)
        ZipPassword = ZipPassword[16074:23897]
        File = r'C:\Users\Public\Documents'+r'\LockedX3.zip'
        #print(File)
        File_Ziped = r'C:\Users\Public\Documents'+r'\LockedX4.zip'
        #print(File_Ziped)
        zip_file_WithPassword(str(ZipPassword),File, File_Ziped)
        if os.path.exists(r'C:\Users\Public\Documents'+r'\LockedX3.zip'):
            os.remove(r'C:\Users\Public\Documents'+r'\LockedX3.zip')
            #"压缩包已删除"
        else:
            pass
            #"找不到旧版数据压缩包"
        #↓五次加密↓
        keyfile_list = os.listdir(Desktop+r'\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）')
        print("使用："+str(keyfile_list)+" 为密钥进行五次加密")
        keyfile = keyfile_list[0]
        with open(Desktop+r"\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）\\"+str(keyfile), 'rb') as f:
            content = f.read()
        ZipPassword = binascii.hexlify(content)
        ZipPassword = ZipPassword[24110:31497]
        File = r'C:\Users\Public\Documents'+r'\LockedX4.zip'
        #print(File)
        File_Ziped = r'C:\Users\Public\Documents'+r'\LockedX5.zip'
        #print(File_Ziped)
        zip_file_WithPassword(str(ZipPassword),File, File_Ziped)
        if os.path.exists(r'C:\Users\Public\Documents'+r'\LockedX4.zip'):
            os.remove(r'C:\Users\Public\Documents'+r'\LockedX4.zip')
            #"压缩包已删除"
        else:
            pass
            #"找不到旧版数据压缩包"
        #↓最终加密↓
        keyfile_list = os.listdir(Desktop+r'\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）')
        print("使用："+str(keyfile_list)+" 为密钥进行最终加密")
        keyfile = keyfile_list[0]
        with open(Desktop+r"\请把需要加密的文件放入此文件夹\请把任意文件放入此文件夹中以作为密钥文件（加密用）\\"+str(keyfile), 'rb') as f:
            content = f.read()
        ZipPassword = binascii.hexlify(content)
        ZipPassword = ZipPassword[-16075:-8100]
        File = r'C:\Users\Public\Documents'+r'\LockedX5.zip'
        #print(File)
        File_Ziped = r'C:\Users\Public\Documents'+r'\LockedFinal.zip'
        #print(File_Ziped)
        zip_file_WithPassword(str(ZipPassword),File, File_Ziped)

        if os.path.exists(Desktop+r'\加密文件容器.AZLocked'):
            print("!桌面已存在一未改名加密容器，请对其进行改名或将其转移至其他目录,本次加密无效!")
            pass
        else:
            os.rename(r'C:\Users\Public\Documents'+r'\LockedFinal.zip',Desktop+r'\加密文件容器.AZLocked')
        if os.path.exists(r'C:\Users\Public\Documents'+r'\LockedX5.zip'):
            os.remove(r'C:\Users\Public\Documents'+r'\LockedX5.zip')
            #"压缩包已删除"
        else:
            pass
            #"找不到旧版数据压缩包"
        if os.path.exists(Desktop+r'\请把需要加密的文件放入此文件夹'):
            shutil.rmtree(Desktop+r'\请把需要加密的文件放入此文件夹')
            time.sleep(0.7)
            #"旧版数据文件已删除"
        else:
            time.sleep(0.7)
            #"找不到旧版数据文件"
        if os.path.exists(r'C:\Users\Public\Documents'+r'\LockedFinal.zip'):
            os.remove(r'C:\Users\Public\Documents'+r'\LockedFinal.zip')
            #"压缩包已删除"
        else:
            pass
            #"找不到旧版数据压缩包"
        print("已完成加密！")
        second = 3
        for i in range(second,0,-1):
            print("\r"+' >>'+str(second)+'秒后退出<',end="")
            time.sleep(1)
            second -= 1
    elif Choice == "N"or"n":
        quit()
    else:
        print("请输入有效指令!")
