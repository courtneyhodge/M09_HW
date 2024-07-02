from setuptools import setup, find_packages



setup(

    name='M09 HW',

    version='0.1.0',

    author='Courtney Hodge',

    author_email='yss2zv@virginia.edu',

    packages=find_packages(),  # Automatically find packages in your project

    scripts=['my_project_script'],

    url='https://github.com/courtneyhodge/M09_HW',

    license='MIT LICENSE',

    description='An awesome package that does something',

    long_description=open('README.md').read(),

    install_requires=[

        "Django >= 1.1.1",

        "pytest",

    ],

)


