from setuptools import setup



setup(

    name = 'booklover.py',

    version = '0.1.0',

    author = 'Courtney Hodge',

    author_email = 'yss2zv@virginia.edu',

    packages = ['booklover.py', 'booklover_test.py'],

    scripts = ['my_project_script'],

    url = 'https://github.com/courtneyhodge/M09_HW',

    license = 'MIT LICENSE',

    description = 'An awesome package that does something',

    long_description = open('README.txt').read(),

    install_requires = [

        "Django >= 1.1.1",

        "pytest",

    ],

)
