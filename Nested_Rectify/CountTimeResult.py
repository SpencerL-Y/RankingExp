import os
import numpy as np
import random
import datetime
from sklearn.svm import LinearSVC
from z3 import *
import signal
import time
import re

train_expression = re.compile(r"train_ranking_functioning time = ")

dirName = sys.argv[1]

fileList = os.listdir(dirName)
i = 0
for name in fileList:
    if name.endswith(".bpl.log"):
        print(name)
        os.rename(os.path.join(os.path.abspath(dirName), name), str(i)+".bpl.log")
        i = i + 1