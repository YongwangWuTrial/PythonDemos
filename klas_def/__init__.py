import os.path

'''
导入的模块及其导入的决定了在后期使用是导入方式繁简程度：
__init__.py中导入的内容多，则包调用者导入语句简单，反之需要嵌入方式精细导入；
'''
from klas_def.interface import *
# from klas_def.txtDat import *

print(os.path.abspath(os.path.curdir))
print("package's name is", __name__)


# __all__ = ["SourceFiles",]
