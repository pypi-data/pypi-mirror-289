from setuptools import setup

setup(name='partlint',
      version='1.1.0',
      description='Check if LCSC part numbers still match the values of the parts',
      url='https://git.sr.ht/~martijnbraam/partlint',
      author='Martijn Braam',
      author_email='martijn@brixit.nl',
      packages=['partlint'],
      install_requires=['sexpdata', 'tabulate', 'requests', 'openpyxl'],
      project_urls={
          'Source': 'https://git.sr.ht/~martijnbraam/partlint',
      },
      entry_points={
          'console_scripts': ['partlint=partlint.__main__:main'],
      })