from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext

source_files = [
    'src/libinjection.pyx',
    'submodules/src/libinjection_sqli.c',
    'submodules/src/libinjection_html5.c',
    'submodules/src/libinjection_xss.c'
]
cmd_class = {'build_ext': build_ext}

setup(
    name='libinjection-python',
    version='2018.9',
    description='Libinjection Python Wrapper',
    author='wangzhenghao',
    author_email='wzhvictor@outlook.com',
    license='GPLv3',
    url='https://github.com/wzhvictor/libinjection-python',
    packages=[],
    cmdclass=cmd_class,
    ext_modules=[Extension(
        'libinjection',
        sources=source_files,
        include_dirs=['submodules/src'],
        library_dirs=['submodules/src'])
    ],
    install_requires=open('requirements.txt').read().splitlines()
)
