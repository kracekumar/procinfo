#! -*- coding: utf-8 -*-

import os
import sys
from nose.tools import ok_
sys.path.insert(0, os.path.abspath('..'))

import procinfo


def test_return_human_readable():
    ok_(procinfo.return_human_readable(3035918336L), {'value': 2.83, 'str': '2.83 GB'})
