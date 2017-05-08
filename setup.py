from setuptools import setup

setup(name='python-facebook-bot',
      version='0.1',
      description='Using API to get Facebook Events by location, etc... with Python',
      url='http://github.com/tudoanh/python-facebook-bot',
      author='Do Anh Tu',
      author_email='tu0703@gmail.com',
      license='MIT',
      install_requires=['requests>=2.13.0'],
      packages=['facebook_bot'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])
