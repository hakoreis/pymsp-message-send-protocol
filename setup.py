try:
    from setuptools import setup

except(ImportError):
    from distutils.core import setup

setup(
	name='pymsp', 
	packages=['pymsp'], 
	version='0.9', 
	description='QPython Message Send Protocol (MSP) adapter', 
	long_description=open('README.md').read(), 
	author='Hakan Vergil', 
	author_email='hakanvergil@gmail.com', 

	install_requires=['bar', 'greek'], 

	scripts=[ 'scripts/cool', 'scripts/skype', ]
)



