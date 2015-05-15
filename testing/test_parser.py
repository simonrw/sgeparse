from sgeparse import JobsParser
import pytest


@pytest.fixture
def parser(data):
    return JobsParser(data)


def test_parse_testdata(parser):
    assert parser.njobs > 5


def test_first_job(parser):
    assert next(parser.jobs).owner == 'sw'
