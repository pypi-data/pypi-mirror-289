from setuptools import setup, find_packages

with open('README.md', 'r') as file:
	readme_file = file.read()

setup(
	name =  'ppfutils',
	long_description = readme_file,
	long_description_content_type = 'text/markdown',
	version = '0.0',
	packages = find_packages(),
	install_requires = []
)
