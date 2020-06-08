import os
import numpy as np
import random
import datetime
from sklearn.svm import LinearSVC
from z3 import *
import signal
import time


dirName = sys.argv[1]
targetCSV = sys.argv[2]

fileList = os.listdir(dirName)
for name in fileList:
    if name.endswith(".bpl.log"):
        with open(dirName + name, "r", encoding="utf-8") as f:
            changed = False
            print(dirName + name)
            for line in f:
                if line.find("LEARNING RESULT") != -1:
                    if (line.find("INF-INITE") != -1): 
                        print("INF-INITE")
                        wf = open(targetCSV, "a")
                        wf.write(name.split(".", 1)[0] + "," + "N\n")
                        wf.close()
                        changed = True
                        break
                    elif line.find("FINITE") != -1:
                        print("FINITE")
                        wf = open(targetCSV, "a")
                        wf.write(name.split(".", 1)[0] + "," + "Y\n")
                        wf.close()
                        changed = True
                        break
                    else:
                        print("UNKNOWN")
                        wf = open(targetCSV, "a")
                        wf.write(name.split(".", 1)[0] + "," + "U\n")
                        wf.close()
                        changed = True
                        break
            if not changed:
                print("UNKNOWN")
                wf = open(targetCSV, "a")
                wf.write(name.split(".", 1)[0] + "," + "U\n")
                wf.close()
                changed = True

