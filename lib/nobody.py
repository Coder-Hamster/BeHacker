import time
import json
import os

def wait(x):
    now = time.time()
    while(time.time()-now <= x):
        pass

def check_times(file_rev):
    f = open(file_rev,"r",encoding="UTF-8")
    time_list = json.loads(f.read())
    if(time_list["times"]=="first"):
        time_list["times"] = "no_first"
        f.close()
        f = open(file_rev,"w")
        f.write(json.dumps(time_list))
        f.close()
        return True
    else:
        return False



