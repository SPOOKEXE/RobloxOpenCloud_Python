from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
	long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'API for Roblox Open Cloud - DataStores, MessagingService and Place Publishing.'
LONG_DESCRIPTION = 'This package allows easy access to utilise your API keys without having to worry about the network side.\nSimply create a client object and pick what function you would like to utilise and wallah!'

# Setting up
setup(
	name="roblox_opencloud",
	version=VERSION,
	author="SPOOK_EXE (Declan H)",
	author_email="<unavailable>",
	description=DESCRIPTION,
	long_description_content_type="text/markdown",
	long_description=long_description,
	packages=find_packages(),
	install_requires=[],
	keywords=['python', 'roblox', 'open-cloud', 'roblox open-cloud', 'datastore', 'publish', 'messaging-service'],
	classifiers=[
		"Development Status :: 2 - Production",
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 3",
		#"Operating System :: Unix",
		#"Operating System :: MacOS :: MacOS X",
		"Operating System :: Microsoft :: Windows",
	]
)