import base64
import datetime
import time
import os
try:
    print('please enter your file\'s extension, for example: jpg png txt or .jpg .png .txt...')
    ext = input()
    if '.'not in ext:
        ext = '.'+ext
    data = ''
    with open('mimesis.txt','r')as file:
        file.seek(0, os.SEEK_END)
        print("file size: ", file.tell(), "bytes")
    start_time = time.time()
    with open('mimesis.txt', 'r')as file:
        data = file.read()
    data.replace('\n', '')
    data = data.split('‍')
    for x in range(len(data)):
        data[x] = data[x].replace('​', '1')
        data[x] = data[x].replace('‌', '0')
    for x in range(len(data)):
        data[x] = chr(int(data[x], 2))
    fin = ''
    read_convert_time = time.time()
    print('file reading and converting time cost: %s' %
          (read_convert_time-start_time))
    print('start combinding and translating')
    for x in data:
        fin += x
    data = base64.b64decode(fin)
    combinding_and_translating_time = time.time()
    print('combing and translating time cost: %s' %
          (combinding_and_translating_time-read_convert_time))
    with open('ori%s' % ext, 'wb')as file:
        file.write(data)
    end_time = time.time()
    cost = end_time-start_time
    print('time cost:' + str(datetime.timedelta(seconds=cost)))
    with open('mimesis.txt', 'w') as file:
        file.write('nothing there')
except:
    pass
