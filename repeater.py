#!/usr/bin/env python3
import subprocess
import time

eta_values = [0.5, 0.4, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.01, 0.001]
for value in eta_values:
    print('===============')
    call_string = './gradient_descent.py -e ' + str(value)
    start_time = time.time()
    p = subprocess.Popen(call_string,shell=True, stdout=subprocess.PIPE,universal_newlines=True)
    end_time = time.time()
    print("ETA: " + str(value))
    for line in p.stdout.readlines():
        print(line,end='')
    print("Running time: {} sec".format(end_time-start_time))
