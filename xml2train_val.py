#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2017/10/13 0013'
"""
import os
import random

trainval_percent = 0.75
train_percent = 0.66
xmlfilepath = 'Annotations'
txtsavepath = 'ImageSets/Main'
if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)
total_xml = os.listdir(xmlfilepath)

num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train = random.sample(trainval,tr)

ftrainval = open(r'ImageSets/Main/trainval.txt','w')
ftrain = open(r'ImageSets/Main/train.txt', 'w')
fval = open(r'ImageSets/Main/val.txt', 'w')
ftest = open(r'ImageSets/Main/test.txt', 'w')

for i  in list:
    name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
print('over!')

