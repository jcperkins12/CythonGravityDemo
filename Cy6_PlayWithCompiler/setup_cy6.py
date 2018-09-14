from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [
        Extension("gravity_cy6",
            ["gravity_cy6.pyx"]
        ),
    ]
)
