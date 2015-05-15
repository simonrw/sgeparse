#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import os


@pytest.fixture
def root():
    return os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))


@pytest.fixture
def data(root):
    return os.path.join(root, 'testing', 'data', 'qjobs.xml')
