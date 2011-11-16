from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.widgetplus',
      version=version,
      description="Widget traversal",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='formlib widget traversal namespace',
      author='Danilo G. Botelho',
      author_email='danilogbotelho@yahoo.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.formlib',
          'zope.traversing',
          'zope.security',
          'zope.publisher',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
