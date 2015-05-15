#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess as sp

from .parser import JobsParser


def get_jobs():
    xml_text = fetch_xml()
    parser = JobsParser(xml_text)
    return parser.jobs


def fetch_xml():
    cmd = ['qstat', '-xml']
    return sp.check_output(cmd)
