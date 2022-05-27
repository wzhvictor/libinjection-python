from setuptools import setup, Extension

USE_CYTHON = False

try:
    from Cython.Build import cythonize

    USE_CYTHON = True
except ImportError:
    pass

ext = ".pyx" if USE_CYTHON else ".c"

extensions = [
    Extension(
        name="libinjection",
        sources=[
            "libinjection/libinjection" + ext,
            "libinjection/src/libinjection_sqli.c",
            "libinjection/src/libinjection_html5.c",
            "libinjection/src/libinjection_xss.c",
        ],
        include_dirs=["libinjection/src"],
        library_dirs=["libinjection/src"],
    )
]

if USE_CYTHON:
    extensions = cythonize(extensions)

setup(
    name="libinjection-python",
    version="1.1.6",
    author="wzhvictor",
    author_email="wzhvictor@outlook.com",
    url="https://github.com/wzhvictor/libinjection-python",
    description="Libinjection Python Wrapper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Cython",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=[],
    include_package_data=True,
    ext_modules=extensions,
)
