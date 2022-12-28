
import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['mac_acl/']

# TARGET
target = Executable(
    script="tk.py",
    base="Win32GUI",
)

# SETUP CX FREEZE
setup(
    name = "MacACL",
    version = "1.0",
    description = "",
    author = "Oscar Ossa",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)