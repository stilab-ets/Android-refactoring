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
import shutil

os.chdir('C:/Users/AQ42770/Documents/ck/target')
path='C:/Users/AQ42770/Documents/MobileSoft/before'
for n in range(0,Number):
    path1= path+"/"+str(n)+"before"
    cmd='java -jar ck-0.6.4-SNAPSHOT-jar-with-dependencies.jar "%s"'
    cmd = cmd % (path1)
    args = shlex.split(cmd)
    p = subprocess.Popen(args)
    time.sleep(80)
    class1="class1"+str(n)+".csv"
    os.rename('class.csv',class1)
    
