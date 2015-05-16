#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Code devoted to querying for job info as xml
'''

import subprocess as sp

from .parser import JobsParser


def get_jobs(user=None):
    '''
    Query for queued jobs and return a list of dictionaries.

    :param user: User to query for. Default to '*'
    :returns: list of dictionaries of jobs
    '''
    xml_text = fetch_xml(user=user)
    parser = JobsParser(xml_text)
    return parser.jobs


def fetch_xml(user=None):
    '''
    Use `qstat` to query for jobs, with the `-xml` flag to get xml data, ready for
    parsing.
    '''
    cmd = ['qstat', '-xml']
    if user is not None:
        cmd.extend(['-u', user])
    return sp.check_output(list(map(str, cmd)))
