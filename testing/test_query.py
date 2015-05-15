try:
    from unittest import mock
except ImportError:
    import mock

from sgeparse.query import get_jobs


def test_query(data):
    with mock.patch('sgeparse.query.fetch_xml') as fetch_xml:
        with open(data) as infile:
            fetch_xml.return_value = infile.read()

        jobs = get_jobs()

    assert jobs[0]['owner'] == 'sw'
