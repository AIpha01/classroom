#-*- coding:utf-8 -*-

import requests
import re,os
import threading
import time

def store_path(path):
    path = path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    else:
        return False

def get_image(url):
    req = requests.get(url, timeout=30)
    return req.text

def save_images(req, name):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(req)
    for imageURL in imglist:
        splitPath = imageURL.split('/')
        fileName = splitPath[-1]
        print(fileName, 'Download Completes')
        dirName = name + "/" + fileName
        try:
            if "http:" in imageURL:
                rr = requests.get(imageURL)
            else:
                rr = requests.get('http:' + imageURL)
            data = rr.content
            f = open(dirName, 'wb+')
            f.write(data)
            f.close()
        except :
            continue

if __name__ == '__main__':
    Initial_page = input('The initial page: ')
    Final_page = input('The final page: ')
    print('Start Download')
    path = 'Imagines'
    store_path(path)

    for i in range(int(Initial_page),int(Final_page)+1):
        req = get_image("http://jandan.net/ooxx/page-%d#comments" % i)
        threading._start_new_thread(save_images, (req, path))
    input('press Enter to exit...\n')



