import os
import shlex
import subprocess
import pandas as pd
path='C:/Users/AQ42770/Desktop/RefactoringMiner/bin/vimtouch'
os.chdir(path)
pa='C:/Users/AQ42770/Desktop/1'
df=pd.read_csv('all_refactorings.csv' ,sep=';')
a=df.loc[~df.CommitId.duplicated(keep='last')]
repo_Name = a['CommitId']
b=repo_Name.to_frame(name=None)


n=0
for elem in b['CommitId']:
   print(elem)
   path= pa+"/"+str(n)
   n+=1
   commande='git worktree add "%s" %s'
   commande= commande % (path, elem)
   args = shlex.split(commande)
   p = subprocess.Popen(args)
        
    
    
    
    

