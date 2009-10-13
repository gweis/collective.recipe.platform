from setuptools import setup, find_packages
import sys, os

version = '0.1'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

tests_require = ['zope.testing', 'zc.buildout']

setup(name='collective.recipe.platform',
      version=version,
      description="Provide buildout variables with platform specific values.",
      long_description=(
          read('README.txt') +
          read('src', 'collective', 'recipe', 'platform', 'README.txt') +
          read('CHANGES.txt')),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Framework :: Buildout',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
      keywords='buildout development build',
      author='Gerhard Weis',
      author_email='gerhard.weis@gmx.com',
      url='http://pypi.python.org/pypi/collective.recipe.platform',
      license='BSD',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.recipe'],
      include_package_data=True,
      install_requires=[
          'zc.buildout',
          'setuptools',
          ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='collective.recipe.platform.tests.test_docs.test_suite',
      entry_points = {'zc.buildout':
                      ['default = collective.recipe.platform:Recipe']},
      )
