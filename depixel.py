import sys
import subprocess

input=[] 
for i in range(len(sys.argv)):
    if i == 0:
        continue
    input.extend([sys.argv[i]])
    command="potrace "+input[i-1]+" -b pdf"
    a=subprocess.Popen(command,shell=True)
