from sgeparse import JobsParser


def test_parse_testdata(data):
    parser = JobsParser(data)
    assert len(parser.jobs) > 5
