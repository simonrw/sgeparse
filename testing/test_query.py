#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from unittest import mock
except ImportError:
    import mock

from sgeparse.query import get_jobs, fetch_xml


def test_query(data):
    with mock.patch('sgeparse.query.fetch_xml') as fetch_xml:
        with open(data) as infile:
            fetch_xml.return_value = infile.read()

        jobs = get_jobs()

    assert jobs[0]['owner'] == 'sw'


@mock.patch('subprocess.Popen')
def test_fetch_xml(Popen, data):
    with open(data) as infile:
        xml_text = infile.read()

    # Nasty mocking of Popen
    process = Popen.return_value.__enter__.return_value
    process.poll.return_value = 0
    process.communicate.return_value = (xml_text, '')
    Popen.return_value.communicate.return_value = (xml_text, '')
    Popen.return_value.poll.return_value = 0

    xml = fetch_xml()
    assert 'queue_info' in xml


@mock.patch('subprocess.check_output')
def test_fetch_with_user_arg(check_output):
    fetch_xml(user='*')
    check_output.assert_called_once_with(['qstat', '-xml', '-u', '*'])
