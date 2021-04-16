

import os
import shlex
import subprocess
import json
from collections import Counter
import json 
import csv
import pandas as pd
import time
import glob


extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
for file in all_filenames:
    df = pd.read_csv(file)
    a=df.loc[~df.Name.duplicated(keep='last')]
    a.to_csv(file, index=False, na_rep='NaN')
    a.to_csv(file, index=False, na_rep='NaN')
