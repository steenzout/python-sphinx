# Tutorial

The first thing you can do is it to create a new
sphinx template project for your organization in GitHub
(just like this one).

Taking this project as the baseline,
first of all you create a `requirements-docs.txt` and
add it to the `MANIFEST.in` file.

The `requirements-docs` file should contain all the dependencies
you'll need to build the Sphinx documentation for your project.

For example:

   recommonmark==0.4.0
   semantic_version==2.6.0
   Sphinx==1.4.8
   sphinx_rtd_theme==0.1.9


After this you can setup the `docs` virtualenv in `tox`.

For example:

   [testenv:docs]
   usedevelop = False
   changedir = docs

   deps =
       -rrequirements.txt
       -rrequirements-docs.txt

   commands =
       steenzout-sphinx-generate organization organization.sphinx .
       make dummy
       make apidoc
       make coverage
       make changes
       make html

   whitelist_externals =
       /usr/bin/make


Before you continue,
you'll need to create a metadata module.

For example,

```python
   __author__ = u'Myself'
   __author_email__ = u'email@example.com'

   __classifiers__ = [
       'Development Status :: 5 - Production/Stable',
       'Intended Audience :: Developers',
       'License :: OSI Approved :: Apache Software License',
       'Operating System :: OS Independent',
       'Programming Language :: Python',
       'Programming Language :: Python :: 2',
       'Programming Language :: Python :: 2.7',
       'Programming Language :: Python :: 3',
       'Programming Language :: Python :: 3.6',
       'Programming Language :: Python :: 3.5',
       'Programming Language :: Python :: Implementation :: CPython',
       'Topic :: Documentation',
       'Topic :: Documentation :: Sphinx',
       'Topic :: Software Development :: Documentation'
   ]
   __copyright__ = u'2016, %s' % __author__

   __description__ = u'Sphinx configuration for YOUR GitHub organization.'

   __maintainer__ = u'Myself'
   __maintainer_email__ = u'email@example.com'

   __url__ = u'https://github.com/organization/python-sphinx/'

   __version__ = u'0.0.1'
```

This metadata module must be placed
under `organization/sphinx/metadata.py` directory or
else this library won't find it.

The next step is to create a `templates` directory under `organization/sphinx`.

In this directory you should place the `conf.py.j2` and `Makefile.j2` templates you need.

Check this project template files for an example.

After you complete all of these tasks you can now generate your documentation using


```bash
$ tox -e docs
```

After you complete these steps and you are happy with the results
you can use your new `organization.sphinx` templates in any of your projects.

To achieves this you setup your `requirements-docs.txt`
by addding your `organization.sphinx` package.


   -e git+git@github.com:organization/python-sphinx.git@master#egg=organization-sphinx-master

The `tox.ini` file for the project will only change the package being documented.

   [testenv:docs]
   usedevelop = False
   changedir = docs

   deps =
       -rrequirements.txt
       -rrequirements-docs.txt

   commands =
       steenzout-sphinx-generate organization organization.project .
       make dummy
       make apidoc
       make coverage
       make changes
       make html

   whitelist_externals =
       /usr/bin/make

In the end, you can generate all the documentation
with the `tox -e docs` command.
