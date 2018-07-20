'''
Created on May 17, 2018

@author: Heng.Zhang
'''

import sys
import time
import numpy as np
import logging

runningPath = sys.path[0]
sys.path.append("%s\\features\\" % runningPath)

RELEASE_RATIO = 1
DISPATCH_RATIO = -1

MAX_CPU = 92
MAX_MEM = 288
MAX_DISK = 1024
MAX_P = 7
MAX_M = 7
MAX_PM = 9
SLICE_CNT = 98
ISOTIMEFORMAT = "%Y-%m-%d %X"

MACHINE_CNT = 6000
APP_CNT = 9338
INST_CNT = 68219
        
def getCurrentTime():
    return "[%s]" % (time.strftime(ISOTIMEFORMAT, time.localtime()))

def split_slice(slice):
    return np.array(list(map(float, slice.split('|'))))

def score_of_cpu_percent_slice(slice):
    return np.where(np.greater(slice, 0), \
                    1 + 10 * (np.exp(np.maximum(0, slice - 0.5)) - 1), \
                    0).sum()

def print_and_log(msg):
    print(getCurrentTime(), msg)
    logging.info(msg)


g_pheromone_dict = dict()

g_cur_def_pheromone = 700

ALPHA = 1.0 #启发因子，信息素的重要程度
BETA = 2.0  #期望因子，城市间距离的重要程度
ROU = 0.5   #信息素残留参数
