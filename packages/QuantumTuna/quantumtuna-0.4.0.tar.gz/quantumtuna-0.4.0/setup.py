from setuptools import setup

setup(
    name='QuantumTuna',
    version='0.4.0',    
    description='A user-friendly quantum chemistry program for diatomics!',
    url='https://github.com/harrybrough1/TUNA',
    author='Harry Brough',
    author_email='harry.brough@yahoo.com',
    license='BSD 2-clause',
    packages=['twona'],
    install_requires=['numpy',
                      'setuptools',                     
                      ],

    classifiers=[      
        'Programming Language :: Python :: 3.13',
    ],
)