import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'cmsplugin-rt',
    version = '0.3.1',
    packages = find_packages(),   #'cmsplugin_rt',   #find_packages(),
    include_package_data = True,
    license = 'BSD License', # example license
    description = 'This package contains a number of basic plugins to kick start your DjangoCMS project, such as Twitter Bootstrap navbar and buttons, Facebook and Twitter buttons, a Style Modifier, Google Analytics tracking code, Google fonts, meta tags and resizable pictures.',
    long_description = README,
    keywords = "button meta twitter bootstrap style modifier racing tadpole",
    url = 'https://github.com/RacingTadpole/cmsplugin-rt',
    author = 'Art Street',
    author_email = 'art@racingtadpole.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe = False,
)
