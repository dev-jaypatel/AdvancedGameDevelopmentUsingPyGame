##Packaging your game for distribution

import cx_Freeze


executables = [cx_Freeze.Executable("advancedpython.py")]

cx_Freeze.setup(
    name="Learning More PyGame",
    options = {"build_exe": {"packages":["pygame"], "include_files":['png/']}},
    executables = executables
)
