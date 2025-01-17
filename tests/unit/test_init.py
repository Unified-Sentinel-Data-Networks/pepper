# -*- coding: utf-8 -*-
# Import Python Libraries
from __future__ import print_function, unicode_literals, absolute_import
import imp
import os
import shutil
import setuptools_scm

# Import Pepper Libraries
import upepper


def test_no_setup():
    setuppath = os.path.join(os.path.dirname(upepper.__file__), os.pardir, 'setup.py')
    shutil.move(setuppath, setuppath + '.bak')
    ptest = imp.load_source('ptest', os.path.join(os.path.dirname(upepper.__file__), '__init__.py'))
    shutil.move(setuppath + '.bak', setuppath)
    assert ptest.version == setuptools_scm.get_version()
    assert ptest.sha is None


def test_version():
    assert upepper.version == setuptools_scm.get_version()
    assert upepper.sha is None
