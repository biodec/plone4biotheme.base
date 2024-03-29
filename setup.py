from setuptools import setup, find_packages
import os

version = '1.1.0rc1'

setup(name='plone4biotheme.base',
      version=version,
      description="An installable theme for Plone 4.0",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme bio',
      author='Biodec S.r.l.',
      author_email='info@biodec.com',
      url='http://www.plone4bio.org/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone4biotheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [distutils.setup_keywords]
      paster_plugins = setuptools.dist:assert_string_list

      [egg_info.writers]
      paster_plugins.txt = setuptools.command.egg_info:write_arg
      """,
      paster_plugins = ["ZopeSkel"],
      )
