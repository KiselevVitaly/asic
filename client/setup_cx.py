from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['os'], 'excludes': ['tkinter']}
setup(
    name='asinc_server',
    version='0.0.1',
    description='Asinc chat',
    author='Vladislav Goryakin',
    options={
        'build_exe': build_exe_options,
    },
    executables=[Executable('src/client.py')]
)
