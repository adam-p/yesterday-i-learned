#!/usr/bin/env python3


import os
from collections import Counter, defaultdict


alphabet = defaultdict(int)
rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    # print('Found directory: %s' % dirName)
    for fname in fileList:
        fpath = os.path.join(dirName, fname)
        # print('\t%s' % fpath)
        if fpath.endswith('.md'):
            with open(fpath, 'r') as f:
                for line in f:
                    for char in line:
                        alphabet[char.lower()] += 1

for (char, freq) in Counter(alphabet).most_common(100):
    print(char, ',', freq)
