import json
from collections import Counter
import json 
import csv
import pandas as pd
import glob
import time
import os
import shlex
import subprocess

os.chdir('C:/Program Files/SciTools/bin/pc-win64')

base='C:/Users/AQ42770/Documents/MobileSoft/before'

for n in range(0,Number):
    
    #base1= base+"/"+str(n)
   
    base1= "C:/Users/AQ42770/Documents/MobileSoft/before/"+str(n)+"before/project.udb"
    source= "C:/Users/AQ42770/Documents/MobileSoft/before/"+str(n)+"before"
    OutputDirectory= "C:/Users/AQ42770/Documents/MobileSoft/beforeUnder"
    OutputFile= "C:/Users/AQ42770/Documents/MobileSoft/beforeUnder/metricsUn"+str(n)+".csv"
    cmd='und -db %s create -languages java add %s settings -metrics all -metricsOutputFile %s analyze report metrics'
    cmd = cmd % (base,source,OutputFile)
    args = shlex.split(cmd)
    p = subprocess.Popen(args)
    time.sleep(80)
    
