#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import datetime

from sgeparse.parser import JobsParser


@pytest.fixture
def parser(data):
    with open(data) as infile:
        return JobsParser(infile.read())


def test_parse_testdata(parser):
    assert parser.njobs > 5


def test_first_job(parser):
    assert parser.jobs[0] == {
        'job_number': 1031650,
        'priority': 0.60500,
        'name': 'k2_3b802-20150513',
        'owner': 'sw',
        'state': 'r',
        'start_time': datetime.datetime(2015, 5, 15, 13, 38, 8),
        'queue': 'parallel',
        'host': 'ngts08.local',
        'slots': 12,
    }
