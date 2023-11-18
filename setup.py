from cx_Freeze import setup, Executable
import sys

buildOptions = dict(packages=[], excludes=[])

base = None
if sys.platform =="win32":
    base="Win32GUI"

exe=[Executable("dashboard.py", base=base)]

setup(
    name="IMS",
    version='0.1',
    author="Teddy",
    description="First EXE APP",
    options=dict(build_exe=buildOptions),
    executables = exe
)