Django Ajax CBV
=================

|Build Status| |Codacy Badge| |Coverage Status| |BCH compliance| |Pypi|

Django module to easily use generic Class Based views with ajax.

Table of contents:
 * `How to install`_;
 * `License`_.

Compatibility
-------------
Tested with python 2.7, 3.4, 3.5, 3.6 and Django 1.9, 1.10, 1.11: `Travis CI <https://travis-ci.org/dipcode-software/django-ajax-cbv>`_

How to install
--------------

To install the app run :

.. code:: shell

    pip install django-ajax-cbv

or add it to the list of requirements of your project.

Then add ‘ajax\_cbv’ to your INSTALLED\_APPS.

.. code:: python

    INSTALLED_APPS = [
        ...
        'ajax_cbv',
    ]

License
-------

MIT license, see the LICENSE file. You can use obfuscator in open source
projects and commercial products.

.. _How to install: #how-to-install
.. _License: #license

.. |Build Status| image:: https://travis-ci.org/dipcode-software/django-ajax-cbv.svg?branch=master
   :target: https://travis-ci.org/dipcode-software/django-ajax-cbv
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/a64f03c2bd344561bc21e05c23aa04fb
   :target: https://www.codacy.com/app/srtabs/django-ajax-cbv?utm_source=github.com&utm_medium=referral&utm_content=dipcode-software/django-ajax-cbv&utm_campaign=Badge_Grade
.. |Coverage Status| image:: https://coveralls.io/repos/github/dipcode-software/django-ajax-cbv/badge.svg?branch=master
   :target: https://coveralls.io/github/dipcode-software/django-ajax-cbv?branch=master
.. |BCH compliance| image:: https://bettercodehub.com/edge/badge/dipcode-software/django-ajax-cbv?branch=master
   :target: https://bettercodehub.com/
.. |Pypi| image:: https://img.shields.io/pypi/v/django-ajax-cbv.svg?style=flat-square
   :target: https://pypi.python.org/pypi/django-ajax-cbv
