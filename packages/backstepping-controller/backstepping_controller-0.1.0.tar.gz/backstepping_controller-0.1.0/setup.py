from setuptools import setup, find_packages

setup(
    name='backstepping_controller',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'sympy'
    ],
    description='A package for simulating control systems using backstepping control laws',
    author='Samuel O. Folorunsho',
    author_email='folorunshosamuel001@gmail.com',
    url='https://github.com/sof-danny/backstepping_controller',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
