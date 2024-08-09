"""""" # start delvewheel patch
def _delvewheel_patch_1_7_4():
    import os
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'cvc5.libs'))
    if os.path.isdir(libs_dir):
        os.add_dll_directory(libs_dir)


_delvewheel_patch_1_7_4()
del _delvewheel_patch_1_7_4
# end delvewheel patch

import sys
from .cvc5_python_base import *
__file__ = cvc5_python_base.__file__
__version__ = "1.2.0"
