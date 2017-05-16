#!/usr/bin/env python3

import fnmatch
import os
import random
import re


def get_item():
    items = set()
    for ifile in os.listdir('.'):
        if not fnmatch.fnmatch(ifile, '*.md'):
            continue
        with open(ifile, 'r') as f:
            for line in f:
                if line.startswith('* ') or line.startswith('1.'):
                    items.add((ifile, line.strip()))
    fn, line = random.choice(list(items))
    line = re.sub(r'^(\*|1\.)\s*', '', line)
    return fn, line


def main():
    fn, line = get_item()
    try:
        import mdv
        line = mdv.main(line)
    except ImportError:
        pass
    print('Fun fact! {1} ({0})'.format(fn, line))


if __name__ == '__main__':
    main()
