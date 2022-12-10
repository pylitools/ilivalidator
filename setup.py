import os
from setuptools import setup, find_packages

# buildNumber = 'LOCALBUILD'
# if os.environ.get('GITHUB_RUN_NUMBER'): 
#     buildNumber = os.environ.get('GITHUB_RUN_NUMBER')

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    author="Stefan Ziegler",
    author_email='edi.gonzales@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
    ],
    description="Python package for ilivalidator.",
    install_requires=['importlib-resources'] ,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='ilivalidator,interlis',
    name='ilivalidator',
    packages=find_packages(include=['ilivalidator', 'ilivalidator.*']),
    package_data={'ilivalidator.lib_ext':['*.h', '*.lib', '*.dll', '*.so', '*.dylib']},
    #test_suite='tests',
    #tests_require=test_requirements,
    url='https://github.com/pylitools/ilivalidator',
    version='0.0.2',
)
