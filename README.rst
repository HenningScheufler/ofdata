======
OFData
======


.. image:: https://img.shields.io/pypi/v/ofdata.svg
        :target: https://pypi.python.org/pypi/ofdata

.. image:: https://img.shields.io/travis/HenningScheufler/ofdata.svg
        :target: https://travis-ci.com/HenningScheufler/ofdata

.. image:: https://readthedocs.org/projects/ofdata/badge/?version=latest
        :target: https://ofdata.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




provides meta data for the openfoam library


* Free software: MIT license
* Documentation: https://ofdata.readthedocs.io.


How to use
----------

.. code-block::

    python -m venv env
    pip install .
    cd tests
    ofdata $WM_PROJECT_DIR # parse headers
    python test-flask


open in browser http://127.0.0.1:5001/func/forces/




Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
