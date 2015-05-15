#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess as sp

from .parser import JobsParser


def get_jobs(user=None):
    xml_text = fetch_xml(user=user)
    parser = JobsParser(xml_text)
    return parser.jobs


def fetch_xml(user=None):
    cmd = ['qstat', '-xml']
    if user is not None:
        cmd.extend(['-u', user])
    return sp.check_output(list(map(str, cmd)))
