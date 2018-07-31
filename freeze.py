from cx_Freeze import setup, Executable

setup(name='executable',
	version='0.1',
	description='various functions',
	executables=[Executable("executable.py")])