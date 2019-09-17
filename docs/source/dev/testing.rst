.. _testing:

Testing
=======

Running Test Files
-------------------

Python files for testing can be found in the ``tests`` subdirectory of the project.

There are two types of test files:

1. Unit test files to be run by pytest

    These files begin with ``test`` and end with ``.py``.

    These files can be run automatically by selecting ``Run unit tests`` from the Spyder ``Run`` menu.

    (Note: you will need to install ``spyder-unittest`` for this to work; i.e. ``pip install spyder-unittest``)

    The tests can also be run by typing ``pytest`` inside the ``tests`` directory of the libsbml-draw repository

2. Files to be run by python

    These files begin with ``mtest`` and end with ``.py``.

    These files can be run from Spyder by opening the file and pressing the big green arrow.

    ``mtest`` stands for manual tests.  These tests draw the models, so that the user can view them.  

    They also write out SBML model files.  They contain ``assert`` statements which test values after being set.
