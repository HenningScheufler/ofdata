======
OFData
======

provides meta data for the openfoam library


* Free software: MIT license
* Documentation: https://ofdata.readthedocs.io.


How to use
----------

..  code-block:: bash

    pip install -e .
    cd tests
    ofdata $WM_PROJECT_DIR # parse headers
    python test_flask.py
    http://127.0.0.1:5001/func/forces/ enter browser


Output
------

.. image:: docs/images/docs_postProcessing.png 
   :width: 600