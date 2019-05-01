import shutil
import os

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            if os.path.isdir(d):
                shutil.rmtree(d)
                shutil.copytree(s, d, symlinks, ignore)


copytree('_site', '../robsouthgate4.github.io')