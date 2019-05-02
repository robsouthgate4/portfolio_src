# import shutil
# import os

# def copytree(src, dst, symlinks=False, ignore=None):
#     for item in os.listdir(src):
#         print(item)
#         s = os.path.join(src, item)
#         d = os.path.join(dst, item)       
#         shutil.rmtree(d) 
#         if os.path.isdir(s):            
#             shutil.copytree(s, d, symlinks, ignore)
#         else:
#             shutil.copy(s, d)


# copytree('_site', '../robsouthgate4.github.io')