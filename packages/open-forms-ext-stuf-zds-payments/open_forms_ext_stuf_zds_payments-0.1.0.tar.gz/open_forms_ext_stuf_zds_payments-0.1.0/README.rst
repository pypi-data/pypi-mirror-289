

Welcome to stuf_zds_payments's documentation!
=================================================

:Version: 0.1.0
:Source: https://github.com/maykinmedia/stuf_zds_payments
:Keywords: ``<keywords>``
:PythonVersion: 3.12

|build-status| |code-quality| |black| |coverage| |docs|

|python-versions| |django-versions| |pypi-version|

<One liner describing the project>

.. contents::

.. section-numbering::

Features
========

* ...
* ...

Installation
============

Requirements
------------

* Python 3.12 or above
* Django 4.2 or newer


Install
-------

.. code-block:: bash

    pip install stuf_zds_payments


Usage
=====

<document or refer to docs>

Local development
=================

To install and develop the library locally, use::

.. code-block:: bash

    pip install -e .[tests,coverage,docs,release]

When running management commands via ``django-admin``, make sure to add the root
directory to the python path (or use ``python -m django <command>``):

.. code-block:: bash

    export PYTHONPATH=. DJANGO_SETTINGS_MODULE=testapp.settings
    django-admin check
    # or other commands like:
    # django-admin makemessages -l nl


.. |build-status| image:: https://github.com/maykinmedia/stuf_zds_payments/workflows/Run%20CI/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/stuf_zds_payments/actions?query=workflow%3A%22Run+CI%22

.. |code-quality| image:: https://github.com/maykinmedia/stuf_zds_payments/workflows/Code%20quality%20checks/badge.svg
     :alt: Code quality checks
     :target: https://github.com/maykinmedia/stuf_zds_payments/actions?query=workflow%3A%22Code+quality+checks%22

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |coverage| image:: https://codecov.io/gh/maykinmedia/stuf_zds_payments/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/maykinmedia/stuf_zds_payments
    :alt: Coverage status

.. |docs| image:: https://readthedocs.org/projects/stuf_zds_payments/badge/?version=latest
    :target: https://stuf_zds_payments.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/stuf_zds_payments.svg

.. |django-versions| image:: https://img.shields.io/pypi/djversions/stuf_zds_payments.svg

.. |pypi-version| image:: https://img.shields.io/pypi/v/stuf_zds_payments.svg
    :target: https://pypi.org/project/stuf_zds_payments/
