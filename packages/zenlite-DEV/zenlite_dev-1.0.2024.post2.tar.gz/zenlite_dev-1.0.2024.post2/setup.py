from setuptools import setup, find_packages

setup(
    name='zenlite_DEV',
    version='1.0.2024-2',
    description='the python engine',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Izaiyah Stokes',
    author_email='zeroth.bat@gmail.com',
    url='https://github.com/stozak',
    packages=find_packages(),
    package_data={"zenlite": ['assets/*']},
    install_requires=[
        'GLFW',
        'Numba',
        'Numpy',
        'PyGLM',
        'ModernGL',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)