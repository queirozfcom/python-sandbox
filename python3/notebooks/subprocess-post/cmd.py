import subprocess
import sys

with open('out.txt','w+') as fout:
    with open('err.txt','w+') as ferr:
        out=subprocess.call(["./bash-script-with-bad-syntax"],stdout=fout,stderr=ferr)
        fout.seek(0)
        print('output:')
        print(fout.read())
        ferr.seek(0) 
        print('error:')
        print(ferr.read())
