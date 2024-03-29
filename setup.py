'''
Build the python-aiml Py2/Py3 package
'''

from setuptools import setup
import glob

from aiml.constants import VERSION

#package_prefix = "Lib/site-packages/aiml"


setup_args = dict( name="python-aiml",
    version=VERSION,
    author="cc",
    author_email="jerrychen110@hotmail.com",
    
    description="An interpreter package for AIML, the Artificial Intelligence Markup Language",
    long_description="""python-aiml implements an interpreter for AIML, the Artificial Intelligence
Markup Language developed by Dr. Richard Wallace of the A.L.I.C.E. Foundation.
It can be used to implement a conversational AI program.

Forked from PyAIML 0.8.6 (https://github.com/cdwfs/pyaiml) 
PyAIML (c) Cort Stratton
""",
    url="https://github.com/jerrychen110/python-aiml",
    platforms=["any"],
    classifiers=["Development Status :: 4 - Beta",
                 "Environment :: Console",
                 "Intended Audience :: Developers",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.4",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "License :: OSI Approved :: BSD License",
                 "Operating System :: OS Independent",
                 "Topic :: Communications :: Chat",
                 "Topic :: Scientific/Engineering :: Artificial Intelligence"
                 ],
 
    install_requires = [ 'setuptools',
    ],

    packages=[ "aiml", 'aiml.script', 'aiml.multi_language' ],
#    package_dir = { 'aiml': 'aiml',
#                    'aiml.script' : 'aiml/script' },

    include_package_data = False,       # otherwise package_data is not used
    package_data={ 'aiml': ['botdata/EN/*/*.aiml',
                            'botdata/EN/*/*.xml',
                            'botdata/EN/*/*.aiml',
                            'botdata/EN/*/*.xml',
                            'botdata/CN/*/*.xml',
                            'botdata/CN/*/*.aiml',
                            'botdata/CN/*/*.py',

                            ]},

    entry_points = { 'console_scripts': [
        'aiml-validate = aiml.script.aimlvalidate:main',
        'aiml-bot = aiml.script.bot:main',
    ]},

    test_suite = 'test.__main__.load_tests',

#    data_files=[
#        (package_prefix, glob.glob("aiml/self-test.aiml")),
#        (package_prefix, glob.glob("*.txt")),
#    ],
)

if __name__ == '__main__':
    setup( **setup_args )
