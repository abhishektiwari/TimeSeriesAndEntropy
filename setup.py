try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Physiological time-series analysis using various entropy approaches',
	'author': 'Abhishek Tiwari',
	'url': 'http://github.com/abhishektiwari/TimeSeriesAndEntropy',
	'download_url': 'http://github.com/abhishektiwari/TimeSeriesAndEntropy',
	'author_email': 'abhishek@abhishek-tiwari.com',
	'version': '0.1',
	'install_requires': [],
	'packages': ['entropy'],
	'scripts': [],
	'name': 'TimeSeriesAndEntropy'
}

setup(**config)
