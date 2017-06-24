#!/usr/bin/env python
import random
import os
import time


bcolors = [
     '\033[95m',
     '\033[94m',
     '\033[92m',
     '\033[93m',
     '\033[91m',
     '\033[0m'
    ]
 

def main(name, counter):
    for x in range(counter):
        print random.choice(bcolors), "Happy Birthday, {0}".format(name)
        os.system('clear')
     
if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--name')
    parser.add_option('--count', default=100, type='int')
    opt, arg = parser.parse_args()
    main(opt.name, opt.count)    
