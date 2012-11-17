from distutils.core import setup

setup(
    name='dirmerger',
    version='0.0.1',
    author='Krzysztof Szukielojc',
    author_email='krzysztof@szukielojc.com',
    packages=['dirmerger'],
    scripts=['bin/dir-merger'],
#    url='http://pypi.python.org/pypi/TowelStuff/',
#    license='LICENSE.txt',
#    description='Useful towel-related stuff.',
#    long_description=open('README.txt').read(),
    install_requires=[
        "path",
    ],
)
