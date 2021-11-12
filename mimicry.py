import base64
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import time
import datetime
try:
    Tk().withdraw()
    filename = askopenfilename()
    with open(filename,'r')as file:
        file.seek(0, os.SEEK_END)
        print("file size: ", file.tell(), "bytes")
    start_time = time.time()
    data = ''
    print('reading file')
    read_time = time.time()
    print('readfile time cost: %s' % (read_time-start_time))
    print('file converting')
    with open(filename, 'rb')as file:
        data = file.read()
        data = base64.b64encode(data)
        data = str(data, 'utf-8')
    temp = []
    for x in data:
        temp.append(x)
    fin = []
    for x in temp:
        fin.append(ord(x))
    for x in range(len(fin)):
        fin[x] = format(fin[x], 'b')
    for x in range(len(fin)):
        fin[x] = fin[x].replace('0', '‌')  # 8204
        fin[x] = fin[x].replace('1', '​')  # 8203
    convert_time = time.time()
    print('file converting time cost: %s' % (convert_time-read_time))
    space = '‍'  # 8205
    print('start combining')
    res = space.join(fin)
    with open('mimesis.txt', 'w')as file:
        file.write(res)
    combind_time = time.time()
    print('combinding time cost: %s' % (combind_time-convert_time))
    print('finished')
    end_time = time.time()
    cost = end_time-start_time
    print('total time cost:' + str(datetime.timedelta(seconds=cost)))
except:
    pass
