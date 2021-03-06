from distutils.core import setup
setup(
	name = 'add',         # How you named your package folder (MyLib)
	packages = ['add-py'],   # Chose the same as "name"
	version = '0.3',      # Start with a small number and increase it with every change you make
	license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
	description = 'This is just an attempt to upload code to pypi',   # Give a short description about your library
	author = 'Zafar Shadman',                   # Type in your name
	author_email = 'shadmanzafar15@gmail.com',      # Type in your E-Mail
	url = 'https://github.com/zapcode',   # Provide either the link to your github or to your website
	download_url = 'https://github.com/zapcode/add-py/archive/refs/tags/v1.0.3.tar.gz',   
	keywords = ['CALCULATE', 'ADD', 'SUM'],   # Keywords that define your package best
	install_requires=[            # I get to this in a second
		'numpy',
		'pandas',
	],
	classifiers=[
		'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
		'Intended Audience :: Developers',      # Define that your audience are developers
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',   # Again, pick a license
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	],
)
