#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip

from setuptools import find_packages, setup

if int(pip.__version__.split('.')[0]) >= 10:
    from pip._internal import download as pip_download
    from pip._internal.req import parse_requirements

else:
    from pip import download as pip_download
    from pip.req import parse_requirements

exec(open('steenzout/sphinx/metadata.py').read())


def requirements(requirements_file):
    """Return packages mentioned in the given file.
    Args:
        requirements_file (str): path to the requirements file to be parsed.
    Returns:
        (list): 3rd-party package dependencies contained in the file.
    """
    return [
        str(pkg.req) for pkg in parse_requirements(
            requirements_file, session=pip_download.PipSession()) if pkg.req is not None]


setup(name='steenzout.sphinx',
      version=__version__,
      description=__description__,
      author=__author__,
      author_email=__author_email__,
      maintainer=__maintainer__,
      maintainer_email=__maintainer_email__,
      url=__url__,
      classifiers=__classifiers__,
      namespace_packages=['steenzout'],
      packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
      package_data={'steenzout.sphinx': ['templates/*.j2']},
      install_requires=requirements('requirements.txt'),
      tests_require=requirements('requirements-test.txt'),
      entry_points={
          'console_scripts': [
              'steenzout-sphinx-generate = steenzout.sphinx.cli:generate',
          ]})
