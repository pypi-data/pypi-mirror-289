from setuptools import setup, find_packages

with open('README.md', 'r') as f:
	description = f.read()

setup(
	name='tspoon',
	version='0.1.2',
	packages=find_packages(),
	install_requires=[
		# 'os',
		# 'time',
		# 'sys',
		# 'pickle',
		# 'pandas',
		# 'numpy',
		# 'regex',
		# 'datetime',
		# 'matplotlib',
		# 'statsmodels',
		# 'copy'
	],
	description='Tspoon is a Python library for time-series pre-processing, period conversion, normalization, and visualization.',
	long_description=description,
	long_description_content_type='text/markdown',
)