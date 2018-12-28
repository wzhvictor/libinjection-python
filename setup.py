from setuptools import setup, Extension
from Cython.Distutils import build_ext

source_files = [
    'libinjection/libinjection.pyx',
    'libinjection/src/libinjection_sqli.c',
    'libinjection/src/libinjection_html5.c',
    'libinjection/src/libinjection_xss.c'
]
cmd_class = {'build_ext': build_ext}

setup(
    name='libinjection-python',
    version='1.1.4',
    author='wzhvictor',
    author_email='wzhvictor@outlook.com',
    url='https://github.com/wzhvictor/libinjection-python',
    description='Libinjection Python Wrapper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Cython',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=[],
    include_package_data=True,
    cmdclass=cmd_class,
    ext_modules=[Extension(
        name='libinjection',
        sources=source_files,
        include_dirs=['libinjection/src'],
        library_dirs=['libinjection/src'])
    ],
    install_requires=[
        'setuptools>=38.3.0',
        'Cython>=0.23'
    ]
)
