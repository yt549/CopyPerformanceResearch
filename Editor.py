import sys
import shutil
from threading import Thread
from datetime import datetime
import os
import glob
from multiprocessing import Process
import subprocess

'''
Author: Yingkai tan
Objective: This source code is try to compare five different approach to copy 
my *.py code to another directory. Compare their time and output the time respectively

sample output would be:
shutil copyfile():  0:00:00.023392
shutil CopyObj():  0:00:00.018553
thread:  0:00:00.012101
muliple process:  0:00:00.114032
subprocess:  0:00:00.003632

the best performance to worst performance:  ['shutil CopyObj()', 'shutil copyfile()', 'subprocess' 'thread', 'muliple process']
'''
def clear_files():
    files = glob.glob("/Users/tanyingkai/Desktop/Neeva/CopyTo/*")
    for f in files:
        os.remove(f)

def copy1_shutil_CopyFile():
    dir_src = "/Users/tanyingkai/Desktop/Neeva/CopyFrom"
    dir_dst = "/Users/tanyingkai/Desktop/Neeva/CopyTo"
    try:
        for filename in os.listdir(dir_src):
            if filename.endswith('.py'):
                shutil.copy(dir_src + '/' + filename, dir_dst)

    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit(1)
    except:
        print("Unexpected error:", sys.exc_info())
        exit(1)

def copy2_shutil_CopyObj(dir_src = "/Users/tanyingkai/Desktop/Neeva/CopyFrom", dest = "/Users/tanyingkai/Desktop/Neeva/CopyTo", buffer_size=16000):
    try:
        for filename in os.listdir(dir_src):
            if filename.endswith('.py'):
                with open(dir_src + '/' + filename, 'rb') as fsrc:
                    with open(dest + '/' + filename, 'wb') as fdest:
                        shutil.copyfileobj(fsrc, fdest, buffer_size)

    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit(1)
    except:
        print("Unexpected error:", sys.exc_info())
        exit(1)


def copy3_Thread():
    dir_src = "/Users/tanyingkai/Desktop/Neeva/CopyFrom"
    dir_dst = "/Users/tanyingkai/Desktop/Neeva/CopyTo"
    for filename in os.listdir(dir_src):
        if filename.endswith('.py'):
            Thread(target=shutil.copy, args=[dir_src + '/' + filename, dir_dst + '/' + filename]).start()

def copy4_Multi_Process():
    dir_src = "/Users/tanyingkai/Desktop/Neeva/CopyFrom"
    dir_dst = "/Users/tanyingkai/Desktop/Neeva/CopyTo"
    for filename in os.listdir(dir_src):
        if filename.endswith('.py'):
            Process(target=shutil.copy, args=[dir_src + '/' + filename, dir_dst + '/' + filename]).start()

def copy5_Subprocess():
    dir_src = "/Users/tanyingkai/Desktop/Neeva/CopyFrom"
    dir_dst = "/Users/tanyingkai/Desktop/Neeva/CopyTo"
    for filename in os.listdir(dir_src):
        if filename.endswith('.py'):
            src = dir_src + '/' + filename
            dst = dir_dst + '/' + filename
            cmd = 'copy "%s" "%s"' % (src, dst)

    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    time_table = []
    # test 1
    t1_start = datetime.now()
    copy1_shutil_CopyFile()
    t1_end = datetime.now()-t1_start
    print("shutil copyfile(): ", t1_end)
    # clear
    clear_files()
    time_table.append([t1_end, "shutil copyfile()"])

    # test 2
    t2_start = datetime.now()
    copy2_shutil_CopyObj()
    t2_end = datetime.now() - t2_start
    print("shutil CopyObj(): ", t2_end)

    # clear
    clear_files()
    time_table.append([t2_end, "shutil CopyObj()"])

    # test 3
    t3_start = datetime.now()
    copy3_Thread()
    t3_end = datetime.now() - t3_start
    print("thread: ", t3_end)
    # clear
    clear_files()
    time_table.append([t3_end, "thread"])

    # test 4
    t4_start = datetime.now()
    copy4_Multi_Process()
    t4_end = datetime.now() - t4_start
    print("muliple process: ", t4_end)
    # clear
    clear_files()
    time_table.append([t4_end, "muliple process"])

    # test 5
    t5_start = datetime.now()
    copy5_Subprocess()
    t5_end = datetime.now() - t5_start
    print("subprocess: ", t5_end)
    # clear
    clear_files()
    time_table.append([t5_end, "subprocess"])

    time_table.sort(key = lambda x:x[0])

    print("the best performance to worst performance: ", [i[1] for i in time_table])


